from modules.google_sheets import *  # third-part


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
        '''
        list_of_dicts = [dict(zip(user_titles, row)) for row in title_values]
        for dic in list_of_dicts:
            for key, value in dic.items():
                if value == self.username:
                    print('passed username')
                elif value == self.password:
                    print('passed password')
                else:
                    print('did not match')
        print(
            f'You have logged in with the following data:\n{self.username}\n{self.password}')


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
