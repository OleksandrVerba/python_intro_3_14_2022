import os
import random

################################################################################
# task_01


def get_file_and_dir_names(dir_name: str) -> dict:
    files_01 = [file_01 for file_01 in os.listdir(os.chdir(dir_name)) if os.path.isfile(file_01)]
    directory_01 = [directory_01 for directory_01 in os.listdir(os.chdir(dir_name)) if os.path.isdir(directory_01)]
    dictionary_01_a = {'filenames': files_01, 'dirnames': directory_01}
    return dictionary_01_a


################################################################################
# task_02


def get_sorted_file_and_dir_names(dictionary_01_b, bool_value: bool = True) -> dict:
    values_b = [*dictionary_01_b.values()]
    values_b[0].sort(), values_b[1].sort() if bool_value else values_b[0].reverse(), values_b[1].reverse()
    dictionary_02 = {'filenames': values_b[0], 'dirnames': values_b[1]}
    return dictionary_02


bool_value = True
dir_name = os.getcwd()
dictionary_01_b = get_file_and_dir_names(dir_name)

################################################################################
# task_03


def randomize_values(dictionary_01_b, string_c: str) -> dict:
    files_03 = []
    dicts_03 = []
    if string_c in dictionary_01_b["filenames"]:
        files_03.append(string_c)
    if string_c in dictionary_01_b["dirnames"]:
            dicts_03.append(string_c)
    dictionary_03 = {'filenames': files_03, 'dirnames': dicts_03}
    return dictionary_03


dict_values = [*dictionary_01_b.values()]
string_c = random.choice(sum(dict_values, []))
