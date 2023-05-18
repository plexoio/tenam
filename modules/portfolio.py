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

        self.asset = Asset()  # Asset instance for Menu
        self.assets_active = []

        self.transaction = Transaction()  # Transaction instance for Menu
        self.transactions_active = []

        self.data_analysis = Data_Analysis()  # Data Analysis instance for Menu
        self.data_analysis_active = []

        self.taxation = Get_Taxation()  # Taxation instance for Menu
        self.taxation_active = []

    def menu(self):
        '''
        Represents the instance of the whole app navigation
        '''
        menu_list = 'Menu:\n\n1.Assets\n2.Transaction\n3.Data Analysis\n4.Taxation\n5.Update Tax Value\n6.RSS News\n7.Return\n'

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

        # GET Taxation's class function
        current_taxation = self.taxation.my_tax()

        # STORE Taxation's values for menu
        self.taxation_active.append(current_taxation)
        # MENU starts
        while True:

            print(menu_list)
            menu_input = input('Type index number: ')

            if menu_input == '1':  # Asset
                clear_screen()
                pairs = self.assets_active[0]
                print('Your current assets: \n')
                for asset in pairs:
                    print(f'{asset}\n')
                print('RSS news: GOES HERE! \n')

            elif menu_input == '2':  # Transaction
                clear_screen()
                t_paris = self.transactions_active[0]
                print('Your last 6 transactions: \n')
                for transaction in t_paris:
                    print(f'{transaction}')
                print(f'{margin}RSS news: GOES HERE! \n')

            elif menu_input == '3':  # Data Analysis
                clear_screen()
                data_pairs = self.data_analysis_active[0]
                print(f"In this section, you'll have the ability to view your current asset portfolio.\nThe amount, prices, and associated taxes of each asset will be provided\nto help you analyze your potential profits and ascertain your tax obligations:\n")
                for my_data in data_pairs:
                    print(f'{my_data}')
                print(f'{margin}RSS news: GOES HERE! \n')

            elif menu_input == '4':  # Actual Tax Taxation
                clear_screen()
                taxation_data = int(self.taxation_active[0][0])
                print(f'In this section you can visualize the mount of taxes you have input\nwhen initiating the application, and the subsequent calculations\nwill be based on that input:\n')
                print(f'Your tax responsability value is: {taxation_data}%\n')
            
            elif menu_input == '5':
                tax = int(input('How much taxes do you pay in percentage?: '))
                if tax >= 0:
                    taxation = Taxation(tax)
                    taxation.assigning_tax()
                    print('\nPlease, restart application to load results!\n')
            elif menu_input == '7':
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
                pass
            else:
                print(
                    f'{self.username} OR {self.password} did not match with our records')
                return False
        return True


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

    def __init__(self):
        # Local Variables
        self.taxation = Get_Taxation()  # Taxation instance for analysis
        self.taxation_active = []

    def my_data_analysis(self):
        '''
        Fetch Data Analysis data from Google Sheet to compose Google_Sheet class
        '''
        # Assembling data from Google Sheets

        # GET Taxation's class function
        current_taxation = self.taxation.my_tax()

        # STORE Taxation's values for menu
        self.taxation_active.append(current_taxation)

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

        # purchase_price = []
        # actual_price = []
        # tax_pay = []
        taxation_data = int(self.taxation_active[0][0])
        push_data = SHEET.worksheet('data_analysis')
        i = 2
        # Data processing
        for pairs in analysis_dic:
            self.currency = pairs.get('currency')
            self.old_price = int(pairs.get('old_price'))
            self.new_price = int(pairs.get('new_price'))
            self.profit = pairs.get('profit')
            
            old_price = self.old_price
            new_price = self.new_price
            tax_pay = new_price * taxation_data / 100
            new_earn = new_price - tax_pay - old_price

            push_data.update(f'D{i}', tax_pay)
            push_data.update(f'E{i}', new_earn)
            i += 1
            analysis_pairs.append(
                f'{margin}{my_currencies}{self.currency}\n{my_old_price}{self.old_price}$\n{my_new_price}{self.new_price}$\n{my_tax}: {taxation_data}%\n{my_pay_tax}: {tax_pay}')
        return analysis_pairs


class Taxation(object):
    '''
    Part of the main object instance (Google_Sheet)
    '''

    def __init__(self, tax):
        self.tax = tax
        self.to_tax = SHEET.worksheet('taxation')

    def assigning_tax(self):
        clear_screen()
        print('Data uploading to server...')
        self.to_tax.update('A2', self.tax)
        print('Data uploaded to server successfully!')


class Get_Taxation(object):
    '''
    Part of the main object instance (Google_Sheet)
    '''

    def my_tax(self):
        '''
        Fetch Taxation data from Google Sheet to compose Google_Sheet class
        '''
        # Google Sheets
        my_tax = SHEET.worksheet('taxation')
        display_tax = my_tax.get_all_values()
        title_taxation = display_tax[0]
        taxation_values = display_tax[1]
        return taxation_values
