from utils.excel_reader import ExcelReader


def test_read_excel():

    data = ExcelReader.read_login_data(
        "testdata/login_data.xlsx",
        "LoginData"
    )

    print(data)

    assert len(data) == 3