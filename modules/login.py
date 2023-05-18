from getpass import getpass
from modules.portfolio import User, Taxation, clear_screen  # author's
import time

def login_input():
    print(f'For testing purposes use this data:\n\nUsername: Tenam\nPassword: test123\n')
    print('Welcome to Tenam, please login:')
    while True:
        username = input('Username: ')
        password = getpass('Password: ')
        login = User(username, password)
        if login.user_validation():
            print('Login successful!')
            time.sleep(2)
            clear_screen()
            break