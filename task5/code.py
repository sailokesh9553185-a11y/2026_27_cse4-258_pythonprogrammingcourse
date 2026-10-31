# Multi-Plan Telecommunications Cost Optimization

print("TELECOMMUNICATION PLAN OPTIMIZATION")

# User requirements
data_required = float(input("Enter required data (GB): "))
calls_required = int(input("Enter required call minutes: "))
sms_required = int(input("Enter required SMS count: "))
validity_required = int(input("Enter required validity (days): "))
budget = float(input("Enter your budget (Rs): "))

n = int(input("\nEnter number of mobile plans: "))

plans = []

for i in range(n):
    print(f"\nEnter details of Plan {i + 1}")

    name = input("Plan name: ")
    price = float(input("Plan price (Rs): "))
    data = float(input("Data limit (GB): "))
    calls = int(input("Call minutes: "))
    sms = int(input("SMS limit: "))
    validity = int(input("Validity (days): "))

    # Additional charges
    data_rate = 10
    call_rate = 0.50
    sms_rate = 0.25

    # Calculate excess usage
    extra_data = max(0, data_required - data)
    extra_calls = max(0, calls_required - calls)
    extra_sms = max(0, sms_required - sms)

    # Calculate extra charges
    extra_charge = (
        extra_data * data_rate
        + extra_calls * call_rate
        + extra_sms * sms_rate
    )

    total_cost = price + extra_charge

    # Check eligibility
    if validity >= validity_required and total_cost <= budget:
        plans.append((name, total_cost, price, extra_charge))

# Find economical plan
if plans:
    best_plan = min(plans, key=lambda x: x[1])

    print("\n----- RECOMMENDED PLAN -----")
    print("Plan Name:", best_plan[0])
    print("Base Price: Rs.", best_plan[2])
    print("Extra Charges: Rs.", best_plan[3])
    print("Total Cost: Rs.", best_plan[1])
    print("Status: Eligible")
else:
    print("\nNo eligible plan found!")
    print("Please increase your budget or modify requirements.")
