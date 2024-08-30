def display_menu(menu):
    print("Welcome to Moon Restaurant")
    print("Below is our menu card. Have a look!")
    for item, price in menu.items():
        print(f"{item}: Rs{price}")

def get_order(menu):
    order_total = 0
    while True:
        item = input("Please enter the name of the item you want to order: ").capitalize()
        if item in menu:
            while True:
                try:
                    quantity = int(input(f"How many {item}(s) would you like to order? "))
                    if quantity > 0:
                        break
                    else:
                        print("Please enter a positive number.")
                except ValueError:
                    print("Please enter a valid number.")
            order_total += menu[item] * quantity
            print(f"{quantity} x {item}(s) have been added to your order.")
        else:
            print(f"Sorry, the item {item} is not available.")

        another_order = input("Do you want to add another item? (Yes/No thanks) ").strip().lower()
        if another_order == 'no thanks':
            break
    return order_total

def main():
    menu = {
        'Pizza': 40,
        'Pasta': 50,
        'Salad': 70,
        'Soup': 80,
        'Dessert': 100,
        'Coffee': 140,
    }

    display_menu(menu)
    order_total = get_order(menu)
    print(f"\nThe total amount to pay is Rs{order_total}")
    print("Thank you for ordering! Enjoy your meal.")

if __name__ == "__main__":
    main()
