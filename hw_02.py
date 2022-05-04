# Task 01
value = 1
new_value = value / 2 if value < 100 else -value
print(new_value)

value = 100
new_value = value / 2 if value < 100 else -value
print(new_value)

# Task 02
value = 1
new_value = 1 if value < 100 else 0
print(new_value)

value = 100
new_value = 1 if value < 100 else 0
print(new_value)

# Task 03
value = 1
new_value = True if value < 100 else False
print(new_value)

value = 100
new_value = True if value < 100 else False
print(new_value)

# Task 04
my_str ='qwe'
new_str = my_str + my_str if len(my_str) < 5 else my_str
print(new_str)

my_str ='qwerty'
new_str = my_str + my_str if len(my_str) < 5 else my_str
print(new_str)

# Task 05
my_str ='qwe'
new_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(new_str)

my_str ='qwerty'
new_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(new_str)
