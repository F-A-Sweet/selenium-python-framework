import pytest
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
def test_dashboard(dashboard_page):

    assert dashboard_page.is_dashboard_displayed()