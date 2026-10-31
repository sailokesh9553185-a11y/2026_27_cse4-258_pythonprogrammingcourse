# Multi-Currency Travel Budget Analysis

print("===== TRAVEL BUDGET ANALYSIS =====")

# Input base currency and budget
base_currency = input("Enter base currency (e.g. INR): ").upper()

budget = float(input("Enter planned travel budget: "))

n = int(input("Enter number of expense categories: "))

expenses = []
total_expense = 0

for i in range(n):

    print("\nExpense Category", i + 1)

    category = input("Enter category name: ")

    amount = float(input("Enter expense amount: "))

    currency = input("Enter currency code: ").upper()

    rate = float(input("Enter exchange rate: "))

    fee_percent = float(input("Enter conversion fee (%): "))

    # Currency conversion
    converted_amount = amount * rate

    # Calculate conversion fee
    conversion_fee = converted_amount * fee_percent / 100

    # Calculate final expense
    final_amount = converted_amount + conversion_fee

    expenses.append((category, converted_amount,
                     conversion_fee, final_amount))

    total_expense += final_amount

# Identify largest expense category
largest_expense = max(expenses, key=lambda x: x[3])

# Calculate remaining budget
balance = budget - total_expense

# Display report
print("\n===== TRAVEL EXPENSE REPORT =====")

print("Base Currency:", base_currency)

for item in expenses:
    print("\nCategory:", item[0])
    print("Converted Amount:", round(item[1], 2))
    print("Conversion Fee:", round(item[2], 2))
    print("Total Expense:", round(item[3], 2),
          base_currency)

print("\n--------------------------------")
print("Total Travel Expense:",
      round(total_expense, 2), base_currency)

print("Largest Expense Category:",
      largest_expense[0])

print("Largest Expense Amount:",
      round(largest_expense[3], 2), base_currency)

print("Planned Budget:",
      round(budget, 2), base_currency)

if total_expense <= budget:
    print("Budget Status: WITHIN BUDGET")
    print("Remaining Budget:", round(balance, 2),
          base_currency)
else:
    print("Budget Status: BUDGET EXCEEDED")
    print("Extra Amount:", round(abs(balance), 2),
          base_currency)

print("================================")
