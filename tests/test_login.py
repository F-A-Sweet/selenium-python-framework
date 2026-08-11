import pytest

from utils.csv_reader import CSVReader


test_data = CSVReader.read_csv(
    "testdata/login_data.csv"
)


@pytest.mark.regression
@pytest.mark.parametrize("data", test_data)
def test_login(login_page, data):

    dashboard = login_page.login(
        data["username"],
        data["password"]
    )

    if data["expected"]:
        assert dashboard.is_dashboard_displayed()
    else:
        assert (
            login_page.get_login_error()
            == "Invalid credentials"
        )