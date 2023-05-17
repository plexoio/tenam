import gspread
from google.oauth2.service_account import Credentials
import os

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Credentials
CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('portfolio')

class Google_Portfolio(object):
    '''
    Main portfolio instance
    '''

    def __init__(self):
        self.user_active = []

    def get_user(self, username, password):
        self.user_active.append(User(username, password))

    def welcome_user(self):
        print(f'Welcome to your dashboard {self.user_active[0]}!')



class User(object):
    '''
    Deal with user login validation
    '''

    def __init__(self, username, password):
        '''
        '''
        self.username = username
        self.password = password

    def user_validation(self):
        '''
        Handles user validation comparing Google Sheet and user input data
        '''
        # Login Variables and Data: Used in 'account.py' module at 'User' class
        user = SHEET.worksheet('user')
        data = user.get_all_values()
        user_titles = data[0]
        title_values = data[1:]

        list_of_dicts = [dict(zip(user_titles, row)) for row in title_values]
    
        for dic in list_of_dicts:
            if dic.get('username') == self.username and dic.get('password') == self.password:
                print('passed username and password')
                os.system('cls' if os.name == 'nt' else 'clear')
                portfolio = Google_Portfolio()
                portfolio.get_user(self.username, self.password)
                portfolio.welcome_user()
            else:
                print(
                    f'{self.username} OR {self.password} did not match with our records')
                return False
        return True
    def __repr__(self):
        return self.username


class Asset(object):
    '''
    For one part of the main object instance
    '''

    def __init__(self, currency, value, sheet_name):
        print()


class Taxation(object):
    '''
    For one part of the main object instance
    '''
    def __init__(self, value, sheet_name):
        print()
