# Retail Billing with Multiple Discount Rules

print("===== RETAIL BILLING SYSTEM =====")

n = int(input("Enter number of products: "))

items = []
subtotal = 0
total_tax = 0

for i in range(n):

    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))
    category = input("Enter category (food/clothing/electronics): ").lower()

    amount = price * quantity

    # Category-specific tax
    if category == "food":
        tax_rate = 5
    elif category == "clothing":
        tax_rate = 5
    elif category == "electronics":
        tax_rate = 18
    else:
        tax_rate = 12

    tax = amount * tax_rate / 100

    items.append((name, quantity, price, amount,
                  tax_rate, tax))

    subtotal += amount
    total_tax += tax

# Threshold-based discount
if subtotal >= 5000:
    discount_rate = 20
elif subtotal >= 3000:
    discount_rate = 15
elif subtotal >= 1000:
    discount_rate = 10
else:
    discount_rate = 0

discount = subtotal * discount_rate / 100

# Maximum concession limit
max_discount = 1000

if discount > max_discount:
    discount = max_discount

# Final bill calculation
final_amount = subtotal + total_tax - discount

# Display invoice
print("\n========== ITEMIZED INVOICE ==========")

print("Product\tQty\tPrice\tAmount\tTax")

for item in items:
    print(item[0], "\t", item[1], "\t",
          item[2], "\t", item[3], "\t",
          str(item[4]) + "%")

print("--------------------------------------")
print("Subtotal: Rs.", round(subtotal, 2))
print("Total Tax: Rs.", round(total_tax, 2))
print("Discount Rate:", discount_rate, "%")
print("Discount Amount: Rs.", round(discount, 2))
print("Maximum Discount: Rs.", max_discount)
print("--------------------------------------")
print("Final Amount: Rs.", round(final_amount, 2))
print("======================================")
print("Thank You! Visit Again.")
