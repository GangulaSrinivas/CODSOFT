import tkinter as tk

# Function to perform calculations
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()
        
        if operator == '+':
            result.set(num1 + num2)
        elif operator == '-':
            result.set(num1 - num2)
        elif operator == '*':
            result.set(num1 * num2)
        elif operator == '/':
            if num2 != 0:
                result.set(num1 / num2)
            else:
                result.set("Cannot divide by zero")
    except ValueError:
        result.set("Invalid input")

# Create the main window
window = tk.Tk()
window.title(" Calculator")

# Entry fields for numbers
entry_num1 = tk.Entry(window, font=('Gravitas One', 40))
entry_num2 = tk.Entry(window, font=('Gravitas One', 40))

# Variable to store the operator choice
operator_var = tk.StringVar()
operator_var.set('+')  # Default operator is addition

# Radio buttons for operator selection
addition_radio = tk.Radiobutton(window, text='Add(+)', variable=operator_var, value='+', font=('poppins', 30))
subtraction_radio = tk.Radiobutton(window, text='Sub(-)', variable=operator_var, value='-', font=('poppins', 30))
multiplication_radio = tk.Radiobutton(window, text='Mul(*)', variable=operator_var, value='*', font=('poppins', 30))
division_radio = tk.Radiobutton(window, text='Div(/)', variable=operator_var, value='/', font=('poppins', 30))

# Button to perform calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate, font=('Gravitas One', 40))

# Label to display the result
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result, font=('Gravitas One', 45))

# Arrange widgets in the window
entry_num1.pack(pady=10)
entry_num2.pack(pady=10)
addition_radio.pack()
subtraction_radio.pack()
multiplication_radio.pack()
division_radio.pack()
calculate_button.pack(pady=10)
result_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()
