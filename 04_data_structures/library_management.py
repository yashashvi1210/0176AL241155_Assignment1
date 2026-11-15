library = {"Python Basics": 3, "Data Structures": 2, "Algorithms": 1}

while True:
    print("\n1. Show books  2. Add book  3. Issue book  4. Return book  5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        for book, qty in library.items():
            print(f"{book}: {qty} copies")

    elif choice == "2":
        name = input("Book name: ")
        qty = int(input("Quantity to add: "))
        library[name] = library.get(name, 0) + qty
        print("Book added.")

    elif choice == "3":
        name = input("Book name to issue: ")
        if library.get(name, 0) > 0:
            library[name] -= 1
            print("Book issued.")
        else:
            print("Sorry, book not available.")

    elif choice == "4":
        name = input("Book name to return: ")
        if name in library:
            library[name] += 1
            print("Book returned.")
        else:
            print("This book does not belong to our library.")

    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
