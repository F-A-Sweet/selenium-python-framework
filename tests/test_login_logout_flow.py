import pytest

from utils.config_reader import ConfigReader


@pytest.mark.regression
def test_login_logout_flow(login_page):

    dashboard_page = login_page.login(
        ConfigReader.get_username(),
        ConfigReader.get_password()
    )

    assert dashboard_page.is_dashboard_displayed()

    login_page = dashboard_page.logout()

    assert "login" in login_page.get_current_url().lower()