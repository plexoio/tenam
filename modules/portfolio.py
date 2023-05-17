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
    Main portfolio instances
    '''

    def __init__(self):
        '''
        Allow instance variables
        '''
        self.user_active = []  # For Welcoming
        self.assets_active = []  # for Menu

    def get_user(self, username, password):
        '''
        Append 'Username' & 'Password' to the upper instance variable
        '''
        self.user_active.append(User(username, password))

    def welcome_user(self):
        '''
        Welcome user before opening Menu (appears above it)
        '''
        print(f'Welcome to your dashboard {self.user_active[0]}!')

    def menu(self):
        '''
        Represents the instance of the whole app navigation
        '''
        print('Menu:\n1.Assets\n2.Transaction\n3.Taxation\n4.Data Analysis')

        # Menu Variables
        asset = Asset()  # Calling Asset class
        current_pairs = asset.assets_display()  # Getting class function
        self.assets_active.append(current_pairs)  # Storing the values we need

        # InputF
        menu_input = int(input('Type index number: '))

        # Conditions of the Input
        if menu_input == 1:
            pairs = self.assets_active[0]
            for asset in pairs:
                print(asset)
        else:
            print('Did not print anything!')


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

    def assets_display(self):
        asset = SHEET.worksheet('asset')
        my_assets = asset.get_all_values()
        title_assets = my_assets[0]
        title_values = my_assets[1:]

        assets_dic = [dict(zip(title_assets, rows))for rows in title_values]
        current_pairs = []
        for asset_dic in assets_dic:
            self.currency = asset_dic.get('currency')
            self.amount = asset_dic.get('amount')
            current_pairs.append(f'{self.currency}: {self.amount}')
        return current_pairs


class Taxation(object):
    '''
    For one part of the main object instance
    '''

    def __init__(self, value, sheet_name):
        print()
