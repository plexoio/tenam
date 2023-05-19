# Write your code to expect a terminal of 80 characters wide and 24 rows high
from modules.portfolio import Google_Portfolio, User, Asset, Transaction, Data_Analysis, Taxation  # author's
from modules.login import *

login_input() # call login

menu = Google_Portfolio() # After login launch Menu
menu.menu()