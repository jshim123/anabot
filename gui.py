import tkinter as tk

def console_function():
    # logic from console application
    print("This is a console function.")

# create GUI window
root = tk.Tk()
root.title("Ana")

# create a button and bind it to the console function
button = tk.Button(root, text="Run Console Function", command=console_function)
button.pack()

# start GUI event loop
root.mainloop()
