domains_08 = "hw_08_domains.txt"
names_08 = "hw_08_names.txt"
authors_08 = "hw_08_authors.txt"
############################################################
# Task_02

# def return_domains(domains_08):
#     with open(domains_08, 'r') as first_file:
#         data_a = first_file.read()
#     numbers_08_a = []
#     for line in data_a.split("\n"):
#         number = line.replace(".", "")
#         numbers_08_a.append(number)
#
#     return numbers_08_a
#
#
# result_08_a = return_domains(domains_08)
# print(result_08_a)

############################################################
# Task_02
# def return_names(names_08):
#     with open(names_08, "r") as second_file:
#         data_b = second_file.read()
#     names_list_08_b = []
#     for line in data_b.split("\n"):
#         number = line.split("\t")[1]
#         names_list_08_b.append(number)
#
#     return names_list_08_b
#
#
# result_08_b = return_names(names_08)
# print(result_08_b)

############################################################
# Task_03
# def return_dicts(authors_08):
#     with open(authors_08) as third_file:
#         data_c = third_file.read()
#     dicts_c = []
#     for line in data_c.split("\n"):
#         a = line.split("-")
#         if len(a) > 1:
#             dict_item = {"date": a[0]}
#             dicts_c.append(dict_item)
#     return dicts_c
#
#
# result_08_c = return_dicts(authors_08)
# print(result_08_c)
