from utils.csv_reader import CSVReader


def test_read_csv():

    data = CSVReader.read_csv(
        "testdata/login_data.csv"
    )

    assert len(data) == 3