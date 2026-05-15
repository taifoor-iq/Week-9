import tkinter as tk

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "add":
            result = num1 + num2
        elif operation == "sub":
            result = num1 - num2
        elif operation == "mul":
            result = num1 * num2
        elif operation == "div":
            result = num1 / num2

        result_label.config(text=f"Result: {result}")

    except Exception as e:
        result_label.config(text="Error")


# Clear Function
def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")


# Main Window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x350")
root.config(bg="lightblue")


# Widgets

# Inputs
tk.Label(root, text="Enter first number", bg="lightblue").pack()

entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number", bg="lightblue").pack()

entry2 = tk.Entry(root)
entry2.pack()


# Buttons
tk.Button(
    root,
    text="Add",
    bg="green",
    fg="white",
    command=lambda: calculate("add")
).pack(pady=5)

tk.Button(
    root,
    text="Subtract",
    bg="orange",
    fg="white",
    command=lambda: calculate("sub")
).pack(pady=5)

tk.Button(
    root,
    text="Multiply",
    bg="blue",
    fg="white",
    command=lambda: calculate("mul")
).pack(pady=5)

tk.Button(
    root,
    text="Divide",
    bg="purple",
    fg="white",
    command=lambda: calculate("div")
).pack(pady=5)

# Clear Button
tk.Button(
    root,
    text="Clear",
    bg="red",
    fg="white",
    command=clear
).pack(pady=5)


# Result
result_label = tk.Label(
    root,
    text="Result: ",
    bg="lightblue"
)

result_label.pack(pady=10)

root.mainloop()