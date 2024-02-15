def task1(str):
    return len(str)


def task2(number1, operation, number2):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '/':
        return number1 / number2
    elif operation == '//':
        return number1 // number2
    elif operation == '**':
        return number1 ** number2
    elif operation == '*':
        return number1 * number2
    else:
        return "Невідома операція"

def task3(input_list):
        return max(input_list)
