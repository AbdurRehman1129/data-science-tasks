contact = {}
def main_menu():
    menu = print("""
MENU:
Enter 1 to add new contact.
Enter 2 to view all contact.
Enter 3 to search contact by name.
Enter 4 to remove contact.
Enter 5 to exit.""")

def add_contact():
    while True:
        if len(contact) == 0:
            con = input("Do you want to add contact (Y,N) : ").upper()
        else:
            con = input("Do you want to add more contacts (Y,N) : ").upper()
        if con == "Y":
            while True:
                name = input("Enter name : ").upper()
                if name == "":
                    input("Name can't be empty. Press Enter to try again: ")
                else:
                    break
            while True:
                num = input("Enter number : ")
                if num == "":
                    input("Number can't be empty. Press Enter to try again: ")
                else:
                    break
            while True:
                email = input("Enter email address : ")
                if email == "":
                    input("Email can't be empty. Press Enter to try again: ")
                else:
                    break
            contact[name] = [num, email]
            print(f"\nContact {name} saved successfully.")
        elif con == "N":
            break
        else:
            input("\nInvalid Input. Press enter to try again : ")

def display_contact():
    i = 1
    if len(contact) == 0:
        input("\nYour have no contact. Press enter to continue: ")

    else:
        for name, detail in contact.items():
            print(f"{i}. Name: {name}, Phone Number: {
                  detail[0]}, Email Address: {detail[1]}")
            i += 1
        input("\nPress Enter to continue: ")

def search_name():
    while True:
        if len(contact) == 0:
            input("\nYour have no contact. Press enter to continue: ")
            break
        else:
            search = input("\nEnter name to search: ").upper()
        if search in contact:
            print(f"Name : {search}, Phone Number: {
                  contact[search][0]}, Email: {contact[search][1]}")
            input("\nPress Enter to continue: ")
            break
        else:
            input("\nNot Found. Press Enter to try again: ")

def remove_name():
    while True:
        if len(contact) == 0:
            input("\nYour have no contact. Press enter to continue: ")
            break
        else:
            search = input("\nEnter name to remove: ").upper()
            if search in contact:
                contact.pop(search)
                print(f"\nContact {search} removed successfully.")
                display_contact()
                break
            else:
                input("\nNot Found. Press Enter to try again: ")

while True:
    main_menu()
    user_input = input("\nEnter your choice (1,2,3,4,5) : ")
    if user_input == "1":
        add_contact()
    elif user_input == "2":
        display_contact()
    elif user_input == "3":
        search_name()
    elif user_input == "4":
        remove_name()
    elif user_input == "5":
        break
    else:
        input("\nInvalid input. Press enter to try again: ")