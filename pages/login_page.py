from typing import Any
from playwright.sync_api import Page, expect




class LoginPage:
    PATH = "/login"


    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.email_input = page.get_by_test_id("login-email")
        self.password_input = page.get_by_test_id("login-password")
        self.login_button = page.get_by_test_id("login-submit")
        self.error_message = page.get_by_test_id("login-error")

    def open(self) -> Any :
        self.page.goto(f"{self.base_url}{self.PATH}")
        expect(self.email_input).to_be_visible()
        return self


    def login(self, email: str, password: str) -> None :
        self.email_input.click()
        self.email_input.fill(email)
        self.password_input.click()
        self.password_input.fill(password)
        self.login_button.click()
