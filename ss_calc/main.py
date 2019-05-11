import config
import file_reader
import subject

DATA_FILE_EXTENSION = config.DATA_FILE_EXTENSION
GRADE_LETTERS = config.GRADE_LETTERS

file_names = file_reader.get_file_names()

for file in file_names:
    dictionary = (subject.create_subject_from_file(file))[0]
    ga_names = (subject.create_subject_from_file(file))[1]

for subject in list(dictionary.keys()):
    print("")
    print(dictionary[subject].name + ":")

    for x in dictionary[subject].ga_names:
        print("\t\t" + x + ":")
        for y in GRADE_LETTERS:
            print("\t\t\t" + y + "\t |\t", end="")
            print(str(dictionary[subject].ga_names[x].grade[y].minimum) + " - ", end="")
            print(str(dictionary[subject].ga_names[x].grade[y].maximum))

range_max = 0
for x in dictionary[subject].ga_names:
    for y in GRADE_LETTERS:
        range_current = dictionary[subject].ga_names[x].grade[y].range
        if range_max < range_current:
            range_max = range_current
print(range_max)
