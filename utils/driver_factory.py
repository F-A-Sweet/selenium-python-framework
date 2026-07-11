from selenium import webdriver


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser.lower() == "chrome":
            driver = webdriver.Chrome()

        elif browser.lower() == "firefox":
            driver = webdriver.Firefox()

        elif browser.lower() == "edge":
            driver = webdriver.Edge()

        else:
            raise Exception(f"Browser '{browser}' is not supported.")
        
        driver.maximize_window()
        driver.implicitly_wait(5)

        print(f"Launching {browser} browser...")

        return driver