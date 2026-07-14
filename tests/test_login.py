from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from utils.screenshot import Screenshot

def test_login(driver):

    driver.get(ConfigReader.get_base_url())

    login = LoginPage(driver)

    login.login("Admin", "admin123")

    Screenshot.capture(driver, "login_test")

    print("Current URL:", driver.current_url)
    print("Page Title:", driver.title)
    print("Page Source contains Invalid?:", "Invalid" in driver.page_source)

    assert "dashboard" in driver.current_url.lower()