class Asset(object):
    '''
    Part of the main object instance (Google_Sheet)
    '''

    def assets_display(self, sheet):
        '''
        Fetch assets data from Google Sheet to compose Google_Sheet class
        '''
        # Google Sheets
        asset = sheet.worksheet('asset')
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