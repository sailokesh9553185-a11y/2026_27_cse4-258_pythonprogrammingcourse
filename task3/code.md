### 3\. Hospital Billing and Patient Classification System Using Python

### 1\. Problem Statement

The Hospital Billing and Patient Classification System is designed to calculate the total hospital bill based on consultation charges, diagnostic charges, and treatment charges.

The system applies conditional concessions based on patient category and validates billing constraints before generating the final bill.

The system performs the following operations:

* Consultation Charges: Calculate doctor consultation fees.

* Diagnostic Charges: Calculate laboratory tests, X-rays, and scanning charges.

* Treatment Charges: Calculate treatment and medical procedure charges.

* Conditional Concessions: Apply discounts based on patient category.

* Billing Validation: Ensure charges are not negative and discounts do not exceed the bill amount.

* Patient Classification: Classify patients according to their final payable amount.

### Billing Policy

| Patient category | Concession |
| ---------------- | ---------- |
| Senior citizen   | 15%        |
| Student          | 10%        |
| General patient  | 0%         |

Additional billing rules:

* Consultation charge = ₹500

* Diagnostic charges are entered by the user.

* Treatment charges are entered by the user.

* If the bill exceeds ₹10,000, an additional 5% concession is applied.

* Total bill cannot be negative.

### Patient Classification Policy

| Final payable amount | Classification |
| -------------------- | -------------- |
| Below ₹2,000         | Low Billing    |
| ₹2,000–₹5,000        | Medium Billing |
| Above ₹5,000         | High Billing   |

### 2\. Algorithm

Step 1: Start the program.

Step 2: Enter patient details:

* Patient ID

* Patient name

* Patient category

Step 3: Enter diagnostic charges and treatment charges.

Step 4: Set consultation charge to ₹500.

Step 5: Validate all entered charges.

Step 6: Calculate the subtotal.

Subtotal = Consultation + Diagnostic + Treatment

Step 7: Check patient category.

* Senior citizen: 15% concession.

* Student: 10% concession.

* General: No concession.

Step 8: If subtotal exceeds ₹10,000, apply an additional 5% concession.

Step 9: Calculate the final payable amount.

Final Bill = Subtotal − Total Concession

Step 10: Classify the patient according to the final payable amount.

Step 11: Display the complete hospital bill.

Step 12: Stop the program.

### 3\. Flowchart
flowchart TD
    A([Start]) --> B[/Enter patient details/]
    B --> C[/Enter diagnostic and treatment charges/]
    C --> D{Charges valid?}
    D -- No --> E[Display invalid billing message]
    E --> Z([Stop])
    D -- Yes --> F{Valid patient category?}
    F -- No --> G[Display invalid category]
    G --> Z
    F -- Yes --> H[Set consultation charge]
    H --> I[Calculate subtotal]
    I --> J{Patient category?}
    J -- Senior Citizen --> K[Apply 15% concession]
    J -- Student --> L[Apply 10% concession]
    J -- General --> M[No category concession]
    K --> N{Subtotal > 10000?}
    L --> N
    M --> N
    N -- Yes --> O[Apply additional 5% concession]
    N -- No --> P[No additional concession]
    O --> Q[Calculate final bill]
    P --> Q
    Q --> R{Final bill < 2000?}
    R -- Yes --> S[Low Billing]
    R -- No --> T{Final bill <= 5000?}
    T -- Yes --> U[Medium Billing]
    T -- No --> V[High Billing]
    S --> W[Display final bill]
    U --> W
    V --> W
    W --> Z([Stop])




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
if di…
