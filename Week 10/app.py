import tkinter as tk
from tkinter import messagebox
users = {}

def read_file():
    return users

def write_file(username, password):
    users[username] = password

def login():
    username = login_user.get()
    password = login_pass.get()

    data = read_file()

    if username in data and data[username] == password:
        messagebox.showinfo("Success", f"Welcome {username}!")
    else:
        messagebox.showerror("Error", "Wrong username or password")

def signup():
    username = signup_user.get()
    password = signup_pass.get()

    if username == "" or password == "":
        messagebox.showwarning("Error", "Fields cannot be empty")
        return

    data = read_file()

    if username in data:
        messagebox.showerror("Error", "User already exists")
    else:
        write_file(username, password)
        messagebox.showinfo("Success", "Signup successful!")
        signup_win.destroy()

def main():
    global root, login_user, login_pass, signup_win, signup_user, signup_pass

    root = tk.Tk()
    root.title("Login System")
    root.geometry("350x300")
    root.resizable(False, False)

    tk.Label(root, text="Login", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Username").pack()
    login_user = tk.Entry(root, width=30)
    login_user.pack(pady=5)

    tk.Label(root, text="Password").pack()
    login_pass = tk.Entry(root, show="*", width=30)
    login_pass.pack(pady=5)

    tk.Button(root, text="Login", width=15, command=login).pack(pady=10)
    tk.Button(root, text="Signup", width=15, command=open_signup).pack()

    root.mainloop()

def open_signup():
    global signup_win, signup_user, signup_pass

    signup_win = tk.Toplevel(root)
    signup_win.title("Signup Page")
    signup_win.geometry("300x250")
    signup_win.resizable(False, False)

    tk.Label(signup_win, text="Signup", font=("Arial", 14)).pack(pady=10)

    tk.Label(signup_win, text="Username").pack()
    signup_user = tk.Entry(signup_win, width=25)
    signup_user.pack(pady=5)

    tk.Label(signup_win, text="Password").pack()
    signup_pass = tk.Entry(signup_win, show="*", width=25)
    signup_pass.pack(pady=5)

    tk.Button(signup_win, text="Create Account", command=signup).pack(pady=15)


main()