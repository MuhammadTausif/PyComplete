import curses
from curses import wrapper

def main(stdscr):
    # Clear the screen
    stdscr.clear()

    # Print a message
    stdscr.addstr("Hello, this is a sample curses application!\n")
    stdscr.addstr("Press any key to exit.")

    # Refresh the screen to show the output
    stdscr.refresh()

    # Wait for the user to press a key
    stdscr.getch()

# Initialize the curses application
wrapper(main)
