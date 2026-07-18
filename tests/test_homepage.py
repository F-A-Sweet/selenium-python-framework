import pytest
from utils.config_reader import ConfigReader


@pytest.mark.smoke
def test_homepage(driver):

    driver.get(ConfigReader.get_base_url())

    assert "OrangeHRM" in driver.title