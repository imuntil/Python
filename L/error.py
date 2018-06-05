def zero():
    """除0异常"""
    try:
        print(5/0)
    except ZeroDivisionError:
        print('you can\'t divide by zero')


# zero()


def use_else():
    """use else"""
    print('Give me two numbers, and i\'ll divide them')
    print('enter q to quit')

    while True:
        first_number = input('\nFirst number:')
        if first_number == 'q':
            break
        second_number = input('\nSecond number:')
        try:
            answer = int(first_number) / int(second_number)
        except ZeroDivisionError:
            print('you can\'t divide by 0')
        else:
            print(answer)


# use_else()

