import tkinter as tk
import time

# Create the main window
digital_clock = tk.Tk()
digital_clock.geometry("600x300")
digital_clock.title('Digital Clock')

# Create the label widget
label = tk.Label(digital_clock, font=('calibri', 40, 'bold'),
                 background='#AA0000',
                 foreground='white')

# Pack the label at the center of the window
label.pack(anchor='center')

# Define the time function
def update_time():
    string = time.strftime('%H:%M:%S %p')  # Get the current time
    label.config(text=string)  # Update the label with the current time
    label.after(1000, update_time)  # Call the time function again after 1000ms

# Call the time function for the first time
update_time()

# Start the main loop
digital_clock.mainloop()