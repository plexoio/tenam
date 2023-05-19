import os  # Built-in module for clearing screen depending on OS


def clear_screen():
    '''
    Used all around the code to clear console when needed to avoid overcrowding
    '''
    # Clear console for Windows, Linux, and macOS
    os.system('cls' if os.name == 'nt' else 'clear')

    # Move the cursor to the top left corner of the console
    print('\033[1;1H', end='')
