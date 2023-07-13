result = None
operand = None
operator = None
wait_for_number = True

while True:
    inp = input('Input number: ') if wait_for_number else input('Input operator: ')
    if wait_for_number:
        try:
            operand = float(inp)
        except ValueError:
            print(f'{inp!r} is not a number. Try again.')
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
        if inp == '=':
            print(result)
            break
        elif inp in ['+', '-', '/', '*']:
            operator = inp
        else:
            print(f"{inp!r} is not '+' or '-' or '/' or '*'. Try again")
            continue
    wait_for_number = not wait_for_number
