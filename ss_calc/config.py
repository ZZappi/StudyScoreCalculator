import yaml


def open_config_file():
    with open(CONFIG_FILE_DIRECTORY) as c:
        yaml_out = yaml.safe_load(c)
    return yaml_out


CONFIG_FILE_DIRECTORY = "config.yml"
configuration = open_config_file()

DATA_FILE_EXTENSION = configuration["FILES"]["EXTENSION"]
DATA_FILE_DIRECTORY = configuration["FILES"]["DIRECTORY"]["DATA"]

GRADE_LETTERS = configuration["STUDY_SCORE_CALC"]["DATA"]["GRADE_LETTERS"]

GA_NUM = configuration["STUDY_SCORE_CALC"]["DATA"]["GA_NUM"]


