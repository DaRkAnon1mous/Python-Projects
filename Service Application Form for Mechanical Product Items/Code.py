import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3


# Database Setup
def setup_database():
    conn = sqlite3.connect("service_requests.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS service_requests (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        contact TEXT,
                        product TEXT,
                        issue TEXT,
                        service_date TEXT)''')
    conn.commit()
    conn.close()


# Function to submit form
def submit_form():
    name = entry_name.get()
    contact = entry_contact.get()
    product = entry_product.get()
    issue = entry_issue.get("1.0", tk.END).strip()
    service_date = entry_date.get()

    if not (name and contact and product and issue and service_date):
        messagebox.showerror("Error", "All fields are required!")
        return

    conn = sqlite3.connect("service_requests.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO service_requests (name, contact, product, issue, service_date) VALUES (?, ?, ?, ?, ?)",
                   (name, contact, product, issue, service_date))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Service Request Submitted Successfully!")
    clear_form()


# Function to clear form
def clear_form():
    entry_name.delete(0, tk.END)
    entry_contact.delete(0, tk.END)
    entry_product.delete(0, tk.END)
    entry_issue.delete("1.0", tk.END)
    entry_date.delete(0, tk.END)


# GUI Setup
root = tk.Tk()
root.title("Service Application Form")
root.geometry("450x500")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="Service Application Form", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

frame = tk.Frame(root, padx=10, pady=10, bg="#ffffff", relief=tk.RIDGE, borderwidth=2)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

tk.Label(frame, text="Name:", font=("Arial", 12), bg="#ffffff").grid(row=0, column=0, sticky="w", pady=5)
entry_name = ttk.Entry(frame, width=40)
entry_name.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Contact:", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, sticky="w", pady=5)
entry_contact = ttk.Entry(frame, width=40)
entry_contact.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Product Name:", font=("Arial", 12), bg="#ffffff").grid(row=2, column=0, sticky="w", pady=5)
entry_product = ttk.Entry(frame, width=40)
entry_product.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Issue Description:", font=("Arial", 12), bg="#ffffff").grid(row=3, column=0, sticky="nw", pady=5)
entry_issue = tk.Text(frame, height=5, width=30, wrap=tk.WORD)
entry_issue.grid(row=3, column=1, pady=5)

tk.Label(frame, text="Preferred Service Date:", font=("Arial", 12), bg="#ffffff").grid(row=4, column=0, sticky="w",
                                                                                       pady=5)
entry_date = ttk.Entry(frame, width=40)
entry_date.grid(row=4, column=1, pady=5)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Submit", command=submit_form, width=15).grid(row=0, column=0, padx=10)
ttk.Button(button_frame, text="Clear", command=clear_form, width=15).grid(row=0, column=1, padx=10)

setup_database()
root.mainloop()
