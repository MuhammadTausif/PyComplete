import time
import curses

msg = "Loading"

loading = True

def waiting(msg=f" {msg} "):
    width = 50
    speed = .2
    while loading == True:
        stdscr = curses.initscr()
        stdscr.addstr(0,0,msg.center(width, '_'))
        stdscr.refesh()
        time.sleep(speed)
        stdscr.addstr(0,0,msg.center(width, '\\'))
        stdscr.refesh()
        time.sleep(speed)
        stdscr.addstr(0,0,msg.center(width, '|'))
        stdscr.refesh()
        time.sleep(speed)
        stdscr.addstr(0,0,msg.center(width, '/'))
        stdscr.refesh()
        time.sleep(speed)

        stdscr.refresh()


# waiting()
