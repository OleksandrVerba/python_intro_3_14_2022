# Task 01
my_list = [100, 101, 24, 3494, 467, 5, 60000, 75, 8, 99]
for numbers in my_list:
    if numbers > 100:
        print(numbers)

############################################################
# Task 02
my_list = [100, 101, 24, 3494, 467, 5, 60000, 75, 8, 99]
my_results = []
for numbers in my_list:
    if numbers > 100:
        my_results.append(numbers)
        print(my_results)

############################################################
# Task 03
my_list = [100, 101, 24, 3494, 467, 5, 60000, 75, 8, 99]
if len(my_list) < 2:
    my_list.append(0)
elif len(my_list) > 2:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)