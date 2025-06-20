# Define menu function
def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Define the main logic
def main():
    shopping_list = []  # <-- This is your array

    while True:
        display_menu()  # <-- Calling display_menu
        try:
            choice = int(input("Enter your choice: "))  # <-- Choice input as number
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' added.")
        elif choice == 2:
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed.")
            else:
                print("Item not found.")
        elif choice == 3:
            if shopping_list:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Only runs main if this file is executed directly
if __name__ == "__main__":
    main()
