contacts= {}

while True:
    print("\n_______CONTACT BOOK_______")
    print("1. Create contact")
    print("2. View contact")
    print("3. Search a contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Quit")

    choice= input("Enter your choice: ")

    if choice== "1":
        name= input("Enter your name: ")
        if name in contacts:
            print("Contact name {name} already exists")
        else:
            address= input("Enter address: ")
            mobile= int(input("Enter mobile number: "))
            email= input("Enter e-mail address: ")
            contacts[name]= {'address': address, 'mobile': mobile, 'email': email}
            print(f"Contact {name} has been successfully created")

    elif choice== "2":
        if contacts:
            print("Contact list: ")
            for name, contact in contacts.items():
                print(f"Name: {name}, Mobile Number: {mobile}")
        else:
            print("Contact not found")

    elif choice== "3":
        search= input("Enter the contact you want to search: ")
        a= False
        for name, contact in contacts.items():
            if search.lower() in name.lower():
                print(f"Name: {name}, Address: {address}, Mobile number: {mobile}, E-mail: {email}")
                a= True
        if not a:
            print("Not found")

    elif choice== "4":
        name= input("Enter the contact you want to update: ")
        if name in contacts: 
            address= input("Enter updated address: ")
            mobile= int(input("Enter updated mobile number: "))
            email= input("Enter updated e-mail: ")
            contacts[name]= {'address': address, 'mobile': mobile, 'email': email}
        else:
            print("Contact not found")

    elif choice== "5":
        name= input("Enter contact you want to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} has been deleted successfully")
        else:
            print("Contact not found")

    elif choice== "6":
        print("Exiting the Contact Book")
        break

    else:
        print("Invalid input")