min_length = 10
is_valid = False

while not is_valid:
    password = input('Enter your password: ')

    if len(password) >= min_length:
        is_valid = True
    else:
        print('Password must be {} characters long'.format(min_length))

print('*' * len(password))