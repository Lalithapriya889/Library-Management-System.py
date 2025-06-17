"""
Library Management System
Console-based app using Python and SQLite
"""

import sqlite3

# Connect to SQLite DB
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create the books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
""")
conn.commit()

# Function to add a book
def add_book():
    title = input("Enter title: ")
    author = input("Enter author: ")
    quantity = input("Enter quantity: ")
    cursor.execute("INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)", (title, author, quantity))
    conn.commit()
    print("✅ Book added successfully.")

# Function to view all books
def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    if books:
        print("\n📚 All Books:")
        for b in books:
            print(f"ID: {b[0]}, Title: {b[1]}, Author: {b[2]}, Quantity: {b[3]}")
    else:
        print("No books available.")

# Function to search for a book by title
def search_book():
    keyword = input("Enter title to search: ")
    cursor.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + keyword + '%',))
    results = cursor.fetchall()
    if results:
        print("\n🔍 Search Results:")
        for r in results:
            print(f"ID: {r[0]}, Title: {r[1]}, Author: {r[2]}, Quantity: {r[3]}")
    else:
        print("No matching books found.")

# Function to update a book's quantity
def update_book():
    book_id = input("Enter Book ID to update: ")
    quantity = input("Enter new quantity: ")
    cursor.execute("UPDATE books SET quantity = ? WHERE id = ?", (quantity, book_id))
    if cursor.rowcount == 0:
        print("⚠️ No such book found.")
    else:
        conn.commit()
        print("✅ Book updated.")

# Function to delete a book
def delete_book():
    book_id = input("Enter Book ID to delete: ")
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    if cursor.rowcount == 0:
        print("⚠️ No such book found.")
    else:
        conn.commit()
        print("✅ Book deleted.")

# Menu system
def menu():
    while True:
        print("\n===== 📖 Library Menu =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Book Quantity")
        print("5. Delete Book")
        print("6. Exit")
        choice = input("Enter choice (1-6): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            update_book()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    menu()
    conn.close()
