import gspread # google's library for Google Spread Sheet
from google.oauth2.service_account import Credentials # Importing from google's module
import os  # Built-in module for clearing screen depending on OS
import feedparser  # Importing module after 'pip install feedparser' library
import textwrap  # Wrapper library to make sure text don't exceed 80 chrs








class Taxation(object):
    '''
    Part of the main object instance (Google_Sheet)
    '''

    def __init__(self, tax):
        '''
        Initializing instance variables for tax processing
        '''
        self.tax = tax
        self.to_tax = SHEET.worksheet('taxation')

    def assigning_tax(self):
        '''
        Instance to upload to server what user inputs as seen on the Google_Portfolio composition
        '''
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
