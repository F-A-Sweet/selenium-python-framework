from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.wait_for_element(locator).click()

    def type(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def get_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    def is_displayed(self, locator):
        return self.wait_for_element(locator).is_displayed()

    def get_current_url(self):
        return self.driver.current_url


    def get_title(self):
        return self.driver.title