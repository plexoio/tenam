from modules.taxation import Taxation, Get_Taxation

class Data_Analysis(object):
    '''
    Part of the main object instance (Google_Sheet)
    '''

    def __init__(self, asset, sheet):
        '''
        Initializing instance variables a bit of composing as well
        '''
        self.sheet = sheet
        self.asset = asset
        # Local Variables
        self.assets_active = []
        self.taxation = Get_Taxation()  # Taxation instance for analysis
        self.taxation_active = []

    def my_data_analysis(self, sheet, margin):
        '''
        Fetch Data Analysis data from Google Sheet to compose Google_Sheet class
        '''
        # Assembling data from Google Sheets

        # GET Asset's class function
        current_pairs = self.asset.assets_display(sheet)

        # STORE Asset's values for menu
        self.assets_active.append(current_pairs)

        # GET Taxation's class function
        current_taxation = self.taxation.my_tax(sheet)

        # STORE Taxation's values for menu
        self.taxation_active.append(current_taxation)

        # Google Sheets
        data_analysis = self.sheet.worksheet('data_analysis')
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
        push_data = self.sheet.worksheet('data_analysis')

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
