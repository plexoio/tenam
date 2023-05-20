# all necessary imports
import time
from getpass import getpass
import textwrap
import feedparser
from google.oauth2.service_account import Credentials
import gspread
from modules.utilities import bullet_point, BOLD, RESET, clear_screen, slow_type
from modules.taxation import Taxation, Get_Taxation
from modules.data_analysis import Data_Analysis
from modules.transaction import Transaction
from modules.asset import Asset
from modules.welcome import welcome_users

separator = f'\n-------------------{BOLD}NEW SECTION{RESET}-------------------\n'

# Google Sheets related constants and credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('portfolio')


class Google_Portfolio(object):
    '''
    Main portfolio as object instance, receiving composition
    '''

    def __init__(self):
        '''
        Allow instance variables for composition
        '''
        self.sheet = SHEET
        # Local Variables

        # Asset instance for Menu
        self.asset = Asset()
        self.assets_active = []

        # Transaction instance for Menu
        self.transaction = Transaction(self.sheet)
        self.transactions_active = []

        # Data Analysis instance for Menu
        self.data_analysis = Data_Analysis(self.asset, self.sheet)
        self.data_analysis_active = []

        # Taxation instance for Menu
        self.taxation = Get_Taxation()
        self.taxation_active = []

    def my_rss_news(self, url):
        '''
        Deal with the fetching and processing of RSS data
        '''
        # RSS local variables
        feed = feedparser.parse(url)
        top = feed.entries[:2]
        x = 0

        for news in top:
            x += 1
            print(f'\n{BOLD}RSS News {x}{RESET}\n')

            # Title
            title_lines = textwrap.wrap(news.title, width=70)
            full_title = '\n'.join(title_lines)
            print(f'{bullet_point} {full_title}:\n')

            # Summary
            text_lines = textwrap.wrap(news.summary[:200], width=70)
            # get rid of brackets and add space in between
            full_text = '\n'.join(text_lines)
            print(f'{full_text}...\n')

            # Link
            print(f'{bullet_point}', news.link)

    def menu(self, sheet):
        '''
        Represents the instance of the whole app navigation
        '''
        # Assembling variables for Menu

        # RSS
        url = ('https://www.coindesk.com/arc/outboundfeeds/rss/'
               '?outputType=xml')

        menu_list = (
            '\nMenu section:\n\n1. Assets\n2. Transaction\n3. Data Analysis'
            '\n4. Taxation\n5. Update Tax Value\n6. RSS News\n7. Refresh\n'
            '8. Exit\n')

        # GET Asset's class function
        # Get Asset class function
        current_pairs = self.asset.assets_display(SHEET)
        self.assets_active.append(current_pairs)

        # GET Transaction class function
        current_transactions = self.transaction.my_transactions()
        self.transactions_active.append(current_transactions)

        # GET Data_Analysis's class function
        curr_data_analysis = self.data_analysis.my_data_analysis(sheet)
        self.data_analysis_active.append(curr_data_analysis)

        # GET Taxation's class function
        current_taxation = self.taxation.my_tax(SHEET)
        self.taxation_active.append(current_taxation)

        # MENU starts
        while True:
            try:
                print(menu_list)
                menu_input = input('Where do you want to go?:\n')
                clear_screen()

                if menu_input == '1':  # Asset
                    pairs = self.assets_active[0]
                    print(separator)
                    print('Here you can visualize all your current crypto holdings\n')
                    for asset in pairs:
                        print(f'{bullet_point} {asset}')

                elif menu_input == '2':  # Transaction
                    t_paris = self.transactions_active[0]
                    print(separator)
                    print('Last 6 transactions available in this section')
                    a = 0
                    for transaction in t_paris:
                        a += 1
                        print(f'\n{bullet_point} {BOLD}BLOCKCHAIN BLOCK {a}{RESET}\n')
                        print(f'{transaction}')

                elif menu_input == '3':  # Data Analysis
                    data_pairs = self.data_analysis_active[0]
                    print(separator)
                    print("Based on your assets, old price, new price and tax value "
                    "we have analized your data \n"
                    "for insightful retrospection and foresight regarding your holdings."
                    )
                    for my_data in data_pairs:
                        print(f'{my_data}')

                elif menu_input == '4':  # Actual Tax Taxation
                    taxation_data = int(self.taxation_active[0][0])
                    print(separator)
                    print("Default tax value or the one you input\n"
                        "when updating your taxation.")
                    print(f'{bullet_point} Your tax responsability value is: {taxation_data}%')

                elif menu_input == '5': # Update taxation
                    try:
                        input_tax = input('\nInput your tax duty in percentage:\n')
                        tax = int(input_tax)
                        if tax >= 0:
                            taxation = Taxation(tax, sheet)
                            taxation.assigning_tax()
                            print('\nPlease, restart application to load '
                                'the new tax calculations!')
                        else:
                            print('Only positve numbers!')
                    except ValueError:
                        slow_type(f'\n"{input_tax}" input not correct, please try again!')
                    except KeyboardInterrupt:
                        slow_type(" Key not accepted, please try again!")
                        time.sleep(2)
                        clear_screen()

                elif menu_input == '6': # Get RSS News
                    print(separator)
                    self.my_rss_news(url)

                elif menu_input == '7': # Refresh screen
                    clear_screen()

                elif menu_input == "8": # Exit app
                    slow_type('You have been disconnected!')
                    return
                else:
                    clear_screen()
                    slow_type('Value not supported just yet, try again!\n')
            except KeyboardInterrupt:
                slow_type(" Key not accepted, please try again!")
                time.sleep(2)
                clear_screen()


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
            if (dic.get('username') == self.username and
                    dic.get('password') == self.password):
                pass
            else:
                slow_type('The Username: "{}" OR Password: "{}" did not match '
                      'with our records.\n'
                      .format(self.username, self.password))
                return False
        return True


def login_input():
    '''
    Particular function to deal with login and validation
    '''
    print(f'Welcome to the login section, '
            f'for testing purposes use this data:\n\n'
            f'{bullet_point} Tenam\n{bullet_point} test123'
        )

    while True:
        try:
            username = input('\nUsername:\n')
            password = getpass('\nPassword:\n')
            login = User(username, password)

            if login.user_validation():
                clear_screen()
                print('Loading enviroment for you...')
                time.sleep(2)
                clear_screen()
                print('State: Login successful!')
                break
        except KeyboardInterrupt:
            slow_type(" Key not accepted, please try again!")
            time.sleep(2)


welcome_users(login_input)
menu = Google_Portfolio()  # After login successfully launch Menu
menu.menu(SHEET)
