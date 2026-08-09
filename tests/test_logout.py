import pytest

from pages.dashboard_page import DashboardPage


@pytest.mark.regression
def test_logout(dashboard_page: DashboardPage):

    # # Login
    # login_page.login("Admin", "admin123")

    # # Dashboard Page
    # dashboard = DashboardPage(login_page.driver)

    # # Verify Dashboard
    # assert dashboard.is_dashboard_displayed()

    # Logout
    login_page = dashboard_page.logout()

    # Verify Login Page
    assert "login" in login_page.get_current_url().lower()