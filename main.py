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

def view_ingredients(): #function to display the ingredients and their details
    print("\n--- Ingredients ---")
    for item in ingredients:
        details = ingredients[item]
        print(item, "| cost: $", details["cost"], "| quantity:", details["qty"], "| expiration date:", details["expires"], "| supplier:", details["supplier"], "| reorder at:", details["reorder"])

# Ingredients: salami and prosciutto in slices, brie in oz, grapes each.
ingredients = {
    "salami":     {"cost": 0.25, "qty": 120, "expires": "2026-11-20", "reorder": 30},
    "prosciutto": {"cost": 0.60, "qty": 48,  "expires": "2026-11-12", "reorder": 12},
    "brie":       {"cost": 0.75, "qty": 40,  "expires": "2026-11-09", "reorder": 16},
    "grapes":     {"cost": 0.05, "qty": 150, "expires": "2026-11-06", "reorder": 40}
    "crackers":   {"cost": 0.10, "qty": 200, "expires": "2026-11-30", "reorder": 50}

}
choices = ["2", "3", "4", "5", "6", "7", "8", "9"]
running = True

while running: #while loop to keep the menu running until the user chooses to exit
    show_menu()
    choice = input("Choose an Option (1-10): ")

    if choice in choices:
        print("Coming Soon!")
    if choice == "1":
        view_ingredients()
    elif choice == "10":
        print("Closing Menu! Goodbye!")
        running = False
    else:
        print("Menu option not available. Please enter a number from 1 to 10.")

