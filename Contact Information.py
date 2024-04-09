class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword.lower() in contact.phone.lower():
                results.append(contact)
        return results

    def update_contact(self, contact_idx, new_contact):
        if 1 <= contact_idx <= len(self.contacts):
            self.contacts[contact_idx - 1] = new_contact

    def delete_contact(self, contact_idx):
        if 1 <= contact_idx <= len(self.contacts):
            del self.contacts[contact_idx - 1]


def display_menu(contact_book):
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            add_new_contact(contact_book)
        elif choice == 2:
            contact_book.view_contact_list()
        elif choice == 3:
            keyword = input("Enter name or phone number to search: ")
            contacts = contact_book.search_contact(keyword)
            print("\nSearch Results:")
            for idx, contact in enumerate(contacts, start=1):
                print(f"{idx}. {contact.name} - {contact.phone}")
        elif choice == 4:
            try:
                contact_idx = int(input("Enter the contact number to update: "))
                new_contact = create_contact()
                contact_book.update_contact(contact_idx, new_contact)
            except (ValueError, IndexError):
                print("Invalid contact number.")
        elif choice == 5:
            try:
                contact_idx = int(input("Enter the contact number to delete: "))
                contact_book.delete_contact(contact_idx)
            except IndexError:
                print("Invalid contact number.")
        elif choice == 6:
            print("Exiting Contact Book...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


def create_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")

    return Contact(name, phone, email, address)


def add_new_contact(contact_book):
    new_contact = create_contact()
    contact_book.add_contact(new_contact)


if __name__ == "__main__":
    contact_book = ContactBook()
    display_menu(contact_book)
