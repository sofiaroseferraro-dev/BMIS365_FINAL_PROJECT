# boards.py - board recipes and pre-orders

from inventory import get_whole_number

# How much of each ingredient one board uses.
boards = {
    "basic":  {"salami": 3, "brie": 2, "crackers": 7, "grapes": 6},
    "medium": {"salami": 6, "prosciutto": 3, "brie": 4, "crackers": 10, "grapes": 9},
    "deluxe": {"salami": 9, "prosciutto": 6, "brie": 6, "crackers": 13, "grapes": 12}
}

# Price of each board.
board_prices = {"basic": 35.00, "medium": 55.00, "deluxe": 85.00}


# Reads orders.csv into a list of dictionaries and converts the numbers from strings.
def load_orders():
    orders = []
    file = open("orders.csv", "r")
    file.readline()  # skip the header row
    for line in file:
        parts = line.strip().split(",")
        orders.append({"pickup": parts[0], "customer": parts[1], "board": parts[2],
                       "qty": int(parts[3]), "total": float(parts[4])})
    file.close()
    return orders


# Writes the orders list back to orders.csv.
def save_orders(orders):
    file = open("orders.csv", "w")
    file.write("pickup,customer,board,qty,total\n")
    for order in orders:
        file.write(order["pickup"] + "," + order["customer"] + "," + order["board"] + "," +
                   str(order["qty"]) + "," + str(order["total"]) + "\n")
    file.close()


# Records a pre-order: checks the details and stock, subtracts the ingredients,
# and adds the order to the orders list.
def record_order(ingredients, orders):
    customer = input("Customer name: ")
    pickup = input("Pickup date (YYYY-MM-DD): ")
    print("Boards: basic ($35), medium ($55), deluxe ($85)")
    board = input("Board: ").lower()
    count = get_whole_number("How many boards? ")

    if customer == "" or pickup == "" or "," in customer:
        print("Name and date can't be blank, and the name can't contain a comma.")
    elif board not in boards:
        print("Sorry, that board is not on the menu.")
    elif count == 0:
        print("Order must be for at least 1 board.")
    else:
        # Check every ingredient first so a failed order doesn't change any stock.
        enough = True
        for item in boards[board]:
            needed = boards[board][item] * count
            if ingredients[item]["qty"] < needed:
                print("Not enough", item, "- need", needed, "but only have", ingredients[item]["qty"])
                enough = False

        if enough:
            for item in boards[board]:
                ingredients[item]["qty"] = ingredients[item]["qty"] - boards[board][item] * count
            total = board_prices[board] * count
            orders.append({"pickup": pickup, "customer": customer, "board": board,
                           "qty": count, "total": total})
            print("Order recorded for", customer, "- total: $", total)
        else:
            print("Order not recorded. Restock first.")
