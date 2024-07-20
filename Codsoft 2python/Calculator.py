import tkinter as tk

# Function to update the entry widget
def press(key):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + key)

# Function to calculate the result
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Function to delete the last character
def delete():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="#f0f0f0")

# Create the entry widget
entry = tk.Entry(root, width=16, font=('Arial', 24), bg="#ffffff", bd=10, insertbackground='black')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button definitions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('Del', 5, 1)
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=('Arial', 18), bg="#4CAF50", fg="white", command=evaluate)
    elif text == 'C':
        button = tk.Button(root, text=text, font=('Arial', 18), bg="#F44336", fg="white", command=clear)
    elif text == 'Del':
        button = tk.Button(root, text=text, font=('Arial', 18), bg="#FFC107", fg="black", command=delete)
    else:
        button = tk.Button(root, text=text, font=('Arial', 18), bg="#2196F3", fg="white", command=lambda t=text: press(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

# Adjust column and row weights
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

# Run the application
root.mainloop()
