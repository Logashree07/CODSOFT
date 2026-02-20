import json
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
FILE_NAME = "contacts.json"
def print_header(title):
    print("\n" + "=" * 40)
    print(title.center(40))
    print("=" * 40)
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)
def add_contact():
    contacts = load_contacts()
    
    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty.\n")
        return
    
    phone = input("Enter Phone Number: ").strip()
    if not phone.isdigit():
        print("Phone number must contain only digits.\n")
        return
    
    email = input("Enter Email: ").strip()
    if "@" not in email:
        print("Invalid email format.\n")
        return
    
    address = input("Enter Address: ").strip()
    
    # Prevent duplicate phone numbers
    for contact in contacts:
        if contact["phone"] == phone:
            print("Contact with this phone number already exists.\n")
            return
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    
    contacts.append(contact)
    save_contacts(contacts)
    
    print("Contact added successfully!\n")
def view_contacts():
    contacts = load_contacts()
    
    if not contacts:
        print("No contacts found.")
        return
    
    for index, contact in enumerate(contacts, start=1):
        print("\n" + "-" * 40)
        print(f"Contact {index}")
        print("-" * 40)
        print(f"Name   : {contact['name']}")
        print(f"Phone  : {contact['phone']}")
        print(f"Email  : {contact['email']}")
        print(f"Address: {contact['address']}")
    print("-" * 40)
def search_contact():
    contacts = load_contacts()
    search_name = input("Enter name to search: ").lower()
    
    found = False
    
    for contact in contacts:
        if search_name in contact["name"].lower():
            print("\n===== Contact Found =====")
            print(f"Name   : {contact['name']}")
            print(f"Phone  : {contact['phone']}")
            print(f"Email  : {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
    
    if not found:
        print("No matching contact found.\n")
def update_contact():
    contacts = load_contacts()
    name_to_update = input("Enter name to update: ").lower()
    
    for contact in contacts:
        if name_to_update == contact["name"].lower():
            contact["phone"] = input("Enter new phone: ")
            contact["email"] = input("Enter new email: ")
            contact["address"] = input("Enter new address: ")
            
            save_contacts(contacts)
            print("Contact updated successfully!\n")
            return
    
    print("Contact not found.\n")
def delete_contact():
    contacts = load_contacts()
    name_to_delete = input("Enter name to delete: ").lower()
    
    for contact in contacts:
        if name_to_delete == contact["name"].lower():
            confirm = input("Are you sure you want to delete? (y/n): ").lower()
            
            if confirm == "y":
                contacts.remove(contact)
                save_contacts(contacts)
                print("Contact deleted successfully!\n")
            else:
                print("Deletion cancelled.\n")
            return
    
    print("Contact not found.\n")
def main():
    while True:
        clear_screen()
        print_header("CONTACT BOOK MANAGEMENT SYSTEM")
        
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        print("-" * 40)
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            clear_screen()
            print_header("ADD CONTACT")
            add_contact()
            input("\nPress Enter to continue...")
            
        elif choice == "2":
            clear_screen()
            print_header("VIEW CONTACTS")
            view_contacts()
            input("\nPress Enter to continue...")
            
        elif choice == "3":
            clear_screen()
            print_header("SEARCH CONTACT")
            search_contact()
            input("\nPress Enter to continue...")
            
        elif choice == "4":
            clear_screen()
            print_header("UPDATE CONTACT")
            update_contact()
            input("\nPress Enter to continue...")
            
        elif choice == "5":
            clear_screen()
            print_header("DELETE CONTACT")
            delete_contact()
            input("\nPress Enter to continue...")
            
        elif choice == "6":
            clear_screen()
            print_header("THANK YOU")
            print("Exiting Contact Book...")
            break
            
        else:
            print("Invalid choice! Please select between 1-6.")
            input("Press Enter to try again...")

if __name__ == "__main__":
    main()