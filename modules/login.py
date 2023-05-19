from getpass import getpass # Built-in module for hiding password
import time # built-in module for adding time.sleep() function to allow users read feedback
from run import User
def login_input():
    '''
    Particular function to deal with login and validation
    '''
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