# Big Sky Boards - Ingredient and Board Manager
# BMIS 365 Final Project - Sofia Ferraro

from inventory import load_ingredients, save_ingredients, view_ingredients, add_ingredient
from boards import load_orders, save_orders, record_order


# Prints all the menu options.
def show_menu():
    print("\n--- Big Sky Boards Menu ---")
    print("1. View ingredients")
    print("2. Add or restock an ingredient")
    print("3. View suppliers")
    print("4. View board menu")
    print("5. Record a pre-order")
    print("6. Show expiring and low-stock alerts")
    print("7. Remove expired items")
    print("8. Report with charts")
    print("9. Run 30-day simulation")
    print("10. Save and exit")


# Load saved data when the program starts.
ingredients = load_ingredients()
orders = load_orders()

# Menu options that are not built yet.
coming_soon = ["3", "4", "6", "7", "8", "9"]
running = True

# Shows the menu and runs the user's choice until they pick Save and exit.
while running:
    show_menu()
    choice = input("Choose an option (1-10): ")

    if choice == "1":
        view_ingredients(ingredients)
    elif choice == "2":
        add_ingredient(ingredients)
    elif choice == "5":
        record_order(ingredients, orders)
    elif choice in coming_soon:
        print("Coming soon!")
    elif choice == "10":
        save_ingredients(ingredients)
        save_orders(orders)
        print("Data saved. Goodbye!")
        running = False
    else:
        print("Menu option not available. Please enter a number from 1 to 10.")
