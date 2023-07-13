result = None
operand = None
operator = None
wait_for_number = True

while True:
    user_input = input('Input number: ') if wait_for_number else input('Input operator: ')
    if wait_for_number:
        try:
            operand = float(user_input)
        except ValueError:
            print(f'{user_input!r} is not a number. Try again.')
            continue
        if result is None:
            result = operand
        match operator:
            case '/' if operand == 0:
                print('Number is divided by 0. Try again.')
                continue
            case '/':
                result /= operand
            case '+':
                result += operand
            case '-':
                result -= operand
            case '*':
                result *= operand
    else:
        if user_input == '=':
            print(result)
            break
        elif user_input == '+' or user_input == '-' or user_input == '/' or user_input == '*':
            operator = user_input
        else:
            print(f"{user_input!r} is not '+' or '-' or '/' or '*'. Try again")
            continue
    wait_for_number = not wait_for_number
