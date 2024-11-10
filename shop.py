item = []
quantity = []

def display_menu():
    menu = print("""
MENU:
Enter 1 to add items in shopping list.
Enter 2 to display items.
Enter 3 to remove item.
Enter 4 to update quantity of item.
Enter 5 to exit.
 """)

def add_item():
    add_new = ""
    while True:
        if len(item) == 0:
            add_new = input("Do you want to add item (Y, N) : ").upper()
        else:
            add_new = input(
                "\nDo you want to add more items (Y, N) : ").upper()
        if add_new == "Y":
            new_item = input("Enter item name: ").capitalize()
            if new_item in item:
                print("Item already exist, please modify quantity from main menu.")
            else:
                item.append(new_item)
                while True:
                    item_quantity = int(input("Enter item quantity in KG: "))
                    if item_quantity > 0:
                        quantity.append(item_quantity)
                        break
                    else:
                        print("\nWeight can't be zero or negative.")
        elif add_new == "N":
            break
        elif add_new != "Y" or add_new != "N":
            print("Invalid Input")

def rem_item():
    if len(item) == 0 and len(quantity) == 0:
        print("No item in your shopping list.")
        cont = input("\nPress Enter to continue : ")
    else:
        while True:
            remove_item = int(
                input("Which item you want to remove. Enter number: "))
            if remove_item-1 < len(item) and remove_item > 0:
                item.remove(item[remove_item-1])
                quantity.remove(quantity[remove_item-1])
                print(f"\nItem no {
                      remove_item} removed. Now your shopping list has:")
                display_item()
                break
            else:
                print(f"\nInvalid Input. No item at number {remove_item}")

def display_item():
    if len(item) == 0 and len(quantity) == 0:
        print("No item in your shopping list.")
    else:
        i = 0
        for item_name, weight in zip(item, quantity):
            print(f"{i+1}. {item_name} : {weight} KG")
            i += 1
    cont = input("\nPress Enter to continue : ")

def update_quantity():
    if len(item) == 0 and len(quantity) == 0:
        print("No item in your shopping list.")
    else:
        while True:
            new_quantity = int(
                input("Which item's quantity you want to increase? Enter number: "))
            if new_quantity-1 < len(quantity) and new_quantity > 0:
                while True:
                    new_weight = int(
                        input("Enter item's new quantity in KG: "))
                    if new_weight > 0:
                        quantity[new_quantity-1] = new_weight
                        print(f"\nItem no {
                              new_quantity} updated. Now your shopping list has:")
                        display_item()
                        break
                    else:
                        print("\nWeight can't be zero or negative.")
                break
            else:
                print(f"\nInvalid Input. No item at number {new_quantity}")

while True:
    display_menu()
    menu_option = input("Enter your choice (1,2,3,4,5) : ")
    if menu_option == "1":
        add_item()
    elif menu_option == "2":
        display_item()
    elif menu_option == "3":
        rem_item()
    elif menu_option == "4":
        update_quantity()
    elif menu_option == "5":
        break
    else:
        print("Invalid Input")
        cont = input("Press Enter to continue : ")
