############################################################
# Task_00
# my_list_00 = ["Clarke", "Asimov", "Heinlein", "Kennedy", "Banks", "Adams", "Bradbury", "Capek",
#               "Boule", "Cherryh", "Niven", "Le Guin", "Wolfe", "Lee", "Shelley", "Verne", "Wells",
#               "Butler", "Dick", "Lem"]
# new_list_00 = []
# for index in range(0,len(my_list_00),2):
#     my_list_00[index] = my_list_00[index][::-1]
#     new_list_00.append(my_list_00)
# print(new_list_00)

############################################################
# Task_01

# my_list_01 = ["Clarke", "Asimov", "Heinlein", "Kennedy", "Banks", "Adams", "Bradbury", "Capek",
#               "Boule", "Cherryh", "Niven", "Le Guin", "Wolfe", "Lee", "Shelley", "Verne", "Wells",
#               "Butler", "Dick", "Lem"]
# new_list_01 = []
# for element_01 in my_list_01:
#     if element_01.startswith('a'):
#         new_list_01.append(element_01)
# print(new_list_01)

############################################################
# Task_02

# my_list_02 = ["Clarke", "Asimov", "Heinlein", "Kennedy", "Banks", "Adams", "Bradbury", "Capek",
#               "Boule", "Cherryh", "Niven", "Le Guin", "Wolfe", "Lee", "Shelley", "Verne", "Wells",
#               "Butler", "Dick", "Lem"]
# new_list_02 = []
# for element_02 in my_list_02:
#     if 'a' in element_02:
#         new_list_02.append(element_02)
# print(new_list_02)

############################################################
# Task_03

# persons = [{"name": "John", "age": 20},
#            {"name": "Erica", "age": 15},
#            {"name": "Jack", "age": 35}]

# lower_age_03_a = []
# sorting_list_03_a = []
#
# for dictionary_03_a in persons:
#     sorting_list_03_a.append(dictionary_03_a["age"])
# lesser_number_03_a = min(sorting_list_03_a)
# for dictionary_03_a_a in persons:
#     if dictionary_03_a_a["age"] == lesser_number_03_a:
#         lower_age_03_a.append(dictionary_03_a_a["name"])
# print(lower_age_03_a)

# sorting_list_03_b_a = []
# longest_names_03_b = []
# for dictionary_03_b_a in persons:
#     sorting_list_03_b_a.append(len(dictionary_03_b_a["name"]))
# biggest_number_03 = max(sorting_list_03_b_a)
# for dictionary_03_b_b in persons:
#     if len(dictionary_03_b_b["name"]) == biggest_number_03:
#         longest_names_03_b.append(dictionary_03_b_b["name"])
# print(longest_names_03_b)

# new_list_03_c = []
# for age_03 in persons:
#     new_list_03_c.append(age_03["age"])
# average_age = sum(new_list_03_c) / len(persons)
# print(average_age)

############################################################
# Task_04

# my_dict_1 = {"first": 1, "second": "two", "third": 3.3}
# my_dict_2 = {"first": 1, "second": "two", "fourth": True}

# both_keys_list_04_a = list(set(my_dict_1.keys()) & (my_dict_2.keys()))
# print(both_keys_list_04_a)
#
# first_keys_list_04_b = list(set(my_dict_1.keys()) - (my_dict_2.keys()))
# print(first_keys_list_04_b)

# first_keys_list_04_c = list(set(my_dict_1.keys()) - (my_dict_2.keys()))
# for key_04_c in first_keys_list_04_c:
#     dict_of_first_keys_04_c = {key_04_c: my_dict_1[key_04_c]}
# print(dict_of_first_keys_04_c)

# dict_1_copy_04_d = my_dict_1.copy()
# for key_04_d in my_dict_2:
#     if key_04_d in dict_1_copy_04_d:
#         dict_1_copy_04_d[key_04_d] = [dict_1_copy_04_d[key_04_d], my_dict_2[key_04_d]]
#     else:
#         dict_1_copy_04_d[key_04_d] = my_dict_2[key_04_d]
# print(dict_1_copy_04_d)
