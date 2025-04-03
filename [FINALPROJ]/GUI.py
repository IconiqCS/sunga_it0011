import os  # Import os module for file operations
import tkinter as tk  # Import tkinter for the graphical user interface (GUI)
from tkinter import messagebox, ttk  # Import messagebox for pop-up messages and ttk for styled widgets
import csv  # Import csv module for reading and writing CSV files

# File to store user data
DATA_FILE = "users.csv"

# Ensure the data file exists
if not os.path.exists(DATA_FILE):  # Check if the CSV file doesn't exist
    with open(DATA_FILE, "w", newline="") as file:  # Create the file if it doesn't exist
        writer = csv.writer(file)  # Create a CSV writer object
        writer.writerow(["First Name", "Middle Name", "Last Name", "Birthday", "Gender"])  # Write header row

# Function to save user information to the CSV file
def save_user(first_name, middle_name, last_name, birthday, gender):
    """Saves user information to a CSV file."""
    # Check if any required fields are empty (first_name, last_name, birthday, gender)
    if not all([first_name, last_name, birthday, gender]):
        messagebox.showerror("Error", "All fields except middle name are required!")  # Show error message
        return
    
    try:
        with open(DATA_FILE, "a", newline="") as file:  # Open the CSV file in append mode
            writer = csv.writer(file)  # Create a CSV writer object
            writer.writerow([first_name, middle_name, last_name, birthday, gender])  # Write the user data to the file
        messagebox.showinfo("Success", "User registered successfully!")  # Show success message
    except Exception as e:  # If there is an error, show an error message
        messagebox.showerror("Error", f"Failed to save user: {e}")

# Function to open the sign-up form
def sign_up():
    """Opens the sign-up form."""
    def submit():  # Submit the user data
        save_user(first_name_entry.get().strip(), middle_name_entry.get().strip(),
                  last_name_entry.get().strip(), birthday_entry.get().strip(),
                  gender_var.get())  # Get values from form fields and save them
        sign_up_window.destroy()  # Close the sign-up window
    
    # Create a new window for sign-up
    sign_up_window = tk.Toplevel(root)
    sign_up_window.title("Sign Up")
    sign_up_window.geometry("350x250")
    sign_up_window.configure(bg="#ADD8E6")  # Set background color of the window
    
    fields = ["First Name", "Middle Name", "Last Name", "Birthday (YYYY-MM-DD)"]  # Define form fields
    entries = []  # List to store entry widgets for user input
    
    # Loop to create the entry fields for the user to fill out
    for i, field in enumerate(fields):
        ttk.Label(sign_up_window, text=field+":").grid(row=i, column=0, sticky="w", padx=10, pady=5)  # Create labels
        entry = ttk.Entry(sign_up_window)  # Create text entry widgets
        entry.grid(row=i, column=1, padx=10, pady=5)  # Position entry widgets in the window
        entries.append(entry)  # Add each entry to the list of entries
    
    first_name_entry, middle_name_entry, last_name_entry, birthday_entry = entries  # Assign entry widgets to variables
    
    ttk.Label(sign_up_window, text="Gender:").grid(row=4, column=0, sticky="w", padx=10, pady=5)  # Label for gender field
    gender_var = tk.StringVar(value="Other")  # Default gender selection
    gender_frame = ttk.Frame(sign_up_window)  # Frame to hold gender radio buttons
    gender_frame.grid(row=4, column=1, pady=5)  # Position gender radio buttons
    ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left")  # Male option
    ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left")  # Female option
    
    ttk.Button(sign_up_window, text="Submit", command=submit).grid(row=5, column=1, pady=10)  # Submit button

# Function to view all records from the CSV file
def view_records():
    """Displays all records in a new window."""
    view_window = tk.Toplevel(root)  # Create a new window
    view_window.title("All Records")
    view_window.geometry("500x300")
    view_window.configure(bg="#ADD8E6")  # Set background color of the window
    
    # Create a treeview widget to display records in tabular format
    tree = ttk.Treeview(view_window, columns=("First Name", "Middle Name", "Last Name", "Birthday", "Gender"), show="headings")
    for col in tree['columns']:  # Loop through the columns and set their headings
        tree.heading(col, text=col)
        tree.column(col, width=100)  # Set column width
    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)  # Position treeview in the window
    
    try:
        with open(DATA_FILE, "r") as file:  # Open the CSV file in read mode
            reader = csv.reader(file)  # Create a CSV reader object
            next(reader)  # Skip the header row
            for row in reader:  # Loop through the rows in the CSV file
                tree.insert("", tk.END, values=row)  # Insert each row into the treeview
    except FileNotFoundError:  # If file is not found, show error message
        messagebox.showerror("Error", "No records found.")

# Function to search for a user record based on input
def search_record():
    """Searches for a user record based on input."""
    def search():  # Function to perform the search operation
        query = search_entry.get().strip().lower()  # Get the search query and make it lowercase
        result_window = tk.Toplevel(root)  # Create a new window to display search results
        result_window.title("Search Results")
        result_window.geometry("500x300")
        
        tree = ttk.Treeview(result_window, columns=("First Name", "Middle Name", "Last Name", "Birthday", "Gender"), show="headings")
        for col in tree['columns']:  # Set headings and column widths
            tree.heading(col, text=col)
            tree.column(col, width=100)
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        found = False  # Flag to check if any matching records are found
        try:
            with open(DATA_FILE, "r") as file:  # Open the CSV file in read mode
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:  # Loop through the rows in the CSV file
                    if any(query in field.lower() for field in row):  # Check if any field matches the search query
                        tree.insert("", tk.END, values=row)  # Insert matching row into treeview
                        found = True
        except FileNotFoundError:  # If file is not found, show error message
            messagebox.showerror("Error", "No records found.")
        
        if not found:  # If no matches found, show info message
            messagebox.showinfo("Result", "No matching records found.")
    
    # Create a new window for the search feature
    search_window = tk.Toplevel(root)
    search_window.title("Search Record")
    search_window.geometry("300x150")
    search_window.configure(bg="#ADD8E6")  # Set background color
    
    ttk.Label(search_window, text="Enter name to search:").pack(pady=5)  # Label for search field
    search_entry = ttk.Entry(search_window)  # Create search entry field
    search_entry.pack(pady=5)
    ttk.Button(search_window, text="Search", command=search).pack(pady=5)  # Search button

# Function to exit the application
def exit_program():
    """Closes the application."""
    root.destroy()  # Close the main application window

# Main GUI window
root = tk.Tk()  # Create the main window
root.title("User Management System")  # Set window title
root.geometry("400x300")  # Set window size
root.configure(bg="#ADD8E6")  # Set background color of the window

frame = ttk.Frame(root, padding=20)  # Create a frame to hold buttons and labels
frame.pack(expand=True)  # Position the frame in the window

# Add labels and buttons to the main window
ttk.Label(frame, text="User Management System", font=("Poppins", 18, "bold")).pack(pady=10)
ttk.Button(frame, text="Sign Up", command=sign_up, width=30).pack(pady=5)
ttk.Button(frame, text="View All Records", command=view_records, width=30).pack(pady=5)
ttk.Button(frame, text="Search a Record", command=search_record, width=30).pack(pady=5)
ttk.Button(frame, text="Exit", command=exit_program, width=30).pack(pady=5)

root.mainloop()  # Start the GUI event loop
