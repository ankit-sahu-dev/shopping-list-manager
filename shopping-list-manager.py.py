shopping_list = []

print("/////////////////////////")
print("WELCOME TO THE SHOPPING LIST MANAGER")
print("/////////////////////////")

choice = 0

while choice != 6:
    print("1. Add items")
    print("2. View items")
    print("3. Remove items")
    print("4. Count items")
    print("5. Search item")
    print("6. Exit")
    
    
    choice = int(input("Enter your choice(1-6): "))
    print("You selected:", choice)
    
    if choice == 1:
        print("Add item selected")
        
        item = input("Enter item name: ")
        shopping_list.append(item)
    
    elif choice == 2:
        print(shopping_list)
        
    elif choice == 3:
        item2 = input("Enter item name: ")
        shopping_list.remove(item2)
        print(item2,"removed successfully")
    
    elif choice == 4:
        print(len(shopping_list))
        
    elif choice == 5:
        item3 = input("Enter item name: ")
        if item3 in shopping_list:
            print("Item found")
        else:
            print("Item not found")
            
    elif choice == 6:
        print("THANK YOU FOR USING SHOPPING LIST")
        break
    
    else:
        print("Invalid choice")


