try:
    input_case = int(input('Please, choose an operand by number:\n1. +\n2. -\n3. *\n4. /'
                           '\nYour choice [1-4]: '))

    value_0 = float(input('\nPlease, type a first number.\n'))
    value_1 = float(input("\nNow, type a second:\n"))

    if input_case == 1:
        print('\nCalculation result is:', value_0 + value_1)
    elif input_case == 2:
        print('\nCalculation result is:', value_0 - value_1)
    elif input_case == 3:
        print('\nCalculation result is:', value_0 * value_1)
    elif input_case == 4:
        print('\nCalculation result is:', value_0 / value_1)
    else:
        print('\nSorry, wrong operand number. Try again.')

except ZeroDivisionError:
    print("\nSorry, but you can't divide by zero.")
except ValueError:
    print('\nOops! It was definitely wrong key. Please, try again.')
