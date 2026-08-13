import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.driver_factory import DriverFactory
from utils.screenshot import Screenshot
from utils.config_reader import ConfigReader


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose browser: chrome, firefox, edge"
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            try:
                Screenshot.capture(driver, item.name)
            except Exception:
                pass


@pytest.fixture(scope="function")
def driver(request):

    browser = request.config.getoption("--browser")
    driver = DriverFactory.get_driver(browser)

    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture
def homepage(driver):

    driver.get(ConfigReader.get_base_url())
    return driver


@pytest.fixture
def login_page(homepage):

    return LoginPage(homepage)


@pytest.fixture
def dashboard_page(login_page):

    dashboard = login_page.login(
        ConfigReader.get_username(),
        ConfigReader.get_password()
    )

    return dashboard