contacts = {} 

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    print("\n--- Contacts ---")
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['Phone']}")
        print(f"Email: {info['Email']}")
        print(f"Address: {info['Address']}")
        print("-" * 20)

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, info in contacts.items():
        if search_term in name or search_term in info['Phone']:
            print(f"\n--- Contact found for '{search_term}' ---")
            print(f"Name: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print(f"Address: {info['Address']}")
            found = True
    if not found:
        print(f"No contact found for '{search_term}'.")

def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ")
    if name_to_delete in contacts:
        del contacts[name_to_delete]
        print(f"Contact '{name_to_delete}' deleted successfully!")
    else:
        print(f"No contact found with the name '{name_to_delete}'.")

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, 4, or 5.")
