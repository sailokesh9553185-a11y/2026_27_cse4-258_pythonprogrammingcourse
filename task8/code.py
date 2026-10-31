# Manufacturing Cost and Profitability Analysis

print("===== MANUFACTURING COST ANALYSIS =====")

# Input details
product = input("Enter product name: ")
quantity = int(input("Enter production quantity: "))

material_cost = float(input("Enter material cost per unit: "))
labour_cost = float(input("Enter labour cost per unit: "))
wastage_percent = float(input("Enter wastage percentage: "))
machine_cost = float(input("Enter machine cost per unit: "))
selling_price = float(input("Enter selling price per unit: "))
profit_target = float(input("Enter target profit percentage: "))

# Calculate material cost
total_material = material_cost * quantity

# Calculate wastage cost
wastage_cost = total_material * wastage_percent / 100

# Calculate labour cost
total_labour = labour_cost * quantity

# Calculate machine cost
total_machine = machine_cost * quantity

# Calculate total production cost
total_cost = (
    total_material +
    wastage_cost +
    total_labour +
    total_machine
)

# Calculate sales revenue
revenue = selling_price * quantity

# Calculate profit
profit = revenue - total_cost

# Calculate profit percentage
if total_cost > 0:
    profit_percent = (profit / total_cost) * 100
else:
    profit_percent = 0

# Display report
print("\n===== MANUFACTURING REPORT =====")

print("Product Name:", product)
print("Production Quantity:", quantity)

print("\n----- COST DETAILS -----")
print("Material Cost: Rs.", round(total_material, 2))
print("Wastage Cost: Rs.", round(wastage_cost, 2))
print("Labour Cost: Rs.", round(total_labour, 2))
print("Machine Cost: Rs.", round(total_machine, 2))

print("\nTotal Production Cost: Rs.", round(total_cost, 2))
print("Total Sales Revenue: Rs.", round(revenue, 2))
print("Total Profit: Rs.", round(profit, 2))
print("Profit Percentage:", round(profit_percent, 2), "%")

# Check profit target
print("\n----- PROFITABILITY STATUS -----")

if profit_percent >= profit_target:
    print("Target Profit Percentage:", profit_target, "%")
    print("Status: PROFIT TARGET ACHIEVED")
else:
    print("Target Profit Percentage:", profit_target, "%")
    print("Status: PROFIT TARGET NOT ACHIEVED")

print("===============================")
