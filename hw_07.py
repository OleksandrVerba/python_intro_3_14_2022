# import random
# import string
# from random import randint

############################################################
# Task_01

# def reverse_item_01(my_list):
#     new_list = []
#     for index in range(0,len(my_list),2):
#         my_list[index] = my_list[index][::-1]
#         new_list.append(my_list)
#
#     return new_list
#
#
# my_list = ["Clarke", "Asimov", "Heinlein", "Kennedy", "Banks", "Adams", "Bradbury", "Capek",
#            "Boule", "Cherryh", "Niven", "Le Guin", "Wolfe", "Lee", "Shelley", "Verne", "Wells",
#            "Butler", "Dick", "Lem"]
# result_01 = reverse_item_01(my_list)
# print(result_01)

############################################################
# Task_02

# def return_first_a_items_02(my_list):
#     new_list = []
#     for element in my_list:
#         if element.startswith('a'):
#             new_list.append(element)
#     return new_list
#
#
# my_list = ["Clarke", "Asimov", "Heinlein", "Kennedy", "Banks", "Adams", "Bradbury", "Capek",
#            "Boule", "Cherryh", "Niven", "Le Guin", "Wolfe", "Lee", "Shelley", "Verne", "Wells",
#            "Butler", "Dick", "Lem"]
# result_02 = return_first_a_items_02(my_list)
# print(result_02)

############################################################
# Task_03

# def return_any_a_items_03(my_list):
#     new_list = []
#     for element in my_list:
#         if 'a' in element:
#             new_list.append(element)
#     return new_list
#
#
# my_list = ["Clarke", "Asimov", "Heinlein", "Kennedy", "Banks", "Adams", "Bradbury", "Capek",
#            "Boule", "Cherryh", "Niven", "Le Guin", "Wolfe", "Lee", "Shelley", "Verne", "Wells",
#            "Butler", "Dick", "Lem"]
# result_03 = return_any_a_items_03(my_list)
# print(result_03)

############################################################
# Task_04


# def append_string_only_04(my_list):
#     new_list = []
#     for string_item in my_list:
#         if type(string_item) == str:
#             new_list.append(string_item)
#     return new_list
#
#
# my_list = ["one", 1, "two", 2, "three", 3]
# result_04 = append_string_only_04(my_list)
# print(result_04)

############################################################
# Task_05

# def get_non_repeated_values_05(my_str):
#     new_list = list(set(my_str))
#
#     return new_list
#
#
# my_str = ["one", 1, "two", 2, "three", 3, "one", 1, "three", 3]
#
# result_05 = get_non_repeated_values_05
# print(result_05)

############################################################
# Task_06

# def get_new_list_06(string_06_a, string_06_b):
#     new_list = list(set(string_06_a) & set(string_06_b))
#     return new_list
#
#
# string_06_a = "Monty"
# string_06_b = "Python"
# result_06 = get_new_list_06(string_06_a, string_06_b)
# print(get_new_list_06(string_06_a, string_06_b))

############################################################
# Task_07

# def something(string_07_a, string_07_b):
#     list_07 = []
#     for symbol_07 in set(string_07_a).intersection(string_07_b):
#         if string_07_a.count(symbol_07) == 1 and string_07_b.count(symbol_07) == 1:
#             list_07.append(symbol_07)
#     return list_07
#
#
# string_07_a = "aaaasdf1"
# string_07_b = "Pasdfff2"
#
# result_07 = something(string_07_a, string_07_b)
# print(result_07)

############################################################
# Task_08

# def generate_address_08(names, domains):
#     e_mail = names[randint(0, len(names) -1)] + "." + str(randint(100, 999))\
#              + "@" + "".join(random.choices(string.ascii_lowercase, k=randint(5, 7))) + "."\
#              + domains[randint(0, len(domains) -1)]
#     return e_mail
#
#
# names = ["king", "miller", "kean", "smith"]
# domains = ["net", "com", "ua"]
# result_08 = generate_address_08(names, domains)
# print(result_08)
