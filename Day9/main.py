import logger_config

from csv_reader import read_csv


try:

    data = read_csv("sample.csv")

    print("\nCSV DATA\n")

    for row in data:
        print(row)

except Exception as e:

    print(f"Program failed: {e}")