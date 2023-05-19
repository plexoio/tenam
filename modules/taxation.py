from modules.clear_screen import clear_screen

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
