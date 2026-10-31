# Railway Fare and Reservation Calculator

print("RAILWAY FARE CALCULATOR")

distance = float(input("Enter journey distance (km): "))
n = int(input("Enter number of passengers: "))

total_fare = 0
total_penalty = 0

for i in range(n):

    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))

    print("\nTravel Classes")
    print("1. Sleeper - Rs. 1.50/km")
    print("2. AC 3 Tier - Rs. 2.50/km")
    print("3. AC 2 Tier - Rs. 3.50/km")

    choice = int(input("Select class (1-3): "))

    if choice == 1:
        rate = 1.50
        reservation = 20
        class_name = "Sleeper"

    elif choice == 2:
        rate = 2.50
        reservation = 40
        class_name = "AC 3 Tier"

    elif choice == 3:
        rate = 3.50
        reservation = 50
        class_name = "AC 2 Tier"

    else:
        print("Invalid class selection")
        continue

    # Distance slab charges
    if distance <= 100:
        slab_charge = 0
    elif distance <= 500:
        slab_charge = 50
    else:
        slab_charge = 100

    basic_fare = distance * rate + slab_charge

    # Age-based concession
    concession = 0

    if age < 5:
        concession = basic_fare
    elif age >= 60:
        concession = basic_fare * 0.20

    fare = basic_fare - concession + reservation

    print("\nPassenger Name:", name)
    print("Travel Class:", class_name)
    print("Basic Fare: Rs.", round(basic_fare, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Reservation Fee: Rs.", reservation)

    cancel = input("Cancel ticket? (yes/no): ").lower()

    if cancel == "yes":
        penalty = fare * 0.25
        payable = penalty
        total_penalty += penalty
        print("Cancellation Penalty: Rs.", round(penalty, 2))
    else:
        payable = fare
        print("Ticket Confirmed")

    print("Final Amount: Rs.", round(payable, 2))

    total_fare += payable

print("\n----- FINAL RAILWAY BILL -----")
print("Total Passengers:", n)
print("Total Cancellation Penalty: Rs.",
      round(total_penalty, 2))
print("Total Amount: Rs.", round(total_fare, 2))
print("Thank You!")
