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


# Global variables
margin = f'----------------------------\n'


class Google_Portfolio(object):
    '''
    Main portfolio as object instance, receiving composition
    '''

    def __init__(self):
        '''
        Allow instance variables for composition
        '''
        # Local Variables
        self.user_active = []  # For Welcome message

        self.asset = Asset()  # Asset instance for Menu
        self.assets_active = []

        self.transaction = Transaction()  # Transaction instance for Menu
        self.transactions_active = []

        self.data_analysis = Data_Analysis()
        self.data_analysis_active= []

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

        # Assembling variables for Menu

        # GET Asset's class function
        current_pairs = self.asset.assets_display()  # Get Asset class function

        # STORE Asset's values values for menu
        self.assets_active.append(current_pairs)

        # GET Transaction class function
        current_transactions = self.transaction.my_transactions()

        # STORE Transaction's values for menu
        self.transactions_active.append(current_transactions)

        # GET Data_Analysis's class function
        current_data_analysis = self.data_analysis.my_data_analysis()

        # STORE Data_Analysis's values for menu
        self.data_analysis_active.append(current_data_analysis)

        # MENU starts
        while True:

            print(menu_list)
            menu_input = input('Type index number: ')

            if menu_input == '1': # Asset
                clear_screen()
                pairs = self.assets_active[0]
                print('Your current assets: \n')
                for asset in pairs:
                    print(f'{asset}\n')
                print('RSS news: GOES HERE! \n')

            elif menu_input == '2': # Transaction
                clear_screen()
                t_paris = self.transactions_active[0]
                print('Your last 6 transactions: \n')
                for transaction in t_paris:
                    print(f'{transaction}')
                print(f'{margin}RSS news: GOES HERE! \n')
            
            elif menu_input == '3': # Data Analysis
                clear_screen()
                data_pairs = self.data_analysis_active[0]
                print(f"In this section, you'll have the ability to view your current asset portfolio.\nThe amount, prices, and associated taxes of each asset will be provided\nto help you analyze your potential profits and ascertain your tax obligations:\n")
                for my_data in data_pairs:
                    print(f'{my_data}')
                print(f'{margin}RSS news: GOES HERE! \n')

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
        for pairs in transactions_dic:
            self.currency = pairs.get('currency')
            self.txid = pairs.get('txid')
            self.status = pairs.get('status')
            self.amount = pairs.get('amount')
            transaction_pairs.append(
                f'{margin}{self.currency}: {self.amount}\n\n Status: {self.status}\n\nTxID: {self.txid}')
        return transaction_pairs


class Data_Analysis(object):
    '''
    Part of the main object instance (Google_Sheet)
    '''

    def my_data_analysis(self):
        '''
        Fetch Data Analysis data from Google Sheet to compose Google_Sheet class
        '''
        # Google Sheets
        data_analysis = SHEET.worksheet('data_analysis')
        my_analysis = data_analysis.get_all_values()
        title_analysis = my_analysis[0]
        analysis_values = my_analysis[1:]

        # Internal Sorting

        analysis_dic = [dict(zip(title_analysis, rows))
                        for rows in analysis_values]
        analysis_pairs = []

        # local variables
        my_currencies = '- Currency: '
        my_old_price = '- Purchase Price: '
        my_new_price = '- Actual Price: '
        my_tax = '- Tax Responsibility: '
        my_pay_tax = '- Tax to pay: '
        my_profit = '- Calculated profit: '

        # Data Analysis Variables

        purchase_price = []
        actual_price = []
        #tax = []
        tax_pay =[]

        # Data processing
        for pairs in analysis_dic:
            self.currency = pairs.get('currency')
            self.old_price = pairs.get('old_price')
            self.new_price = pairs.get('new_price')
            # self.tax = pairs.get('tax')
            self.pay_tax = pairs.get('pay_tax')
            self.profit = pairs.get('profit')
            purchase_price.append(self.old_price)
            actual_price.append(self.new_price)
            #tax.append(self.tax)
            tax_pay.append(self.pay_tax)
            analysis_pairs.append(
                f'{margin}{my_currencies}{self.currency}\n{my_old_price}{self.old_price}$\n{my_new_price}{self.new_price}$\n{my_tax}{self.pay_tax}\n{my_profit}{self.profit}')
        
        # Data Analysis Calculations
        pp = [int(p) for p in purchase_price]
        ap = [int(a) for a in actual_price]
        print(pp)
        print(ap)
        #print(t)
        #print(tp)
        return analysis_pairs


class Taxation(object):
    '''
    Part of the main object instance (Google_Sheet)
    '''
    def __init__(self, tax):
        self.tax = tax

    def assigning_tax(self):
        to_tax = SHEET.worksheet('taxation')
        to_tax.update('A2', [[self.tax]])
        print('worked!')
