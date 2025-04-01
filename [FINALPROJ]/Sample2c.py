import tkinter as tk
from tkinter import messagebox
import csv

# File to store user data
DATA_FILE = "users.csv"

def save_user(first_name, middle_name, last_name, birthday, gender):
    try:
        with open(DATA_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([first_name, middle_name, last_name, birthday, gender])
        messagebox.showinfo("Success", "User registered successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save user: {e}")

def sign_up():
    def submit():
        save_user(first_name_entry.get(), middle_name_entry.get(), last_name_entry.get(),
                  birthday_entry.get(), gender_var.get())
        sign_up_window.destroy()
    
    sign_up_window = tk.Toplevel(root)
    sign_up_window.title("Sign Up")
    
    tk.Label(sign_up_window, text="First Name:").grid(row=0, column=0)
    first_name_entry = tk.Entry(sign_up_window)
    first_name_entry.grid(row=0, column=1)
    
    tk.Label(sign_up_window, text="Middle Name:").grid(row=1, column=0)
    middle_name_entry = tk.Entry(sign_up_window)
    middle_name_entry.grid(row=1, column=1)
    
    tk.Label(sign_up_window, text="Last Name:").grid(row=2, column=0)
    last_name_entry = tk.Entry(sign_up_window)
    last_name_entry.grid(row=2, column=1)
    
    tk.Label(sign_up_window, text="Birthday (YYYY-MM-DD):").grid(row=3, column=0)
    birthday_entry = tk.Entry(sign_up_window)
    birthday_entry.grid(row=3, column=1)
    
    tk.Label(sign_up_window, text="Gender:").grid(row=4, column=0)
    gender_var = tk.StringVar(value="Other")
    tk.Radiobutton(sign_up_window, text="Male", variable=gender_var, value="Male").grid(row=4, column=1)
    tk.Radiobutton(sign_up_window, text="Female", variable=gender_var, value="Female").grid(row=4, column=2)
    
    tk.Button(sign_up_window, text="Submit", command=submit).grid(row=5, column=1)

def view_records():
    view_window = tk.Toplevel(root)
    view_window.title("All Records")
    
    try:
        with open(DATA_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                tk.Label(view_window, text=" | ".join(row)).pack()
    except FileNotFoundError:
        tk.Label(view_window, text="No records found.").pack()

def search_record():
    def search():
        query = search_entry.get().lower()
        search_window = tk.Toplevel(root)
        search_window.title("Search Results")
        
        found = False
        try:
            with open(DATA_FILE, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if query in [field.lower() for field in row]:
                        tk.Label(search_window, text=" | ".join(row)).pack()
                        found = True
        except FileNotFoundError:
            messagebox.showerror("Error", "No records found.")
        
        if not found:
            tk.Label(search_window, text="No matching records found.").pack()
    
    search_window = tk.Toplevel(root)
    search_window.title("Search Record")
    
    tk.Label(search_window, text="Enter name to search:").pack()
    search_entry = tk.Entry(search_window)
    search_entry.pack()
    tk.Button(search_window, text="Search", command=search).pack()

def exit_program():
    root.destroy()

# Main GUI
root = tk.Tk()
root.title("User Management System")

tk.Label(root, text="Welcome to the User Management System").pack()
tk.Button(root, text="Sign Up", command=sign_up).pack()
tk.Button(root, text="View All Records", command=view_records).pack()
tk.Button(root, text="Search a Record", command=search_record).pack()
tk.Button(root, text="Exit", command=exit_program).pack()

root.mainloop()
