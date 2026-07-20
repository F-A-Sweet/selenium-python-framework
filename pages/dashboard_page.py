from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):

    DASHBOARD_HEADER = (
        By.XPATH,
        "//h6[text()='Dashboard']"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def is_dashboard_displayed(self):
        return self.wait_for_element(self.DASHBOARD_HEADER).is_displayed