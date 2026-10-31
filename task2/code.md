### Progressive Electricity Billing System Using Python

### 1\. Problem Statement

The Progressive Electricity Billing System is designed to calculate household electricity bills based on monthly electricity consumption using a slab-based tariff system.

The system calculates the electricity bill by considering the following factors:

* Consumption Slabs: Different electricity rates are applied to different units of consumption.

* Fixed Charges: A fixed amount is added to every monthly bill.

* Surcharge: An additional percentage is charged on the energy cost.

* Rebate: A discount is provided when electricity consumption is below a specified limit.

* Monthly Comparison: Bills are compared across several months.

* Unusual Increase Detection: The system identifies months where the bill increases by more than 30% compared with the previous month.

### Electricity Tariff Slabs Used

| Consumption     | Rate per unit |
| --------------- | ------------- |
| 0–100 units     | ₹2            |
| 101–200 units   | ₹3            |
| 201–300 units   | ₹5            |
| Above 300 units | ₹7            |

Additional charges:

* Fixed charge = ₹50

* Surcharge = 5% of energy charges

* Rebate = ₹20 if consumption is below 100 units

* Unusual increase = More than 30% compared with the previous month's bill.

### 2\. Algorithm

Step 1: Start the program.

Step 2: Enter the number of months.

Step 3: Enter electricity consumption in units for each month.

Step 4: Calculate energy charges using progressive slabs.

Step 5: Add fixed charges to the energy charges.

Step 6: Calculate a 5% surcharge.

Step 7: Check rebate eligibility.

* If consumption is below 100 units, subtract ₹20.

* Otherwise, no rebate.

Step 8: Calculate the final electricity bill.

Step 9: Store monthly bills.

Step 10: Compare each month's bill with the previous month's bill.

Step 11: If the increase is greater than 30%, identify it as an unusual increase.

Step 12: Display monthly bills and unusual increases.

Step 13: Stop the program.

### 3\. Flowchart
flowchart TD
    A([Start]) --> B[/Enter number of months/]
    B --> C[/Enter electricity units/]
    C --> D{Units >= 0?}
    D -- No --> E[Display invalid input]
    E --> C
    D -- Yes --> F[Calculate progressive slab charges]
    F --> G[Add fixed charges]
    G --> H[Calculate surcharge]
    H --> I{Units < 100?}
    I -- Yes --> J[Apply rebate]
    I -- No --> K[No rebate]
    J --> L[Calculate final bill]
    K --> L
    L --> M[Store monthly bill]
    M --> N{More months?}
    N -- Yes --> C
    N -- No --> O[Display monthly bills]
    O --> P[Compare consecutive bills]
    P --> Q{Increase > 30%?}
    Q -- Yes --> R[Display unusual increase warning]
    Q -- No --> S[Display normal bill variation]
    R --> T[Display comparison results]
    S --> T
    T --> U([Stop])

### 4\. Python Source Code

python

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
        print("Invalid units. Please enter a positive value.…
