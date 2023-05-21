from modules.utilities import clear_screen
import time
from modules.utilities import bullet_point, slow_type, BOLD, RESET

def welcome_users(login_func):
    while True:
        clear_screen()
        print(f"{BOLD}WELCOME TO TENAM!{RESET}\n\nYour comprehensive crypto tracker. A dynamic\n"
              "tool for all your crypto investments in a single interface,\n"
              "no need to access each platform individually.\n\nAt present, "
              "you'll deal with static data from gspread, due to the\n"
              "sensitive nature of project delivery on GitHub.")
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
