from modules.taxation import Taxation, Get_Taxation
from modules.utilities import bullet_point, BOLD, RESET, slow_type

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
        self.assets_active = []
        self.taxation = Get_Taxation()  # Taxation instance for analysis
        self.taxation_active = []

    def my_data_analysis(self, sheet):
        '''
        Get Data Analysis data from Google Sheet to compose Google_Sheet class
        '''
        # Assembling data from Google Sheets
        current_pairs = self.asset.assets_display(sheet)  # GET Asset's func
        self.assets_active.append(current_pairs)  # STORE Asset's values

        current_taxation = self.taxation.my_tax(sheet)  # GET Taxation's func
        self.taxation_active.append(current_taxation)  # STORE Tax's values

        data_analysis = self.sheet.worksheet('data_analysis')
        my_analysis = data_analysis.get_all_values()
        title_analysis = my_analysis[0]
        analysis_values = my_analysis[1:]

        analysis_dic = [dict(zip(title_analysis, rows))
                        for rows in analysis_values]
        analysis_pairs = []

        my_actual_amount = f' '
        my_old_price = f'{bullet_point} Purchase price: '
        my_new_price = f'{bullet_point} Actual price: '
        my_tax = f'{bullet_point} Taxation: '
        my_pay_tax = f'{bullet_point} Tax: '
        my_profit = f'{bullet_point} Profit: '
        in_future = f'{bullet_point} Foresight profit at 40% (after tax): '

        taxation_data = int(self.taxation_active[0][0])
        push_data = self.sheet.worksheet('data_analysis')

        i = 2  # Move values in Google Sheet

        a = 0
        my_amount = self.assets_active[0]
        nums = []
        for asset in my_amount:
            nums.append(asset)

        for pairs in analysis_dic:
            self.old_price = int(pairs.get('old_price'))
            self.new_price = int(pairs.get('new_price'))

            old_price = self.old_price
            new_price = self.new_price
            tax_pay = int(new_price * taxation_data / 100)
            new_earn = new_price - tax_pay - old_price

            if new_earn < 0: 
                final_lost = f'\n{bullet_point} {BOLD}At LOSS with:{RESET} {new_earn}$'
            elif new_earn > 0:
                final_lost = f'\n{bullet_point} {BOLD}At WIN with:{RESET} {new_earn}$'
            else:
                final_lost = f'\n{bullet_point} {BOLD}Profit neutrality:{RESET} {new_earn}$'

            actual_foresight = int(new_price * 40 / 100 + new_price)
            future_tax = int(actual_foresight * 10 /100)
            basic_profit = actual_foresight - future_tax
            profit_foresight = basic_profit - old_price

            push_data.update(f'D{i}', tax_pay)
            push_data.update(f'E{i}', new_earn)

            i += 1  # Move values in Google Sheet

            result_str = (
                f'\n{BOLD}{my_actual_amount}{nums[a]}{RESET}\n\n'
                f'{my_old_price}{self.old_price}$\n'
                f'{my_new_price}{self.new_price}$\n'
                f'{my_tax}{taxation_data}%\n'
                f'{my_pay_tax}{tax_pay}$\n'
                f'{my_profit}{new_earn}$\n'
                f'{in_future}{profit_foresight}$'
                f'{final_lost}'
            )
            analysis_pairs.append(result_str)
            a += 1
        return analysis_pairs
