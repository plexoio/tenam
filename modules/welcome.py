from modules.utilities import clear_screen
import time


def welcome_users(login_func):
    while True:
        clear_screen()
        print("TENAM\n\nYour comprehensive crypto tracker. A dynamic\n"
              "tool for all your crypto investments in a single interface,\n"
              "no need to access each platform individually.\n\nAt present, "
              "you'll deal with static data from gspread, due to open\n"
              "and sensitive nature of projects delivery on GitHub.")
        try:
            enter = input(
                f'\nTo Enter System please input "Y":\n')
            if enter.lower() == 'y':
                clear_screen()
                login_func()  # Instance of login_input()
                break
            else:
                print('Wrong value entered, it has to be "Y"')
                
        except KeyboardInterrupt:
            print("Key not accepted, please try again!")
            
    return True
