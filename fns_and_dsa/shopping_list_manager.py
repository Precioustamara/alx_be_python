def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Prompt for and add an item
            item = input('Enter the item to add: ')
            item_name = item.lower()
            if item_name in shopping_list:
                print (f"{item} already exist")
                add = input("Would you like to keep it? (Y/N) ").lower()
                if add == 'y':
                  shopping_list.append(item_name)
            else:
             exit
            shopping_list.append(item_name)
        elif choice == 2:
            # Prompt for and remove an item
           item = input('Enter the item to remove: ')
           if item not in shopping_list:
            print("item does not exist")
           else:
            shopping_list.remove(item)
           print(f"{item} has been removed")
        elif choice == 3:
           if not shopping_list:
                    print("The list is empty")
           else:
                    print("\nShopping list")
                    for index, item in enumerate(shopping_list, start=1):
                        print(f"{index}. {item.capitalize()}")
                        print("Goodbye!")
                        break
        else:
                print("Invalid choice. Please try again.") 

if __name__ == "__main__":
    main()