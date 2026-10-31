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
