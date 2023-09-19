import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Step 1: Initialize the main application window
app = tk.Tk()
app.title("To-Do List")
app.configure(bg="#f0f0f0")  # Set the background color

# Step 2: Define functions for managing tasks

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove a task
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Function to update a task
def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        updated_task = entry.get()
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, updated_task)
        entry.delete(0, tk.END)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Function to mark a task as complete or incomplete
def toggle_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_item = task_listbox.get(selected_task_index)
        if task_item.startswith("✔ "):
            updated_task = task_item[2:]  # Remove the "✔ " prefix
        else:
            updated_task = "✔ " + task_item  # Add the "✔ " prefix
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, updated_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark.")

# Step 3: Create GUI elements

# Create a style for buttons
style = ttk.Style()
style.configure(
    "TButton",
    padding=10,
    relief="flat",
    foreground="Blue",       # Set button text color
    background="Black",     # Set button background color
    font=("Times New Roman", 16),
)

# Entry for adding/updating tasks
entry = tk.Entry(app, width=40, font=("Arial", 12))
entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Buttons for adding, updating, removing, and marking tasks
add_button = ttk.Button(app, text="Add Task", command=add_task, style="TButton")
update_button = ttk.Button(app, text="Update Task", command=update_task, style="TButton")
remove_button = ttk.Button(app, text="Remove Task", command=remove_task, style="TButton")
toggle_button = ttk.Button(app, text="Mark Task", command=toggle_task, style="TButton")
add_button.grid(row=0, column=1, padx=10, pady=10)
update_button.grid(row=1, column=1, padx=10, pady=10)
remove_button.grid(row=2, column=1, padx=10, pady=10)
toggle_button.grid(row=3, column=1, padx=10, pady=10)

# Listbox for displaying tasks
task_listbox = tk.Listbox(app, width=40, height=10, font=("Times New Roman", 15))
task_listbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Add a scrollbar for the listbox
scrollbar = tk.Scrollbar(app, orient="vertical", command=task_listbox.yview)
scrollbar.grid(row=1, column=2, sticky="ns")
task_listbox.configure(yscrollcommand=scrollbar.set)

# Configure grid layout
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)

# Step 4: Start the GUI main loop
app.mainloop()

