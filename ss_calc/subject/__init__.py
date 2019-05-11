import config
import file_reader

GRADE_LETTERS = config.GRADE_LETTERS
GA_NUM = config.GA_NUM
DATA_FILE_EXTENSION = config.DATA_FILE_EXTENSION

object_name_dict = {}

class Subject:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.ga_names = {}

        for i in range(GA_NUM):
            ga_name_temp = "GA" + str(i + 1)
            self.ga_names[ga_name_temp] = GradedAssessment(ga_name_temp)


class GradedAssessment:
    def __init__(self, ga_name):
        self.grade = dict(dict.fromkeys(GRADE_LETTERS))
        self.ga_name = ga_name

    def create_letter_grades(self, score_range):
        score_range_keys = list(score_range.keys())
        for i in range(len(score_range)):
            letter = score_range_keys[i]
            self.grade[letter] = LetterGrade(letter, GRADE_LETTERS[letter], score_range[letter])
        return


class LetterGrade:
    def __init__(self, name_obj, name, score_range_split):
        self.name_obj = name_obj
        self.name = name
        self.score_range_split = score_range_split

        self.range_split = self.calc_score_range()

        self.minimum = int(self.range_split[0])
        self.maximum = int(self.range_split[1])
        self.range = self.maximum - self.minimum

    def calc_score_range(self):
        return self.score_range_split.split("-")


def create_subject_from_file(file_name, ga_names=None):

    object_name_str = str(file_reader.get_object_name(file_name))
    object_name_dict["".join(object_name_str)] = None

    subject_data_raw = file_reader.open_file(file_name)

    object_name_dict[object_name_str] = Subject(subject_data_raw["INFO"]["NAME"],
                                                         str(subject_data_raw["INFO"]["YEAR"]))

    for i in range(GA_NUM):
        i = i + 1

        object_name_dict[object_name_str].ga_names["GA" + str(i)].create_letter_grades(
            subject_data_raw["DATA"]["GA" + str(i)]["GRADE_RANGE"])

    return object_name_dict, ga_names
