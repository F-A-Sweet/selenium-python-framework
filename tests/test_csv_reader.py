from utils.csv_reader import CSVReader

def test_read_csv():

    data = CSVReader.read_csv(
        "testdata/login_data.csv"
    )

    print(data)

    assert len(data) == 3