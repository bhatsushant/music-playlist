import json
import os.path
import pandas as pd


def get_json_data_from_json_file(json_file):
    with open(json_file, "r") as jf:
        json_data = json.load(jf)
        return json_data


def get_normalized_json_data(jd):
    normalized_data = {}

    for key, values in jd.items():
        for index, value in values.items():
            if index not in normalized_data:
                normalized_data[index] = {}
            normalized_data[index][key] = value
            normalized_data[index]["star_rating"] = 0

    return normalized_data


def create_normalized_json_file(json_data, json_file_path):
    if os.path.exists(json_file_path):
        return

    with open(json_file_path, "w") as outfile:
        json.dump(json_data, outfile)


def get_data():
    NORMALIZED_JSON_FILE_PATH = "normalized_playlist.json"

    if os.path.exists(NORMALIZED_JSON_FILE_PATH):
        return get_data_frame_from_json(
            get_json_data_from_json_file(NORMALIZED_JSON_FILE_PATH)
        )

    JSON_FILE_PATH = "playlist.json"
    jd = get_json_data_from_json_file(JSON_FILE_PATH)
    nd = get_normalized_json_data(jd)

    create_normalized_json_file(nd, NORMALIZED_JSON_FILE_PATH)

    return get_data_frame_from_json(
        get_json_data_from_json_file(NORMALIZED_JSON_FILE_PATH)
    )


def get_data_frame_from_json(json):
    df = pd.DataFrame.from_dict(json)
    df.index.name = "index"
    return df.transpose()
