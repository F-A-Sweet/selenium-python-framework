from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import LogGen

class LoginPage(BasePage):

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button")

    def __init__(self,driver):
        super().__init__(driver)
        self.logger = LogGen.get_logger()

    def enter_username(self, username):
        self.type(self.USERNAME, username)

    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.logger.info("Entering username")
        self.enter_username(username)

        self.logger.info("Entering password")
        self.enter_password(password)

        self.logger.info("Clicking login")
        self.click_login()