class User(object):
    '''
    For one part of the main object instance
    '''

    def __init__(self, username, password):
        '''
        '''
        self.username = username
        self.password = password

    def user_login(self):
        '''
        '''
        print(f'{self.username} start login now with {self.password}')

    def user_validation(self):
        '''
        '''
        print('Validation Starts')


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