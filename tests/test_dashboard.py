import pytest
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
def test_dashboard(login_page):

    # Login
    login_page.login("Admin", "admin123")

    # Create Dashboard Page Object
    dashboard = DashboardPage(login_page.driver)

    # Verify Dashboard
    assert dashboard.is_dashboard_displayed()