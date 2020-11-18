import os


def get_pass(login):
    with open('passwords.txt') as file:
        content = file.readlines()
        for pairs in content:
            if pairs.startswith(login):
                ps = pairs.index(':')
                print(pairs[ps + 1:])


def add_data(login, password):
    with open('passwords.txt', 'a') as file:
        file.write('{}:{}'.format(login, password))


if not os.path.exists('passwords.txt'):
    open('passwords.txt', 'w').close()


while True:
    action = input('''1. Add login data
2. Get password
3. Exit\n''')
    if action == '1':
        login = input('Please input login: ')
        password = input('Please input password: ')
        add_data(login, password)
        print('Data has been added')
    elif action == '2':
        login = input('Please input login: ')
        get_pass(login)
    elif action == '3':
        break
