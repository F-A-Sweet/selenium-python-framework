import csv


class CSVReader:

    @staticmethod
    def read_csv(file_path):

        data = []

        with open(file_path, newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:
                row["expected"] = row["expected"] == "True"
                data.append(row)

            return data