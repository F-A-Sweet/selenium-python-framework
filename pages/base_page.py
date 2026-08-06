from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.wait_for_clickable(locator).click()

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

    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_presence(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_invisibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_url(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url)
        )

    def wait_for_title(self, title, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.title_contains(title)
        )