import json
import requests
import config
import os
from playwright.sync_api import sync_playwright
import config


def cookie_compuerta(nombre="sw_session"):
    """Pasa la compuerta con el navegador y devuelve la cookie de sesión."""
    with sync_playwright() as p:
        browser = p.chromium.launch()  # headless: Playwright mete la clave solo
        context = browser.new_context(
            http_credentials={
                "username": os.environ["SPENDWISE_GATE_USER"],
                "password": os.environ["SPENDWISE_GATE_PASS"],
            }
        )
        page = context.new_page()
        page.goto(config.BASE_URL + "/login")
        cookies = context.cookies()
        browser.close()

    cookie = next((c for c in cookies if c["name"] == "swgate_cesarclavijo30"), None)
    if not cookie:
        raise RuntimeError(f"No apareció la cookie {nombre}. Cookies: {[c['name'] for c in cookies]}")
    return cookie


def sesion_con_compuerta():
    c = cookie_compuerta()
    s = requests.Session()
    s.headers["Accept"] = "application/json"
    s.cookies.set(c["name"], c["value"], domain=c["domain"], path=c["path"])
    return s


def get_token(session, email, password):
    url = os.getenv("API_APP_BASE_URL") + os.getenv("API_LOGIN")
    resp = session.post(
        url,
        json={"email": email, "password": password},
        timeout=15,
        allow_redirects=False,
    )
    if resp.is_redirect:
        raise RuntimeError(f"{url} redirige a {resp.headers.get('Location')}: la cookie no pasó la compuerta")
    resp.raise_for_status()
    return resp.json()["accessToken"]



class SpendWiseAPI:
    def __init__(self, session):
        self.session = session
        self.session.headers["Accept"] = "application/json"


    def get(self, path, **params):
        return self.session.get(f"{config.API_BASE_URL}{path}", params=params, timeout=15)


    def me(self):
        return self.get("/api/v1/auth/me")


    def categories(self):
        return self.get("/api/v1/categories")


    def expenses(self):
        return self.get("/api/v1/expenses")