import curses

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

try:
    # Initialize the screen
    stdscr = curses.initscr()
    
    # Turn off automatic echoing of keys to the screen
    curses.noecho()
    
    # React to keys instantly, without requiring the Enter key to be pressed
    curses.cbreak()

    # Enable keypad mode
    stdscr.keypad(True)

    # Call the main function with the initialized screen
    main(stdscr)
finally:
    # Revert the terminal to its original operating mode
    stdscr.keypad(False)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
