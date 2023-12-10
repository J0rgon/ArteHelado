import tkinter as tk

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

root = tk.Tk()
root.title("Scrollable Labels Example")

# Create a vertical scrollbar
scrollbar = tk.Scrollbar(root, orient='vertical')

# Create a canvas to hold the labels and connect it to the scrollbar
canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
canvas.pack(side='left', fill='both', expand=True)

# Configure the scrollbar to control the canvas
scrollbar.config(command=canvas.yview)

# Frame to contain the labels
label_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=label_frame, anchor='nw')

# List of labels (replace this with your labels)
labels = []
for i in range(1, 21):
    label = tk.Label(label_frame, text=f"Label {i}")
    label.pack()

labels.append(tk.Label(label_frame, text="Last Label"))

# Update the scroll region when the canvas size changes
canvas.bind('<Configure>', on_configure)

# Pack the scrollbar to the right of the canvas
scrollbar.pack(side='right', fill='y')

root.mainloop()
