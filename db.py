import os
import json


def create_database(filename="database"):

    file = filename + ".json"
    if not os.path.exists(file):
        with open(file, mode="w", encoding="utf-8") as db_file:
            json.dump({}, db_file)

        print("Database created successfully...")

    else:
        print("Database already exists...")




