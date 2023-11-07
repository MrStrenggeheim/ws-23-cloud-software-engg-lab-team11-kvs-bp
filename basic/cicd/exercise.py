from sqlitedict import SqliteDict
import json
import os
import sys


dict_source = "exercise-data.sqlite"
json_source = "data.json"


def make_dict(key, value):
    db = SqliteDict(dict_source)
    db.clear()
    db[key] = value
    db.commit()
    db.close()


def source_exist(source):
    if not os.path.exists(source):
        raise "Source does not exist"


def dict2json():
    source_exist(dict_source)
    with open(json_source, "w") as f:
        db = SqliteDict(dict_source)
        json.dump({k: v for k, v in db.items()}, f)
        db.close()

def check_json(key, value):
    source_exist(json_source)
    with open("data.json") as f:
        data = json.load(f)
        assert data[key] == value


if __name__ == "__main__":
    cmd = sys.argv[1]
    key, value = "ci-cd", "CI/CD is fun"
    if cmd == "md":
        make_dict(key, value)
    elif cmd == "d2j":
        dict2json()
    elif cmd == "cj":
        check_json(key, value)