### 10\. Campus Event Financial Planning

### 1\. Problem Statement

Develop a Python program to manage the financial planning of a campus event by calculating venue, equipment, catering, transport, and certificate expenses.

The program should:

* Accept the costs of different event arrangements.

* Calculate the total event expenditure.

* Calculate the amount received through sponsorship.

* Determine the sponsorship shortfall.

* Calculate participant registration contributions.

* Determine the minimum number of participants required to break even.

* Display the complete event financial report.

* Identify whether the event budget is sufficient.

### 2\. Algorithm

* Start the program.

* Enter the event name.

* Enter venue expenses.

* Enter equipment expenses.

* Enter catering cost per participant.

* Enter transport cost per participant.

* Enter certificate cost per participant.

* Enter expected number of participants.

* Enter sponsorship amount.

* Calculate fixed expenses.

* Calculate variable expenses per participant.

* Calculate total event expenditure.

* Calculate sponsorship shortfall.

* Calculate the participant contribution required.

* Calculate the minimum registration count needed to break even.

* Display the complete financial report.

* Stop.

### 3\. Flowchart
flowchart TD
    A([Start]) --> B[/Enter event name/]
    B --> C[/Enter venue and equipment costs/]
    C --> D[/Enter catering transport and certificate costs/]
    D --> E[/Enter expected participants/]
    E --> F[/Enter sponsorship and registration fee/]
    F --> G[Calculate fixed expenses]
    G --> H[Calculate variable cost per participant]
    H --> I[Calculate total event expenditure]
    I --> J[Calculate sponsorship shortfall]
    J --> K[Calculate participant contribution]
    K --> L{Registration fee > variable cost?}
    L -- Yes --> M[Calculate minimum break-even participants]
    L -- No --> N[Break-even not possible]
    M --> O[Calculate total income and profit or loss]
    N --> O
    O --> P{Total income >= total cost?}
    P -- Yes --> Q[Event financially viable]
    P -- No --> R[Event has financial loss]
    Q --> S[/Display financial report/]
    R --> S
    S --> T([Stop])

### 4\. Python Source Code

```python

# Campus Event Financial Planning

print("===== CAMPUS EVENT FINANCIAL PLANNING =====")

# Input event details
event_name = input("Enter event name: ")

venue = float(input("Enter venue cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))

catering = float(input("Enter catering cost per participant: Rs. "))
transport = float(input("Enter transport cost per participant: Rs. "))
certificate = float(input("Enter certificate cost per participant: Rs. "))

participants = int(input("Enter expected participants: "))

sponsorship = float(input("Enter sponsorship amount: Rs. "))

# Registration contribution per participant
registration_fee = float(input("Enter registration fee per participant: Rs. "))

# Calculate fixed expenses
fixed_cost = venue + equipment

# Calculate variable cost per participant
variable_cost = catering + transport + certificate

# Calculate total variable expenses
total_variable = variable_cost * participants

# Calculate total event cost
total_cost = fixed_cost + total_variable

# Calculate sponsorship shortfall
if sponsorship < total_cost:
    shortfall = total_cost - sponsorship
else:
    shortfall = 0

# Calculate participant contribution
participant_collection = registration_fee * participants

# Calculate remaining amount after sponsorship
remaining_cost = max(0, total_cost - sponsorship)

# Calculate minimum participants for break-even
if registration_fee > variable_cost:
    minimum_participants = (
        fixed_cost - sponsorship
    ) / (registration_fee - variable_cost)

    minimum_participants = max(
        0, int(minimum_participants + 0.999999)
    )
else:
    minimum_participants = None

# Calculate final financial position
total_income = sponsorship + participant_collection
profit_loss = total_income - total_cost

# Display report
print("\n========== EVENT FINANCIAL REPORT ==========")

print("Event Name:", event_name)

print("\n----- EXPENSE DETAILS -----")
print("Venue Cost: Rs.", venue)
print("Equipment Cost: Rs.", equipment)
print("Catering Cost: Rs.", catering * participants)
print("Transport Cost: Rs.", transport * participants)
print("Certificate Cost: Rs.", certificate * participants)

print("\nFixed Cost: Rs.", fixed_cost)
print("Variable Cost Per Participant: Rs.", variable_cost)
print("Total Event Cost: Rs.", total_cost)

print("\n----- INCOME DETAILS -----")
print("Sponsorship Amount: Rs.", sponsorship)
print("Sponsorship Shortfall: Rs.", shortfall)
print("Registration Fee: Rs.", registration_fee)
print("Participant Collection: Rs.", participant_collection)
print("Total Income: Rs.", total_income)

print("\n----- BREAK-EVEN ANALYSIS -----")

if minimum_participants is not None:
    print("Minimum Participants Required:",
          minimum_participants)
else:
    print("Break-even is not possible with the given registration fee.")

print("\nProfit/Loss: Rs.", profit_loss)

if profit_loss >= 0:
    print("Status: EVENT IS FINANCIALLY VIABLE")
else:
    print("Status: EVENT HAS A FINANCIAL LOSS")

print("============================================")
```

