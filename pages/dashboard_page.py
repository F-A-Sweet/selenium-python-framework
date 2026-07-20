from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):

    DASHBOARD_HEADER = (
        By.XPATH,
        "//h6[text()='Dashboard']"
    )

    PROFILE_DROPDOWN = (
        By.CLASS_NAME,
        "oxd-userdropdown-tab"
    )

    LOGOUT = (
        By.XPATH,
        "//a[text()='Logout']"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def is_dashboard_displayed(self):
        return self.wait_for_element(self.DASHBOARD_HEADER).is_displayed
    
    def logout(self):
        self.click(self.PROFILE_DROPDOWN)
        self.click(self.LOGOUT)