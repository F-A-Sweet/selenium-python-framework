import pytest
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
def test_logout(login_page):

    # Login
    login_page.login("Admin", "admin123")

    # Dashboard Page
    dashboard = DashboardPage(login_page.driver)

    # Verify Dashboard
    assert dashboard.is_dashboard_displayed()

    # Logout
    dashboard.logout()

    # Verify Login Page
    assert "login" in login_page.driver.current_url.lower()