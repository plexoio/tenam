import os  # Built-in module for clearing screen depending on OS


def clear_screen():
    '''
    Used all around the code to clear console when needed to avoid overcrowding
    '''
    os.system('cls' if os.name == 'nt' else 'clear')