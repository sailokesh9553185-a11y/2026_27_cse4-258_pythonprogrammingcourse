# Employee Payroll and Deduction Analysis System

# Function to calculate progressive deductions
def calculate_deduction(gross):

    deduction = 0

    if gross <= 20000:
        deduction = gross * 0.05

    elif gross <= 40000:
        deduction = (20000 * 0.05) + ((gross - 20000) * 0.10)

    else:
        deduction = (
            (20000 * 0.05) +
            (20000 * 0.10) +
            ((gross - 40000) * 0.15)
        )

    return deduction


# Main program
print("===== EMPLOYEE PAYROLL SYSTEM =====")

emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")

basic = float(input("Enter Basic Pay: Rs. "))
overtime_hours = float(input("Enter Overtime Hours: "))
incentives = float(input("Enter Incentives: Rs. "))

# Validate input
if basic < 0 or overtime_hours < 0 or incentives < 0:

    print("\nInvalid Input!")
    print("Salary details cannot be negative.")

else:

    # Calculate allowances
    hra = basic * 0.20
    da = basic * 0.10

    # Calculate overtime payment
    overtime_rate = 200
    overtime_pay = overtime_hours * overtime_rate

    # Calculate gross salary
    gross = basic + hra + da + overtime_pay + incentives

    # Calculate progressive deductions
    deduction = calculate_deduction(gross)

    # Calculate net salary
    net_salary = gross - deduction

    # Display salary statement
    print("\n========== SALARY STATEMENT ==========")

    print("Employee ID       :", emp_id)
    print("Employee Name     :", name)

    print("\n---------- EARNINGS ----------")

    print("Basic Pay         : Rs.", round(basic, 2))
    print("HRA (20%)         : Rs.", round(hra, 2))
    print("DA (10%)          : Rs.", round(da, 2))
    print("Overtime Pay      : Rs.", round(overtime_pay, 2))
    print("Incentives        : Rs.", round(incentives, 2))

    print("--------------------------------------")
    print("Gross Salary      : Rs.", round(gross, 2))

    print("\n---------- DEDUCTIONS ----------")

    print("Progressive Deduction: Rs.",
          round(deduction, 2))

    print("--------------------------------------")

    print("Net Salary        : Rs.",
          round(net_salary, 2))

    print("\nPayroll generated successfully.")
