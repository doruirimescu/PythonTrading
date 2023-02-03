from Trading.utils.time import get_date_now_cet
from Trading.config.config import DATA_STORAGE_PATH
import os
import json


def write_to_json_file(file_name: str, data_dict: dict) -> None:
    f = open(file_name, 'w')
    json_object = json.dumps(data_dict, indent=4)
    f.write(json_object)
    f.close()

def read_json_file(file_name: str) -> dict:
    try:
        with open(file_name, 'r+') as f:
            json_data = json.load(f)
            return json_data
    except Exception as e:
        return None

def write_json_to_file_named_with_today_date(json_dict, file_path: str):
    data_path = os.getenv("DATA_STORAGE_PATH", "data/")
    date_today = get_date_now_cet()
    json_path = data_path + file_path + str(date_today) + ".json"
    f = open(json_path, 'w')
    json_object = json.dumps(json_dict, indent=4)
    f.write(json_object)
    f.close()


def read_json_from_file_named_with_today_date(file_path: str):
    date_today = get_date_now_cet()
    json_path = DATA_STORAGE_PATH + file_path + str(date_today) + ".json"
    try:
        with open(json_path, 'r+') as f:
            json_data = json.load(f)
            return json_data
    except Exception as e:
        return None
