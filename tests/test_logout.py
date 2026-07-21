import pytest
# from pages.dashboard_page import DashboardPage


@pytest.mark.regression
def test_logout(dashboard_page):

    # # Login
    # login_page.login("Admin", "admin123")

    # # Dashboard Page
    # dashboard = DashboardPage(login_page.driver)

    # # Verify Dashboard
    # assert dashboard.is_dashboard_displayed()

    # Logout
    dashboard_page.logout()

    # Verify Login Page
    assert "login" in dashboard_page.driver.current_url.lower()