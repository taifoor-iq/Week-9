import tkinter as tk

def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(key))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("320x380")
root.resizable(0, 0)
root.configure(bg="#1e1e2f")   # darker background

entry = tk.Entry(
    root,
    font=("Arial", 20),
    bd=10,
    relief=tk.RIDGE,
    justify="right",
    bg="#ffffff",              # white display
    fg="#000000"
)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3),
]

for (text, row, col) in buttons:
    if text == "C":
        action = clear
        color = "#ff6b6b"   # red clear button
    elif text == "=":
        action = calculate
        color = "#51cf66"   # green result button
    elif text in ['+', '-', '*', '/']:
        action = lambda x=text: press(x)
        color = "#74c0fc"   # blue operators
    else:
        action = lambda x=text: press(x)
        color = "#adb5bd"   # light gray numbers

    tk.Button(
        root,
        text=text,
        width=5,
        height=2,
        font=("Arial", 14),
        bg=color,
        fg="black",
        command=action
    ).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()