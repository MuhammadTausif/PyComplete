import tkinter as tk
from threading import Timer

# Define the time delay in seconds
delay = 60

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

    # Create a label with a message
    message = tk.Label(window, text="This is a popup window!", font=("Helvetica", 24))
    message.pack(expand=True)

    # Start the Tkinter event loop
    window.mainloop()

# Function to start the timer
def start_timer():
    t = Timer(delay, create_popup)
    t.start()

# Start the timer for the first time
start_timer()

# Print a success message
print(f"A fullscreen popup window will appear after {delay} seconds and reappear after being closed.")