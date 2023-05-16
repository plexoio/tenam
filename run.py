# Write your code to expect a terminal of 80 characters wide and 24 rows high
from google_sheets import * # third-party
from portfolio import Portfolio, Google_Sheet # author's
from account import User, Asset, Taxation # author's
from data_analysis import Data_Analysis # author's
from transaction import Transaction # author's

user = SHEET.worksheet('user')
data = user.get_all_values()

print(data)