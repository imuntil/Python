def read():
    with open('word.txt', encoding='utf-8', mode='r') as file_object:
        # contents = file_object.read()
        # print(contents)
        # for line in file_object:
        #     print(line.rstrip())

        lines = file_object.readlines()

        pi_string = ''
        for line in lines:
            pi_string += line.strip()

        print(pi_string[:52] + '...')
        print(len(pi_string))

    print(pi_string.replace('，', '-.-'))


def write():
    filename = 'write.txt'
    with open(filename, encoding='utf-8', mode='w') as file_object:
        file_object.write('i love python')
        file_object.write('\ni love animation')


# write()

def add():
    filename = 'write.txt'
    with open(filename, 'a') as file_object:
        file_object.write('\ni also love eating')
        file_object.write('\ni\'m otaku ')


# add()

def user_input():
    filename = 'write.txt'
    name = input('your name:')
    with open(filename, 'a') as file_object:
        file_object.write('\nmy name is {}'.format(name))


# user_input()

def more_input():
    filename = 'write.txt'
    with open(filename, 'a') as file_object:
        file_object.write('\nand we are:')
        while True:
            we = input('we are:')
            if we == 'quit':
                break
            file_object.write('\n-{}'.format(we))


more_input()
