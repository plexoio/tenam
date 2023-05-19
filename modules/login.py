from getpass import getpass
from modules.portfolio import User, Taxation, clear_screen  # author's
import time

def login_input():
    print('Welcome to Tenam, please login:\n')
    print(f'For testing purposes use this data:\nUsername: Tenam\nPassword: test123\n')
    while True:
        username = input('Username: ')
        password = getpass('Password: ')
        login = User(username, password)
        if login.user_validation():
            clear_screen()
            print('Loading enviroment for you, almost there!')
            time.sleep(2)
            clear_screen()
            print('Login successful!')
            break