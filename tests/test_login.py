import pytest
# from pages.login_page import LoginPage
# from utils.config_reader import ConfigReader
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

    login_page.login(
        data["username"],
        data["password"]
    )

    # print("Current URL:", driver.current_url)
    # print("Page Title:", driver.title)
    # print("Page Source contains Invalid?:", "Invalid" in driver.page_source)

    if data["expected"]:
        assert "dashboard" in login_page.driver.current_url.lower()
    else:
        assert "dashboard" not in login_page.driver.current_url.lower()