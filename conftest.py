import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver

    print("\n\n\nClosing Browser...")

    driver.quit()