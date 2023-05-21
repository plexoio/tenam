from modules.utilities import clear_screen
import time
from modules.utilities import bullet_point, slow_type, BOLD, RESET
from textwrap import fill


def welcome_users(login_func):
    '''
    Print welcome message and validate human with Y to enter
    '''
    while True:
        clear_screen()
        brand = f"{BOLD}WELCOME TO TENAM!{RESET}\n"
        welcome = (
           "Your comprehensive crypto tracker. A dynamic "
           "tool for all your crypto investments in a single interface, "
           "no need to access each platform individually. At present, "
           "you'll deal with static data from gspread, due to the "
           "sensitive nature of project delivery on GitHub.")
        print(brand)
        print(fill(welcome, 80))
        try:
            enter = input(
                f'\n{bullet_point} Input "Y" to enter:\n')
            if enter.lower() == 'y':
                clear_screen()
                login_func()  # Instance of login_input()
                break
            else:
                slow_type('Wrong value entered, it has to be "Y"')
                time.sleep(1)
        except KeyboardInterrupt:
            slow_type(" Key not accepted, please try again!")
            time.sleep(1)
    return True
