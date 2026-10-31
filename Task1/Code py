# University Scholarship Allocation System

students = []
eligible_students = []
rejected_students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    marks = []
    subjects = int(input("Enter number of subjects: "))

    for j in range(subjects):
        mark = float(input(f"Enter subject {j+1} marks: "))
        marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    aggregate = sum(marks) / len(marks)

    student = {
        "id": sid,
        "name": name,
        "aggregate": aggregate,
        "attendance": attendance,
        "income": income
    }

    # Eligibility checking
    if (aggregate >= 75 and
        all(mark >= 60 for mark in marks) and
        attendance >= 75 and
        income <= 250000):

        eligible_students.append(student)

    else:
        rejected_students.append(student)

# Ranking eligible students
eligible_students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["id"]
    )
)

# Display results
print("\n===== SCHOLARSHIP RANK LIST =====")

if eligible_students:
    for rank, s in enumerate(eligible_students, start=1):
        print("\nRank:", rank)
        print("Student ID:", s["id"])
        print("Name:", s["name"])
        print("Aggregate:", round(s["aggregate"], 2), "%")
        print("Attendance:", s["attendance"], "%")
        print("Family Income: Rs.", s["income"])
else:
    print("No eligible students found.")

print("\n===== REJECTED STUDENTS =====")

for s in rejected_students:
    print(s["id"], "-", s["name"])

print("\nProgram completed successfully.")
