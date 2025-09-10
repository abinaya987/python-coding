contacts = {}  

def add_contacts():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email (optional): ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nAll Contacts:")
    for i, (name, info) in enumerate(contacts.items(), start=1):
        print(f"{i}. Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    print()

def search_contact():
    term = input("Enter name to search: ").strip().lower()
    found = False
    for name, info in contacts.items():
        if term in name.lower():
            print(f"Found: Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
            found = True
    if not found:
        print("No matching contacts found.")
    print()

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!\n")
    else:
        print(f"Contact '{name}' not found.\n")


while True:
    print("==== Contact Book ====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        add_contacts()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting Contact Book... Goodbye!")
        break
    else:
        print("Invalid choice! Please select between 1-5.\n")
