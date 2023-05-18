import gspread
from google.oauth2.service_account import Credentials
import os  # for clearing screen depending on OS

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Google Sheets Credentials
CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('portfolio')


def clear_screen():
    '''
    Used all around to clear console when needed to avoid overcrowding
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


class Google_Portfolio(object):
    '''
    Main portfolio as object instance, receiving composition
    '''

    def __init__(self):
        '''
        Allow instance variables
        '''
        # Local Variables
        self.user_active = []  # For Welcome message

        self.asset = Asset()  # Asset instance for Menu
        self.assets_active = []

        self.transaction = Transaction()  # Transaction instance for Menu
        self.transactions_active = []

    def get_user(self, username, password):
        '''
        Append 'Username' & 'Password' to the upper instance variable
        '''
        self.user_active.append(User(username, password))

    def welcome_user(self):
        '''
        Welcome user before opening Menu (appears above it)
        '''
        print(f'Welcome to your dashboard {self.user_active[0]}!\n')

    def menu(self):
        '''
        Represents the instance of the whole app navigation
        '''
        menu_list = 'Menu:\n\n1.Assets\n2.Transaction\n3.Data Analysis\n4.Taxation\n5.RSS News\n6.Return\n'

        # Local Variables
        current_pairs = self.asset.assets_display()  # Get Asset class function
        margin_menu = f'----------------------------\n'

        # Store Asset's values values for menu
        self.assets_active.append(current_pairs)

        # Get Transaction class function
        current_transactions = self.transaction.my_transactions()

        # Store Transaction's values for menu
        self.transactions_active.append(current_transactions)

        while True:

            print(menu_list)
            menu_input = input('Type index number: ')

            if menu_input == '1':
                clear_screen()
                pairs = self.assets_active[0]
                print('Your current assets: \n')
                for asset in pairs:
                    print(f'{asset}\n')
                print('RSS news: GOES HERE! \n')

            elif menu_input == '2':
                clear_screen()
                t_paris = self.transactions_active[0]
                print('Your last 6 transactions: \n')
                for transaction in t_paris:
                    print(f'{transaction}')
                print(f'{margin_menu}RSS news: GOES HERE! \n')

            elif menu_input == 'Return':
                clear_screen()
                self.menu()  # Recursion here

            else:
                clear_screen()
                print('Value not supported try again!')


class User(object):
    '''
    Deal with user login validation
    '''

    def __init__(self, username, password):
        '''
        Defining instance variables to use for login validation
        '''
        self.username = username
        self.password = password

    def user_validation(self):
        '''
        Handles user validation comparing Google Sheet and user input data
        '''
        # Google Sheets
        user = SHEET.worksheet('user')
        data = user.get_all_values()
        user_titles = data[0]
        title_values = data[1:]

        # Internal Sorting
        list_of_dicts = [dict(zip(user_titles, row)) for row in title_values]

        # Data processing
        for dic in list_of_dicts:
            if dic.get('username') == self.username and dic.get('password') == self.password:
                print('passed username and password')
                clear_screen()
                portfolio = Google_Portfolio()
                portfolio.get_user(self.username, self.password)
                portfolio.welcome_user()
            else:
                print(
                    f'{self.username} OR {self.password} did not match with our records')
                return False
        return True

    def __repr__(self):
        '''
        Using this single variable for Object representation used for composition on the Google_Sheet class
        '''
        return self.username


class Asset(object):
    '''
    Part of the main object instance (Google_Sheet)
    '''

    def assets_display(self):
        '''
        Fetch assets data from Google Sheet to compose Google_Sheet class
        '''
        # Google Sheets
        asset = SHEET.worksheet('asset')
        my_assets = asset.get_all_values()
        title_assets = my_assets[0]
        title_values = my_assets[1:]

        # Internal Sorting
        assets_dic = [dict(zip(title_assets, rows))for rows in title_values]
        current_pairs = []

        # Data processing
        for asset_dic in assets_dic:
            self.currency = asset_dic.get('currency')
            self.amount = asset_dic.get('amount')
            current_pairs.append(f'{self.currency}: {self.amount}')
        return current_pairs


class Transaction(object):
    '''
    Part of the main object instance (Google_Sheet)
    '''

    def my_transactions(self):
        '''
        Fetch transactions data from Google Sheet to compose Google_Sheet class
        '''
        # Google Sheets
        transaction = SHEET.worksheet('transaction')
        my_transaction = transaction.get_all_values()
        title_transactions = my_transaction[0]
        transaction_values = my_transaction[1:]

        # Internal Sorting
        transactions_dic = [dict(zip(title_transactions, rows))
                            for rows in transaction_values]
        transaction_pairs = []

        # Data processing
        margin_transaction = f'----------------------------\n'
        for pairs in transactions_dic:
            self.currency = pairs.get('currency')
            self.txid = pairs.get('txid')
            self.status = pairs.get('status')
            self.amount = pairs.get('amount')
            transaction_pairs.append(
                f'{margin_transaction}{self.currency}: {self.amount}\n\n Status: {self.status}\n\nTxID: {self.txid}')
        return transaction_pairs


class Taxation(object):
    '''
    Part of the main object instance (Google_Sheet)
    '''

    def __init__(self, value, sheet_name):
        print()
