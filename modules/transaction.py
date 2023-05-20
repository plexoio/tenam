class Transaction(object):
    '''
    Part of the main object instance (Google_Sheet)
    '''

    def __init__(self, sheet):
        self.sheet = sheet

    def my_transactions(self):
        '''
        Fetch transactions data from Google Sheet to compose Google_Sheet class
        '''
        # Google Sheets
        transaction = self.sheet.worksheet('transaction')
        my_transaction = transaction.get_all_values()
        title_transactions = my_transaction[0]
        transaction_values = my_transaction[1:]

        # Internal Sorting
        transactions_dic = [
            dict(zip(title_transactions, rows))
            for rows in transaction_values
        ]
        transaction_pairs = []

        # Data processing
        for pairs in transactions_dic:
            self.currency = pairs.get('currency')
            self.txid = pairs.get('txid')
            self.status = pairs.get('status')
            self.amount = pairs.get('amount')
            transaction_pairs.append(
                f'{self.currency}: {self.amount}\n\n'
                f'Status: {self.status}\n\nTxID: {self.txid}'
            )
        return transaction_pairs
