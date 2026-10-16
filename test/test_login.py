import re
import pytest
from playwright.sync_api import expect




@pytest.mark.smoke
def test_login_exitoso(login_page, credentials):
    login_page.login(credentials["email"], credentials["password"])
    expect(login_page.page).not_to_have_url(re.compile(r"login"), timeout=20_000)


def test_login_password_incorrecto(login_page, credentials):
    login_page.login(credentials["email"], "password-incorrecto-123")
    expect(login_page.page).to_have_url(re.compile(r"login"))
    expect(login_page.error_message).to_be_visible(timeout=10_000)
