"""Write data to CSV"""
import csv
from typing import List


def read_csv_to_json_array(path: str, fieldnames: List[str]):
    """Helper method for reading csv rows into array of json objects"""

    json_array = []
    with open(path) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        for rows in reader:
            json_object = {}
            for key in fieldnames:
                json_object[key] = rows[key]
            json_array.append(json_object)

    return json_array


def write_results(path: str, data, fieldnames: List[str]):
    """Helper method for writing a List of Dicts to csv"""

    with open(path, "a", newline="") as file:
        for entry, value in data.items():
            file.write(f"{entry}  {value}\n")


def append_line(path: str, cells: List[str]):
    with open(path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(cells)