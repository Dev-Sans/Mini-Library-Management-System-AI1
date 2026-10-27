from datetime import date

books = {}
brw = {}

def add_books(num):
    for i in range(num):
        bid = int(input("Enter Book ID: "))
        if bid in books:
            print("Book ID already exists!")
            continue
        title = input("Book title: ")
        auth = input("Author: ")

        books[bid] = [title, auth, "Available"]
    return books

def search(book_id):
    if book_id in books:
        print("Book record found:", books[book_id])
    else:
        print("No matching records found.")

def brb():
    bid = int(input("Enter Book ID: "))
    if bid not in books:
        print("Book not found!")
        return
    if books[bid][2] == "Not available":
        print("Book is already borrowed!")
        return
    brwr = input("Borrower ID: ")
    brw_date = input("Borrow date (YYYY-MM-DD): ")
    due_date = input("Due date (YYYY-MM-DD): ")
    if due_date < brw_date:
        print("Due date cannot be before borrow date!")
        return
    brw[bid] = [brwr, brw_date, due_date, None]
    books[bid][2] = "Not available"

    print("Book borrowed successfully!")

def return_book():
    bid = int(input("Enter Book ID: "))
    if bid not in brw or brw[bid][3] is not None:
        print("No active borrowing record found!")
        return
    rdate = input("Return date (YYYY-MM-DD): ")
    brw[bid][3] = rdate
    books[bid][2] = "Available"
    print("Book returned successfully!")

def total():
    print("Total books:", len(books))

def avbl_books():
    print("Available books:")
    for bid, val in books.items():
        if val[2] == "Available":
            print(bid, val)

def brwd_books():
    print("Currently borrowed books:")
    for bid, val in books.items():
        if val[2] == "Not available":
            print(bid, val, brw[bid])

def overdue_books():
    today = date.today().isoformat()
    print("Overdue books:")
    found = False
    for bid, record in brw.items():
        if record[3] is None and record[2] < today:
            print(bid, books[bid], record)
            found = True
    if not found:
        print("No overdue books.")

def library_summary():
    available = sum(
        1 for val in books.values()
        if val[2] == "Available"
    )
    borrowed = len(books) - available
    print("Total books:", len(books))
    print("Available books:", available)
    print("Borrowed books:", borrowed)


def save_records():
    with open("library_records.txt", "w") as file:
        file.write("BOOK RECORDS\n")
        for bid, val in books.items():
            file.write(f"{bid}: {val}\n")
        file.write("\nBORROWING RECORDS\n")
        for bid, val in brw.items():
            file.write(f"{bid}: {val}\n")
    print("Records saved successfully!")


while True:
    print("\n--- MINI LIBRARY MANAGEMENT SYSTEM ---")
    print("1. Add books")
    print("2. Search for a book")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Total books")
    print("6. Available books")
    print("7. Borrowed books")
    print("8. Overdue books")
    print("9. Library summary")
    print("10. Save records")
    print("11. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        num = int(input("How many books do you want to add? "))
        add_books(num)

    elif choice == "2":
        bid = int(input("Enter Book ID: "))
        search(bid)

    elif choice == "3":
        brb()

    elif choice == "4":
        return_book()

    elif choice == "5":
        total()

    elif choice == "6":
        avbl_books()

    elif choice == "7":
        brwd_books()

    elif choice == "8":
        overdue_books()

    elif choice == "9":
        library_summary()

    elif choice == "10":
        save_records()

    elif choice == "11":
        save_records()
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
