from modules.utilities import clear_screen
import time


class Taxation(object):
    '''
    Part of the main object instance (Google_Sheet)
    '''

    def __init__(self, tax, sheet):
        '''
        Initializing instance variables for tax processing
        '''
        self.tax = tax
        self.to_tax = sheet.worksheet('taxation')

    def assigning_tax(self):
        '''
        Upload user inputs to the server for Google_Portfolio composition
        '''
        print('Data uploading to server...')
        self.to_tax.update('A2', self.tax)
        time.sleep(1)
        clear_screen()
        print('Data uploaded to server successfully!')
        time.sleep(2)
        clear_screen()


class Get_Taxation(object):
    '''
    Part of the main object instance (Google_Sheet)
    '''

    def my_tax(self, sheet):
        '''
        Fetch Taxation data from Google Sheet to compose Google_Sheet class
        '''
        # Google Sheets
        self.sheet = sheet
        my_tax = self.sheet.worksheet('taxation')
        display_tax = my_tax.get_all_values()
        title_taxation = display_tax[0]
        taxation_values = display_tax[1]
        return taxation_values
