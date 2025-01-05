contacts=[]

def add_contact():
    name=input("Enter Name: ")
    phone=input("Enter PhoneNo: ")
    email=input("Enter EmailID: ")
    address=input("Enter Address: ")
    contacts.append({"name":name, "phone":phone, "email":email, "address":address})
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    print("Contact List:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    print()

def search_contact():
    query=input("Enter name or phone to search: ")
    found=False
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            found=True
    if not found:
        print("No contacts found.")
    print()

while True:
    print("Contact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")
    choice=int(input("Choose an option: "))
    if choice==1:
        add_contact()
    elif choice==2:
        view_contacts()
    elif choice==3:
        search_contact()
    elif choice==4:
        print("Exiting Contact Book!")
        break
    else:
        print("Invalid option. Try again.")
