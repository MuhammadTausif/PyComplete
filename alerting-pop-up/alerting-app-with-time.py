import tkinter as tk
from threading import Timer
from time import strftime

# Define the time delay in seconds
delay = 300

# Function to create a popup window
def create_popup():
    # Create a new Tkinter window
    window = tk.Tk()
    window.title("Popup Window")

    # Set the window to stay on top of all other windows
    window.attributes('-topmost', True)

    # Set the window to cover the whole screen
    window.attributes('-fullscreen', True)

    # Function to close the window and restart the timer
    def on_close():
        window.destroy()
        start_timer()

    # Bind the close event to the on_close function
    window.protocol("WM_DELETE_WINDOW", on_close)

    # Function to update the time
    def time():
        string = strftime('%H:%M:%S %p')
        label.config(text = string)
        label.after(1000, time)

    # Create a label to display the time
    label = tk.Label(window, font = ('calibri', 40, 'bold'),
                     background = 'purple',
                     foreground = 'white')

    # Pack the label into the window
    label.pack(anchor = 'center')
    time()

    # Start the Tkinter event loop
    window.mainloop()

# Function to start the timer
def start_timer():
    t = Timer(delay, create_popup)
    t.start()

# Start the timer for the first time
start_timer()

# Print a success message
print(f"A fullscreen popup window with the current time will appear after {delay} seconds and reappear after being closed")