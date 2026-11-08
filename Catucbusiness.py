items = [
    {"name": "Rice", "amount": 5000, "barcode": "12345678901"},
    {"name": "Oil", "amount": 2500, "barcode": "12345678902"},
    {"name": "Sugar", "amount": 1500, "barcode": "12345678903"},
    {"name": "Milk", "amount": 1200, "barcode": "12345678904"},
    {"name": "Bread", "amount": 500, "barcode": "12345678905"}
]

cart = []

print("\n========== CATUC POS SYSTEM ==========")
print("\n--- AVAILABLE ITEMS ---")

for product in items:
    print(
        f"Item: {product['name']} | "
        f"Barcode: {product['barcode']} | "
        f"Price: {product['amount']} FCFA"
    )

# Customer purchasing section
while True:
    customer_purchase = input(
        "\nEnter item name or barcode (or 'done' to finish): "
    ).strip()

    if customer_purchase.lower() == "done":
        break

    found = False

    for product in items:
        if (product["name"].lower() == customer_purchase.lower()
                or product["barcode"] == customer_purchase):

            found = True

            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Please enter a valid number.")
                break

            if quantity <= 0:
                print("Invalid quantity.")
                break

            total_price = product["amount"] * quantity

            cart.append({
                "name": product["name"],
                "quantity": quantity,
                "unit_price": product["amount"],
                "total_price": total_price
            })

            print(f"{product['name']} added successfully!")
            break

    if not found:
        print("Item not found in our list.")

# Generate receipt
if len(cart) == 0:
    print("\nNo items purchased.")

else:
    subtotal = sum(item["total_price"] for item in cart)

    discount = 0.0

    total_quantity = sum(item["quantity"] for item in cart)

    if subtotal > 10000:
        discount = 0.30
    elif total_quantity > 5 and subtotal > 4000:
        discount = 0.15
    elif subtotal > 5000:
        discount = 0.10

    discount_amount = subtotal * discount
    final_amount = subtotal - discount_amount

    print("\n" + "=" * 75)
    print("                  CATUC SALES RECEIPT")
    print("=" * 75)

    print(f"{'S/N':<5}{'Description':<15}"
          f"{'Quantity':<12}{'Unit Price':<18}{'Total Price':<15}")

    print("-" * 75)

    for sn, item in enumerate(cart, start=1):
        print(
            f"{sn:<5}"
            f"{item['name']:<15}"
            f"{item['quantity']:<12}"
            f"{item['unit_price']:<18,.2f}"
            f"{item['total_price']:<15,.2f}"
        )

    print("-" * 75)

    print(f"\nSubtotal:          {subtotal:,.2f} FCFA")
    print(f"Discount:          {discount * 100:.0f}%")
    print(f"Discount Amount:   {discount_amount:,.2f} FCFA")
    print(f"TOTAL EXPENDITURE: {final_amount:,.2f} FCFA")

    print("=" * 75)
    print("             THANK YOU FOR SHOPPING!")
    print("=" * 75)