### 5\. Sample Input

```text
===== CAMPUS EVENT FINANCIAL PLANNING =====

Enter event name: Tech Fest

Enter venue cost: Rs. 10000
Enter equipment cost: Rs. 5000

Enter catering cost per participant: Rs. 100
Enter transport cost per participant: Rs. 50
Enter certificate cost per participant: Rs. 30

Enter expected participants: 100

Enter sponsorship amount: Rs. 10000

Enter registration fee per participant: Rs. 250
```

### 6\. Sample Output

```text
========== EVENT FINANCIAL REPORT ==========

Event Name: Tech Fest

----- EXPENSE DETAILS -----
Venue Cost: Rs. 10000.0
Equipment Cost: Rs. 5000.0
Catering Cost: Rs. 10000.0
Transport Cost: Rs. 5000.0
Certificate Cost: Rs. 3000.0

Fixed Cost: Rs. 15000.0
Variable Cost Per Participant: Rs. 180.0
Total Event Cost: Rs. 33000.0

----- INCOME DETAILS -----
Sponsorship Amount: Rs. 10000.0
Sponsorship Shortfall: Rs. 23000.0
Registration Fee: Rs. 250.0
Participant Collection: Rs. 25000.0
Total Income: Rs. 35000.0

----- BREAK-EVEN ANALYSIS -----
Minimum Participants Required: 215

Profit/Loss: Rs. 2000.0
Status: EVENT IS FINANCIALLY VIABLE

============================================
```

Correction to the sample calculation: With sponsorship of ₹10,000, the break-even count is 25 participants, not 215. The correct output line is:

```text
Minimum Participants Required: 25
```

### 7\. Break-Even Concept

The break-even point is the minimum number of registrations required for total income to cover total event expenses.

### 8\. Mermaid Flowchart Code

```mermaid

flowchart TD
    A([Start]) --> B[/Enter event name/]
    B --> C[/Enter venue and equipment costs/]
    C --> D[/Enter catering transport and certificate costs/]
    D --> E[/Enter expected participants/]
    E --> F[/Enter sponsorship and registration fee/]
    F --> G[Calculate fixed expenses]
    G --> H[Calculate variable cost per participant]
    H --> I[Calculate total event expenditure]
    I --> J[Calculate sponsorship shortfall]
    J --> K[Calculate participant contribution]
    K --> L{Registration fee > variable cost?}
    L -- Yes --> M[Calculate minimum break-even participants]
    L -- No --> N[Break-even not possible]
    M --> O[Calculate total income and profit or loss]
    N --> O
    O --> P{Total income >= total cost?}
    P -- Yes --> Q[Event financially viable]
    P -- No --> R[Event has financial loss]
    Q --> S[/Display financial report/]
    R --> S
    S --> T([Stop])
```

Result: The Python program successfully calculates campus event expenses, sponsorship shortfalls, participant contributions, and minimum break-even registration requirements, and generates a complete financial report.
