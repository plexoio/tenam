import os  # Built-in module for clearing screen depending on OS
import time

# Global Variables
bullet_point = "\u2022"
BOLD = '\033[1m'
RESET = '\033[0m'


def clear_screen():
    '''
    Used all around the code to clear console when needed to avoid overcrowding
    '''
    # Clear console for Windows, Linux, and macOS
    os.system('cls' if os.name == 'nt' else 'clear')


def slow_type(string, delay=0.05):
    '''
    Time function to delay letter printing use end="" & flush=True
    '''
    for chr in string:
        # end='' for not \n & flush allows output buffer
        print(chr, end='', flush=True)
        time.sleep(delay)
