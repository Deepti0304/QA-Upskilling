import csv
import logging


def read_csv(file_name):

    rows = []

    try:

        with open(file_name, "r") as file:

            reader = csv.reader(file)

            for row in reader:
                rows.append(row)

        logging.info(f"Successfully read file: {file_name}")

        return rows

    except FileNotFoundError as e:

        logging.error(f"File not found: {file_name}")

        raise

    except csv.Error as e:

        logging.error(f"Malformed CSV: {e}")

        raise

    except Exception as e:

        logging.error(f"Unexpected Error: {e}")

        raise