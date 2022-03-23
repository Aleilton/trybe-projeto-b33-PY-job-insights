from functools import lru_cache
import csv


@lru_cache
def read(path):
    list_of_file = []
    with open(path) as file:
        file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in file_reader:
            list_of_file.append(row)
    return list_of_file
