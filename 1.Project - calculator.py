def calculator():
    while True:
        num1 = num2 = ' '
        while type(num1) not in (int, float):
            try:
                num1 = eval(input('Input your first number: '))
            except (NameError, SyntaxError):
                print("Please, enter a valid number\n")

        while type(num2) not in (int, float):
            try:
                num2 = eval(input('Input your second number: '))
            except (NameError, SyntaxError):
                print("Please, enter a valid number\n")


        while True:
            action = input("Choose action (+, -, *, or /): ")

            if action == '+':
                print(f'{num1} + {num2} = {num1 + num2}')
                break
            elif action == '-':
                print(f'{num1} - {num2} = {num1 - num2}')
                break
            elif action == '*':
                print(f'{num1} * {num2} = {num1 * num2}')
                break
            elif action == '/':
                if num2 == 0:
                    print('Error - Wrong action number can not be divided by zero!!!')
                else:
                    print(f'{num1} / {num2} = {num1 / num2}')
                    break
            else:
                print('Error - Invalid action!!!\n')

        choice = input('\nIf You wanna continue calculating print "yes"): ')
        print()
            
        if choice.lower() != 'yes':
            break
        

calculator()