import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
# from utils.screenshot import Screenshot
# from utils.json_reader import JsonReader
# from utils.excel_reader import ExcelReader
from utils.csv_reader import CSVReader

# test_data = JsonReader.read_json("testdata/login_data.json")

# test_data = ExcelReader.read_login_data(
#     "testdata/login_data.xlsx",
#     "LoginData"
# )

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
        assert login_page.is_login_failed()