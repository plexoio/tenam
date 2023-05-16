from modules.account import User  # author's


def login_input():
    print(f'For testing purposes use this data:\n\nUsername: Frank\nPassword: 123456\n')
    print('Welcome to Tenam, please login:')
    username = input('Username: ')
    password = input('Password: ')
    login = User(username, password)
    login.user_validation()
    return print('Done!')
