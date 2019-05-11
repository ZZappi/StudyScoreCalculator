import os

import config
import yaml

DATA_FILE_DIRECTORY = config.DATA_FILE_DIRECTORY
DATA_FILE_EXTENSION = config.DATA_FILE_EXTENSION


def check_file_extension(file_names):
    file_names_validated = []
    for file in file_names:
        if file.split(".")[1] != DATA_FILE_EXTENSION:
            pass
        else:
            file_names_validated.append(file)
    return file_names_validated


def get_file_names():
    file_names = check_file_extension(os.listdir(DATA_FILE_DIRECTORY))
    return file_names


def get_object_name(data_file_name):
    subject_data_raw = open_file(data_file_name)
    return subject_data_raw["INFO"]["NAME_OBJ"]


def get_ga_names(data_file_name):
    subject_data_raw = open_file(data_file_name)
    ga_names = {}
    for x in range(len(subject_data_raw["DATA"])):
        x = x + 1
        ga_names["".join(subject_data_raw["DATA"]["GA" + str(x)]["NAME"])] = None
    return ga_names


def open_file(data_file_name):
    data_file_name = DATA_FILE_DIRECTORY + data_file_name
    with open(data_file_name) as c:
        subject_data_raw = yaml.safe_load(c)
    return subject_data_raw
