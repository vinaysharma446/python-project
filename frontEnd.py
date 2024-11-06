import tkinter as tk
from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="Vinay@123",  
    database="bookstore"  
)

cursor = db.cursor()


def browse_books():
    cursor.execute("SELECT title, author, price FROM books")
    results = cursor.fetchall()

    browse_window = tk.Toplevel()
    browse_window.title("Browse Books")

    if results:
        for book in results:
            tk.Label(browse_window, text=f"{book[0]} by {book[1]} - ${book[2]:.2f}", font=("Arial", 12)).pack(pady=5)
    else:
        tk.Label(browse_window, text="No books found.", font=("Arial", 12)).pack(pady=5)

def search_books():
    search_term = search_entry.get()
    cursor.execute("SELECT title, author, price FROM books WHERE title LIKE %s OR author LIKE %s", 
                   ('%' + search_term + '%', '%' + search_term + '%'))
    results = cursor.fetchall()

    search_window = tk.Toplevel()
    search_window.title("Search Results")

    if results:
        for book in results:
            tk.Label(search_window, text=f"{book[0]} by {book[1]} - ${book[2]:.2f}", font=("Arial", 12)).pack(pady=5)
    else:
        tk.Label(search_window, text="No results found.", font=("Arial", 12)).pack(pady=5)

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    price = float(price_entry.get())
    stock = int(stock_entry.get())

    cursor.execute("INSERT INTO books (title, author, price, stock) VALUES (%s, %s, %s, %s)", 
                   (title, author, price, stock))
    db.commit()

    messagebox.showinfo("Success", "Book added successfully!")
    clear_entries()  # Clear input fields after adding a book

def clear_entries():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    stock_entry.delete(0, tk.END)

def on_enter(e):
    e.widget['background'] = '#76c7c0'

def on_leave(e):
    e.widget['background'] = '#4CAF50' if e.widget['text'] == "Browse Books" else '#2196F3' if e.widget['text'] == "Search" else '#FF9800'

# Main GUI window
root = tk.Tk()
root.title("Online Bookstore Management System")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Browse Books Button
browse_button = tk.Button(root, text="Browse Books", command=browse_books, font=("Arial", 14), bg="#4CAF50", fg="white")
browse_button.pack(pady=10, padx=20, fill='x')
browse_button.bind("<Enter>", on_enter)
browse_button.bind("<Leave>", on_leave)

# Search Books Section
tk.Label(root, text="Search Books", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
search_entry = tk.Entry(root, font=("Arial", 12))
search_entry.pack(pady=5, padx=20, fill='x')
search_button = tk.Button(root, text="Search", command=search_books, font=("Arial", 12), bg="#2196F3", fg="white")
search_button.pack(pady=10)
search_button.bind("<Enter>", on_enter)
search_button.bind("<Leave>", on_leave)

# Add New Book Section
tk.Label(root, text="Add New Book", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)

tk.Label(root, text="Title", bg="#f0f0f0").pack()
title_entry = tk.Entry(root, font=("Arial", 12))
title_entry.pack(pady=5, padx=20, fill='x')

tk.Label(root, text="Author", bg="#f0f0f0").pack()
author_entry = tk.Entry(root, font=("Arial", 12))
author_entry.pack(pady=5, padx=20, fill='x')

tk.Label(root, text="Price", bg="#f0f0f0").pack()
price_entry = tk.Entry(root, font=("Arial", 12))
price_entry.pack(pady=5, padx=20, fill='x')

tk.Label(root, text="Stock", bg="#f0f0f0").pack()
stock_entry = tk.Entry(root, font=("Arial", 12))
stock_entry.pack(pady=5, padx=20, fill='x')

add_book_button = tk.Button(root, text="Add Book", command=add_book, font=("Arial", 12), bg="#FF9800", fg="white")
add_book_button.pack(pady=10)
add_book_button.bind("<Enter>", on_enter)
add_book_button.bind("<Leave>", on_leave)


root.mainloop()