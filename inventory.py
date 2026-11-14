# inventory.py - loads, saves, shows, and updates the ingredients


# Reads ingredients.csv into a dictionary and converts the numbers from strings.
def load_ingredients():
    ingredients = {}
    file = open("ingredients.csv", "r")
    file.readline()  # skip the header row
    for line in file:
        parts = line.strip().split(",")
        ingredients[parts[0]] = {"cost": float(parts[1]), "qty": int(parts[2]),
                                 "expires": parts[3], "reorder": int(parts[4])}
    file.close()
    return ingredients


# Writes the ingredients dictionary back to ingredients.csv.
def save_ingredients(ingredients):
    file = open("ingredients.csv", "w")
    file.write("item,cost,qty,expires,reorder\n")
    for item in ingredients:
        details = ingredients[item]
        file.write(item + "," + str(details["cost"]) + "," + str(details["qty"]) + "," +
                   details["expires"] + "," + str(details["reorder"]) + "\n")
    file.close()


# Prints every ingredient with its cost, quantity, expiration date, and reorder level.
def view_ingredients(ingredients):
    print("\n--- Ingredients ---")
    for item in ingredients:
        details = ingredients[item]
        print(item, "| cost: $", details["cost"], "| quantity:", details["qty"],
              "| expiration date:", details["expires"], "| reorder at:", details["reorder"])


# Asks for a whole number and keeps asking until the user types one.
def get_whole_number(prompt):
    while True:
        answer = input(prompt)
        if answer.isdigit():
            return int(answer)
        print("Please enter a whole number, like 12.")


# Asks for a price and keeps asking until the user types a valid number, like 0.75.
def get_price(prompt):
    while True:
        answer = input(prompt)
        try:
            price = float(answer)
            if price >= 0:
                return price
            print("Price can't be negative.")
        except ValueError:
            print("Please enter a number, like 0.75.")


# Restocks an ingredient if it already exists.
# If it is new, asks for its details and adds it to the dictionary.
def add_ingredient(ingredients):
    item = input("Ingredient name: ").lower()
    if item == "" or "," in item:
        print("Ingredient name can't be blank or contain a comma.")
    elif item in ingredients:
        amount = get_whole_number("How many to add? ")
        ingredients[item]["qty"] = ingredients[item]["qty"] + amount
        ingredients[item]["expires"] = input("New expiration date (YYYY-MM-DD): ")
        print("Restocked", item, "- new quantity:", ingredients[item]["qty"])
    else:
        cost = get_price("Cost per unit: $")
        qty = get_whole_number("Quantity: ")
        expires = input("Expiration date (YYYY-MM-DD): ")
        reorder = get_whole_number("Reorder level: ")
        ingredients[item] = {"cost": cost, "qty": qty, "expires": expires, "reorder": reorder}
        print("Added", item)
