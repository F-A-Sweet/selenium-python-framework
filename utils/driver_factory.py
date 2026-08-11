from selenium import webdriver

from utils.config_reader import ConfigReader


class DriverFactory:

    @staticmethod
    def get_driver(browser):

        browser = browser.lower()

        if browser == "chrome":
            driver = webdriver.Chrome()

        elif browser == "firefox":
            driver = webdriver.Firefox()

        elif browser == "edge":
            driver = webdriver.Edge()

        else:
            raise ValueError(
                f"Browser '{browser}' is not supported."
            )

        driver.maximize_window()
        driver.implicitly_wait(
            ConfigReader.get_implicit_wait()
        )

        print(f"Launching {browser} browser...")

        return driver