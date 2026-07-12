from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button")

    def __init__(self,driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.type(self.USERNAME, username)

    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        print("Entering username")
        self.enter_username(username)

        print("Entering password")
        self.enter_password(password)

        print("Clicking login")
        self.click_login()