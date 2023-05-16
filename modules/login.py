from modules.account import User # author's

def login_input():
    print('Username: Frank, Password: 123456')
    username = input('Username: ')
    password = input('Password: ')
    login = User(username, password)
    login.user_login()
    login.user_validation()
    return print('Done!')