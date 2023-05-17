from modules.portfolio import Google_Portfolio, User, Asset  # author's

def login_input():
    print(f'For testing purposes use this data:\n\nUsername: Frank\nPassword: 123456\n')
    print('Welcome to Tenam, please login:')
    while True:
        username = input('Username: ')
        password = input('Password: ')
        login = User(username, password)
        if login.user_validation():
            break