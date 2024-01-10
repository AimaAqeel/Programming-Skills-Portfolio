# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 22:01:57 2024

@author: AimsMughal
"""

def process_payment(total_cost):
    payment_method = input("Choose payment method (cash/credit): ").lower()

    if payment_method == "cash":
        handle_cash_payment(total_cost)
    elif payment_method == "credit":
        handle_credit_payment()
    else:
        print("Invalid payment method. Please choose 'cash' or 'credit'.")

def handle_cash_payment(total_cost):
    inserted_money = float(input("Insert money: $"))

    if inserted_money == total_cost:
        print("Money inserted is correct. Products will be dispensed shortly!")
    elif inserted_money < total_cost:
        print("Money inserted is not enough!")
    else:
        change = inserted_money - total_cost
        print(f"Money inserted is more than enough! Products and change (${change:.2f}) will be dispensed shortly!")

def handle_credit_payment():
    credit_card_number = input("Enter credit card number: ")
    print(f"Payment successful with credit card ending in {credit_card_number[-4:]}. Products will be dispensed shortly!")

def display_products():
    print("\nProduct Price Code")
    print("Skittles      $2.50    1111")
    print("Flake         $2.00    2222")
    print("Dairy Milk    $2.00    3333")
    print("Hot Choculate $2.50    4444")
    print("Water         $1.00    5555")
    print("Chips         $1.25    1234")
    print("Coffee        $3.00    2345")
    print("latty         $2.75    3456")
    print("Candy Biscuit $1.00    4567")
    print("Tea           $2.50    5678")

def billing(selected_products):
    print("\nBilling Information:")
    print("{:<10} {:<15} {:<10} {:<10}".format("Code", "Product", "Quantity", "Price"))
    print("-" * 45)

    for product in selected_products:
        print("{:<10} {:<15} {:<10} ${:<10.2f}".format(
            product["code"], product["name"], product.get("quantity", 1), product["cost"]))

    print("\nTotal Cost: ${:.2f}".format(sum(product["cost"] * product.get("quantity", 1) for product in selected_products)))

def vending_machine():
    selected_products = []

    while True:
        print("Welcome to X's vending machine\n")
        display_products()

        # Ask the user to type a code
        print("\nType a product code to add to your cart (or type 'done' when finished):")

        # Use the input() function and save the response in a variable called user_input.
        user_input = input()

        if user_input.lower() == 'done':
            if not selected_products:
                print("No products selected. Exiting the vending machine.")
                break

            # Display billing information
            billing(selected_products)

            # Proceed to payment
            total_cost = sum(product["cost"] * product.get("quantity", 1) for product in selected_products)
            process_payment(total_cost)

            print("Thank you for your purchase!")
            break

        try:
            user_code = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid product code or 'done' to finish.")
            continue

        # Check the entered code and add the selected product to the cart
        if user_code in [1111, 2222, 3333, 4444, 5555, 1234, 2345, 3456, 4567, 5678]:
            selected_products.append({"code": user_code, "name": "Product {}".format(user_code), "cost": 2})  # Replace with the actual product details
            print(f"Product {user_code} added to your cart.")
        else:
            print("You have entered an invalid code. Please try again or type 'done' when finished.")

# Run the vending machine
vending_machine()
