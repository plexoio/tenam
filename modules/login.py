from getpass import getpass
from modules.portfolio import User, Taxation  # author's

def login_input():
    print(f'For testing purposes use this data:\n\nUsername: Tenam\nPassword: test123\n')
    print('Welcome to Tenam, please login:')
    while True:
        username = input('Username: ')
        password = getpass('Password: ')
        tax = input('How much taxes do you pay in percentage?: ')
        login = User(username, password)
        taxation = Taxation(tax)
        if login.user_validation():
            taxation.assigning_tax()
            break