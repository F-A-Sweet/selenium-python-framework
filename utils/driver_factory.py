from selenium import webdriver


class DriverFactory:

    @staticmethod
    def get_driver(browser):

        browser = browser.lower()

        if browser == "chrome":

            options = webdriver.ChromeOptions()

            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")

            driver = webdriver.Chrome(options=options)

        elif browser == "firefox":

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")

            driver = webdriver.Firefox(options=options)

        elif browser == "edge":

            options = webdriver.EdgeOptions()
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")

            driver = webdriver.Edge(options=options)

        else:
            raise Exception(
                f"Browser '{browser}' is not supported."
            )

        driver.implicitly_wait(5)

        print(f"Launching {browser} browser...")

        return driver