import csv
import json
from openpyxl import load_workbook


class DataReader:

    @staticmethod
    def read_csv(file_path):

        with open(file_path, newline="") as file:
            return list(csv.DictReader(file))


    @staticmethod
    def read_json(file_path):

        with open(file_path) as file:
            return json.load(file)


    @staticmethod
    def read_excel(file_path):

        workbook = load_workbook(file_path)
        sheet = workbook.active

        rows = list(sheet.values)

        headers = rows[0]

        return [
            dict(zip(headers, row))
            for row in rows[1:]
        ]