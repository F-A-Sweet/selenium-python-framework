import pytest
from utils.driver_factory import DriverFactory
from utils.screenshot import Screenshot


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
        driver = item.funcargs["driver"]
        Screenshot.capture(driver, item.name)

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    driver = DriverFactory.get_driver(browser)

    yield driver

    driver.quit()