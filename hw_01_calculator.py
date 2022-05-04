key_letter = input('Greetings!\nFor using me press any key.\nFor quit press "q".\n')
if key_letter not in "Q, q":
    while key_letter not in "Q, q":
        try:
            input_case = input('\nPlease, choose an operand by number:\n1. +\n2. -\n3. *\n4. /'
                               '\nYour choice [1-4]: ')
            if input_case in "1234":
                value_0 = float(input('\nPlease, type a first number.\n'))
                value_1 = float(input("\nNow, type a second:\n"))
                result = float()
                if input_case in '1':
                    result = value_0 + value_1
                elif input_case in '2':
                    result = value_0 - value_1
                elif input_case in '3':
                    result = value_0 * value_1
                elif input_case in '4':
                    result = value_0 / value_1
                print('\nCalculation result is:', result)
            elif input_case not in "1234":
                print("\nSorry, but it's a wrong operand. Try again?")
            key_letter = input('\nPress any key for repeat or "q" for quit.\n')
        except ZeroDivisionError:
            print("\nSorry, but you can't divide by zero. Let's try again?")
            key_letter = input('\nPress any key for repeat or "q" for quit.\n')
        except ValueError:
            print('\nOops! It was definitely wrong key. Go try again?')
            key_letter = input('\nPress any key for repeat or "q" for quit.\n')
    print('\nHave a nice day!')
else:
    print('\nHave a nice day!')
