import tkinter as tk

# Function to update the display when a button is clicked
def button_click(number):
    if display.get() == "Error":  # Check if display shows an error
        clear_display()  # Clear display if it shows an error
    if number == "C":
        clear_display()
    elif number == "DEL":
        delete_last_character()
    elif number == "=":
        operate()
    else:
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, str(current) + str(number))

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)
    
# Function to delete the last character from display
def delete_last_character():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

# Function to perform arithmetic operation
def operate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator - 93|\\|!(_)5")

# Create the display
display = tk.Entry(window, width=40, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Define button labels
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("DEL", 4, 2), ("+", 4, 3), 
    ("=", 4, 4)  # "=" button remains in the same row
]

# Create buttons
for (text, row, col) in buttons:
    button = tk.Button(window, text=text, padx=20, pady=20, command=lambda num=text: button_click(num))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Adjust row and column sizes
for i in range(5):  
    window.grid_rowconfigure(i, weight=1, uniform="row")
for i in range(5):  
    window.grid_columnconfigure(i, weight=1, uniform="col")
    
    # Create a frame for the background color in column 4, rows 1-3
background_frame = tk.Frame(window, bg="#10283a")
background_frame.grid(row=0, column=4, rowspan=4, sticky="nsew")

# Run the application
window.mainloop()
