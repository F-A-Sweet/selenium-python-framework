import os
from selenium import webdriver


class DriverFactory:

    @staticmethod
    def get_driver(browser):

        is_ci = os.getenv("CI") == "true"

        if browser.lower() == "chrome":

            options = webdriver.ChromeOptions()

            if is_ci:
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--window-size=1920,1080")

            driver = webdriver.Chrome(options=options)

        elif browser.lower() == "firefox":

            options = webdriver.FirefoxOptions()

            if is_ci:
                options.add_argument("--headless")

            driver = webdriver.Firefox(options=options)

        elif browser.lower() == "edge":

            options = webdriver.EdgeOptions()

            if is_ci:
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--window-size=1920,1080")

            driver = webdriver.Edge(options=options)

        else:
            raise Exception(
                f"Browser '{browser}' is not supported."
            )

        driver.maximize_window()
        driver.implicitly_wait(5)

        print(f"Launching {browser} browser...")

        return driver