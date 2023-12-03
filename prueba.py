import tkinter as tk

def on_button_click():
    print("Button Clicked!")

root = tk.Tk()
root.title("Resizable Buttons Example")

# Create a frame
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Configure rows and columns to make the button expand or shrink
frame.grid_rowconfigure(0, weight=1, uniform="group1", minsize=50)  # row 0
frame.grid_columnconfigure(0, weight=1, uniform="group1", minsize=100)  # column 0

# Create a button and place it in the frame
button = tk.Button(frame, text="Click me!", command=on_button_click)
button.grid(row=0, column=0, sticky="nsew")  # sticky="nsew" makes the button expand

# Create another button to demonstrate
button2 = tk.Button(frame, text="Another Button", command=on_button_click)
button2.grid(row=0, column=1, sticky="nsew")

# Run the Tkinter event loop
root.mainloop()
