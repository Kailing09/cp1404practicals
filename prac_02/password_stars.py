def main():
    min_length = 10
    password = get_password(min_length)
    print_asterisks(password)

def get_password(min_length):
    is_valid = False
    while not is_valid:
        password = input('Enter your password: ')
        if len(password) >= min_length:
            is_valid = True
        else:
            print('Password must be {} characters long'.format(min_length))
    return password

def print_asterisks(password):
    print('*' * len(password))

main()
