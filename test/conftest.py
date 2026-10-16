
import pytest
import config
import os
from pages.login_page import LoginPage




@pytest.fixture(scope="session")
def credentials():
    return {"email": os.getenv("ADMIN_EMAIL"), "password": os.getenv("ADMIN_PASSWORD")}




@pytest.fixture
def login_page(page):
   return LoginPage(page, config.BASE_URL).open()



@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict) -> dict :

    return {
        **browser_context_args,
        "http_credentials": {
            "username": os.environ["SPENDWISE_GATE_USER"],
            "password": os.environ["SPENDWISE_GATE_PASS"],
        },
        "ignore_https_errors": False,
}
