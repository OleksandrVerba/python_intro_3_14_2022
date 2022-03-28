print('Calculator')
print('Chose:')
print('1. Add')
print('2. Sub')
print('3. Mul')
print('4. Div')
input_choice = int(input('Enter: '))
if input_choice == 1:
    first_operand = int(input("Enter first operand: "))
    second_operand = int(input("Enter second operand: "))
    output = first_operand + second_operand
    print('Sum =', output)
elif input_choice == 2:
    first_operand = int(input("Enter first operand: "))
    second_operand = int(input("Enter second operand: "))
    output = first_operand - second_operand
    print('Difference =', output)
elif input_choice == 3:
    first_operand = int(input("Enter first operand: "))
    second_operand = int(input("Enter second operand: "))
    output = first_operand * second_operand
    print('Product =', output)
elif input_choice == 4:
    first_operand = int(input("Enter first operand: "))
    second_operand = int(input("Enter second operand: "))
    output = first_operand / second_operand
    print('Quotient =', output)
else:
    print('Invalid Choice')
