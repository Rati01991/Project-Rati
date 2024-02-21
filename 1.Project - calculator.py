def calculator():
    while True:
        try:
            num1 = float(input('Input your first number: '))
            num2 = float(input('Now input your second number: '))
            action = input("Choose action (+, -, *, or /): ")

            if action == '+':
                print(f'{num1} + {num2} = {num1 + num2}')
            elif action == '-':
                print(f'{num1} - {num2} = {num1 - num2}')
            elif action == '*':
                print(f'{num1} * {num2} = {num1 * num2}')
            elif action == '/':
                if num2 == 0:
                    print('Error - Wrong action number can not be divided by zero!!!')
                else:
                    print(f'{num1} / {num2} = {num1 / num2}')
            else:
                print('Error - Invalid action!!!')
        except ValueError:
            print('Error - Please enter valid numbers!!!')
        except Exception as err:
            print('Error - Something went wrong:', err)

        choice = input('If You wanna continue calculating print "yes"5): ')
        if choice.lower() != 'yes':
            break
        

calculator()