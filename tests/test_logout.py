import pytest

from pages.dashboard_page import DashboardPage


@pytest.mark.regression
def test_logout(dashboard_page: DashboardPage):

    login_page = dashboard_page.logout()

    assert "login" in login_page.get_current_url().lower()