import gspread
from google.oauth2.service_account import Credentials
import os  # for clearing screen depending on OS
import feedparser # importing module after 'pip install feedparser' library
import textwrap # wrapper library to make sure text don't exceed 80 chrs

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

    def my_rss_news(self, url):
        feed = feedparser.parse(url)
        top = feed.entries[:2]

        for news in top:
            print('RSS News:\n\n')
            print(f'TITLE: {news.title}\n')
            text_lines = textwrap.wrap(news.summary[:200], width=70)
            full_text = '\n'.join(text_lines) # get rid of brackets and add space in between
            print(f'SUMMARY: {full_text}\n')
            print('LINK: ', news.link)
            print('-------------------------\n')

    def menu(self):
        '''
        Represents the instance of the whole app navigation
        '''
        menu_list = '\nMenu section:\n\n1. Assets\n2. Transaction\n3. Data Analysis\n4. Taxation\n5. Update Tax Value\n6. RSS News\n7. Refresh\n'

        # Assembling variables for Menu

        # RSS

        url = 'https://www.coindesk.com/arc/outboundfeeds/rss/?outputType=xml'

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
            menu_input = input('Where do you want to go?: ')
            clear_screen()

            if menu_input == '1':  # Asset
                pairs = self.assets_active[0]
                print('Your current assets: \n')
                for asset in pairs:
                    print(f'{asset}\n')
                print('RSS news: GOES HERE! \n')

            elif menu_input == '2':  # Transaction
                t_paris = self.transactions_active[0]
                print('Your last 6 transactions: \n')
                for transaction in t_paris:
                    print(f'{transaction}')
                print(f'{margin}RSS news: GOES HERE! \n')

            elif menu_input == '3':  # Data Analysis
                data_pairs = self.data_analysis_active[0]
                print(f"Overview:\n\n- In this section, you'll have the ability to view your current asset portfolio.\n\n- The amount, prices, and associated taxes of each asset will be provided\nto help you analyze your potential profits and ascertain your tax obligations:\n")
                for my_data in data_pairs:
                    print(f'{my_data}')
                print(f'{margin}RSS news: GOES HERE! \n')

            elif menu_input == '4':  # Actual Tax Taxation
                taxation_data = int(self.taxation_active[0][0])
                print(f'In this section you can visualize the mount of taxes you have input\nwhen initiating the application, and the subsequent calculations\nwill be based on that input:\n')
                print(f'Your tax responsability value is: {taxation_data}%\n')

            elif menu_input == '5':
                input_tax = input(
                    '\nHow much taxes do you pay in percentage?: ')
                try:
                    tax = int(input_tax)
                    if tax >= 0:
                        taxation = Taxation(tax)
                        taxation.assigning_tax()
                        print(
                            '\nPlease, restart application to load the new tax calculations!')
                    else:
                        print('Only positve numbers!')
                except ValueError:
                    print(f'\n"{input_tax}" is not a number, please try again!')

            elif menu_input == '6':
                self.my_rss_news(url)

            elif menu_input == '7':
                clear_screen()

            else:
                clear_screen()
                print('Value not supported just yet, try again!\n')


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
                    f'\nThe Username: "{self.username}" OR Password: "{self.password}" did not match with our records.\nPlease, try again!\n')
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
        self.asset = Asset()  # Asset instance for Menu
        self.assets_active = []
        self.taxation = Get_Taxation()  # Taxation instance for analysis
        self.taxation_active = []

    def my_data_analysis(self):
        '''
        Fetch Data Analysis data from Google Sheet to compose Google_Sheet class
        '''
        # Assembling data from Google Sheets

        # GET Asset's class function
        current_pairs = self.asset.assets_display()

        # STORE Asset's values for menu
        self.assets_active.append(current_pairs)

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

        # Local variables
        my_actual_amount = '- '
        my_old_price = '- Purchase price: '
        my_new_price = '- Actual price: '
        my_tax = '- Taxation: '
        my_pay_tax = '- Calculated tax: '
        my_profit = '- Calculated profit: '

        # Data Analysis Variables
        taxation_data = int(self.taxation_active[0][0])
        push_data = SHEET.worksheet('data_analysis')

        i = 2  # Move values in Google Sheet

        # Sort Amounts from Asset's class
        a = 0
        my_amount = self.assets_active[0]
        nums = []
        for asset in my_amount:
            nums.append(asset)

        # Data processing
        for pairs in analysis_dic:
            self.old_price = int(pairs.get('old_price'))
            self.new_price = int(pairs.get('new_price'))
            self.profit = pairs.get('profit')

            # Do calculations

            old_price = self.old_price
            new_price = self.new_price
            tax_pay = new_price * taxation_data / 100
            new_earn = new_price - tax_pay - old_price

            push_data.update(f'D{i}', tax_pay)
            push_data.update(f'E{i}', new_earn)
            i += 1  # Move values in Google Sheet

            analysis_pairs.append(
                f'{margin}{my_actual_amount}{nums[a]}\n{my_old_price}{self.old_price}$\n{my_new_price}{self.new_price}$\n{my_tax}{taxation_data}%\n{my_pay_tax}{tax_pay}\n{my_profit}{new_earn}')
            a += 1
        return analysis_pairs


class Taxation(object):
    '''
    Part of the main object instance (Google_Sheet)
    '''

    def __init__(self, tax):
        self.tax = tax
        self.to_tax = SHEET.worksheet('taxation')

    def assigning_tax(self):
        print('Data uploading to server...')
        self.to_tax.update('A2', self.tax)
        print('Data uploaded to server successfully!')
        clear_screen()


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
