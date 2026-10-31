# Hospital Billing and Patient Classification System

CONSULTATION_CHARGE = 500

# Function to classify patient
def classify_patient(amount):

    if amount < 2000:
        return "Low Billing"

    elif amount <= 5000:
        return "Medium Billing"

    else:
        return "High Billing"


# Main program
print("===== HOSPITAL BILLING SYSTEM =====")

patient_id = input("Enter Patient ID: ")
patient_name = input("Enter Patient Name: ")

print("\nPatient Categories:")
print("1. Senior Citizen")
print("2. Student")
print("3. General")

category = input("Enter patient category (1/2/3): ")

diagnostic = float(input("Enter diagnostic charges: Rs. "))
treatment = float(input("Enter treatment charges: Rs. "))

# Validate billing constraints
if diagnostic < 0 or t…
