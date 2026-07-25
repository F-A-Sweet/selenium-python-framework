import pytest


@pytest.mark.regression
def test_dashboard(dashboard_page):

    assert dashboard_page.is_dashboard_displayed()