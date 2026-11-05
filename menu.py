# Big Sky Boards - Ingredient and Board Manager
# BMIS 365 Final Project - Sofia Ferraro


def show_menu(): #function to display the menu options
    print("\n--- Big Sky Boards Menu ---")
    print("1. View Ingredients")
    print("2. Add or restock an ingredient")
    print("3. View suppliers")
    print("4. View board menu")
    print("5. Record a pre-order")
    print("6. Show expiring and low-stock alerts")
    print("7. Remove expired items")
    print("8. Report with charts")
    print("9. Run 30-day simulation")
    print("10. Save and exit")

choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
running = True

while running: #while loop to keep the menu running until the user chooses to exit
    show_menu()
    choice = input("Choose an Option (1-10): ")

    if choice in choices:
        print("Coming Soon!")
    elif choice == "10":
        print("Closing Menu! Goodbye!")
        running = False
    else:
        print("Menu option not available. Please enter a number from 1 to 10.")
