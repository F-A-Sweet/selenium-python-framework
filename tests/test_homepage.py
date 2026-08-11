import pytest

from pages.login_page import LoginPage
from utils.config_reader import ConfigReader


@pytest.mark.smoke
def test_homepage(driver):

    driver.get(ConfigReader.get_base_url())

    login_page = LoginPage(driver)

    assert "OrangeHRM" in login_page.get_title()