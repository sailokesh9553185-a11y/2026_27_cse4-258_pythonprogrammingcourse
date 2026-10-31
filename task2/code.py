# Progressive Electricity Billing System

FIXED_CHARGE = 50
SURCHARGE_RATE = 0.05
REBATE = 20
INCREASE_LIMIT = 30

# Function to calculate electricity charges
def calculate_bill(units):

    energy_charge = 0

    # Progressive slab calculation
    if units <= 100:
        energy_charge = units * 2

    elif units <= 200:
        energy_charge = (100 * 2) + (units - 100) * 3

    elif units <= 300:
        energy_charge = (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        energy_charge = (
            (100 * 2) +
            (100 * 3) +
            (100 * 5) +
            (units - 300) * 7
        )

    # Fixed charge
    total = energy_charge + FIXED_CHARGE

    # Surcharge
    surcharge = energy_charge * SURCHARGE_RATE

    total += surcharge

    # Rebate
    rebate = 0

    if units < 100:
        rebate = REBATE
        total -= rebate

    return energy_charge, surcharge, rebate, total


# Main program
n = int(input("Enter number of months: "))

bills = []

for i in range(n):

    print("\nMonth", i + 1)

    units = float(input("Enter electricity units: "))

    if units < 0:
        print("Invalid units. Please enter a positive value.")
        continue

    energy, surcharge, rebate, total = calculate_bill(units)

    bills.append({
        "month": i + 1,
        "units": units,
        "energy": energy,
        "surcharge": surcharge,
        "rebate": rebate,
        "total": total
    })


# Display monthly bills
print("\n===== ELECTRICITY BILL DETAILS =====")

for bill in bills:

    print("\nMonth:", bill["month"])
    print("Units Consumed:", bill["units"])
    print("Energy Charges: Rs.", round(bill["energy"], 2))
    print("Fixed Charges: Rs.", FIXED_CHARGE)
    print("Surcharge: Rs.", round(bill["surcharge"], 2))
    print("Rebate: Rs.", bill["rebate"])
    print("Final Bill: Rs.", round(bill["total"], 2))


# Compare monthly bills
print("\n===== MONTHLY BILL COMPARISON =====")

for i in range(1, len(bills)):

    previous = bills[i - 1]["total"]
    current = bills[i]["total"]

    if previous > 0:
        increase = ((current - previous) / previous) * 100

        print("\nMonth", bills[i]["month"])
        print("Previous Bill: Rs.", round(previous, 2))
        print("Current Bill: Rs.", round(current, 2))
        print("Change:", round(increase, 2), "%")

        if increase > INCREASE_LIMIT:
            print("WARNING: Unusual increase detected!")
        else:
            print("Normal bill variation.")

    elif current > 0:
        print("\nMonth", bills[i]["month"])
        print("Increase cannot be calculated from a zero previous bill.")

print("\nProgram completed successfully.")
