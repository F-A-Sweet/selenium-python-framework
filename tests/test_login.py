import pytest
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from utils.screenshot import Screenshot
from utils.json_reader import JsonReader

test_data = JsonReader.read_json("testdata/login_data.json")

@pytest.mark.regression
@pytest.mark.parametrize("data", test_data)

def test_login(driver, data):

    driver.get(ConfigReader.get_base_url())

    login = LoginPage(driver)

    login.login(
        data["username"],
        data["password"]
    )

    print("Current URL:", driver.current_url)
    print("Page Title:", driver.title)
    print("Page Source contains Invalid?:", "Invalid" in driver.page_source)

    if data["expected"]:
        assert "dashboard" in driver.current_url.lower()
    else:
        assert "dashboard" not in driver.current_url.lower()