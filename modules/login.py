from modules.portfolio import Google_Portfolio, User  # author's
import os

def login_input():
    print(f'For testing purposes use this data:\n\nUsername: Frank\nPassword: 123456\n')
    print('Welcome to Tenam, please login:')
    username = input('Username: ')
    password = input('Password: ')
    login = User(username, password)
    if login.user_validation():
        os.system('cls' if os.name == 'nt' else 'clear')