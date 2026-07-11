import pytest
from utils.driver_factory import DriverFactory


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose browser: chrome, firefox, edge"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    driver = DriverFactory.get_driver(browser)

    yield driver

    driver.quit()