# #################################################
# Task_01
#
# int_number_01 = 930120802158390350025208340200824
# result_01 = str(int_number).count('0')
# print(result_01)
#
# #################################################
# Task_02
#
# int_number_02 = 900800060000000000000
# container_02 = ''
# for symbol_02 in reversed(str(int_number_02)):
#     if symbol_02 in '0':
#         container_02 += symbol_02
#     elif symbol_02 not in '0':
#         break
# result_02 = len(container_02)
# print(result_02)
#
# ########################################
# Task_03
#
# my_list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# my_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# my_result = []
# my_result += my_list_1[::2]
# my_result += my_list_2[0::2]
# print(my_result)
#
# ########################################
# Task_04
#
# my_list = [1, 2, 3, 4]
# new_list = []
# new_list += my_list
# new_list.insert(len(new_list), new_list.pop(0))
# print(new_list)
#
# ########################################
# Task_05
#
# my_list = [1, 2, 3, 4]
# my_list.insert(len(my_list), my_list.pop(0))
# print((my_list))
#
# ########################################
# Task_06
#
# string_06 = '33 is less than 44 and 55 but more than 22'
# container_06 = []
# for numbers in string_06.split():
#     if numbers.isdigit() is False:
#         continue
#     container_06.append(int(numbers))
# result_06 = sum(container_06)
# print(result_06)
#
# ########################################
# # Task_07
#
# my_str = 'My long string'
# l_limit = "o"
# r_limit = "g"
#
# start_07 = my_str.find(l_limit)
# end_07 = my_str.rfind(r_limit)
# sub_str = my_str[start_07:end_07]
# print(sub_str)
#
# ########################################
# Task_08
#
# my_str = 'Python?'
# list_08 = []
# result = my_str + '_' if len(my_str) % 2 else my_str
# for symbol_08 in range(0, len(result), 2):
#     list_08.append(result[symbol_08:symbol_08 + 2])
# print(list_08)
#
# ########################################
# Task_09
#
# list_09 = [2, 4, 1, 5, 3, 9, 0, 7]
# result = 0
# for symbol_09 in range(1, len(list_09), -1):
#     if list_09[symbol_09] > (list_09[symbol_09 - 1] + list_09[symbol_09 + 1]):
#         result += 1
# print(result)
#
# ########################################
# Task_10
#
# my_list = [1, 2, 3, "11", "22", 33]
# new_list_10 = []
# for symbol_10 in my_list:
#     if type(symbol_10) == str:
#         new_list_10.append(symbol_10)
# print(new_list_10)
#
# ########################################
# Task_11
#
# my_str = 'Monty Python'
# list_11 = list(set(my_str))
# print(list_11)
#
# ########################################
# Task_12
#
# string_12_0 = "Monty"
# string_12_1 = "Python"
# list_12 = list(set(string_12_0) & set(string_12_1))
# print(list_12)
#
# ########################################
# Task_13
#
# string_13_0 = "aaaasdf1"
# string_13_1 = "Pasdfff2"
# list_13 = []
# for symbol_13 in set(string_13_0).intersection(string_13_1):
#     if string_13_0.count(symbol_13) == 1 and string_13_1.count(symbol_13) == 1:
#         list_13.append(symbol_13)
# print(list_13)
