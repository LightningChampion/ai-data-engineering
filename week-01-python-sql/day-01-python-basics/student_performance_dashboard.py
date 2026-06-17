print("Student Performance Dashboard")
print("=============================")

students = {
    "Ali": {
        "department": "MIS",
        "midterm": 75,
        "final": 85
    },
    "Mehmet": {
        "department": "MIS",
        "midterm": 60,
        "final": 55
    },
    "Ayse": {
        "department": "Computer Engineering",
        "midterm": 90,
        "final": 95
    },
    "Zeynep": {
        "department": "Business",
        "midterm": 50,
        "final": 65
    }
}


def calculate_average(midterm, final):
    average = (midterm * 0.4) + (final * 0.6)
    return average


def calculate_letter_grade(average):
    if average >= 85:
        return "AA"
    elif average >= 70:
        return "BB"
    elif average >= 55:
        return "CC"
    else:
        return "FF"


def get_pass_status(average):
    if average >= 55:
        return "Passed"
    else:
        return "Failed"


averages = []
passed_count = 0
best_student = ""
best_average = 0

print("\nStudent Results")
print("--------------------")

for name, info in students.items():
    average = calculate_average(info["midterm"], info["final"])
    letter_grade = calculate_letter_grade(average)
    status = get_pass_status(average)

    averages.append(average)

    if status == "Passed":
        passed_count = passed_count + 1

    if average > best_average:
        best_average = average
        best_student = name

    print(f"{name} | Department: {info['department']} | Average: {average} | Grade: {letter_grade} | Status: {status}")


class_average = sum(averages) / len(averages)
success_rate = (passed_count / len(students)) * 100

print("\nClass Summary")
print("--------------------")
print(f"Class average: {class_average}")
print(f"Success rate: {success_rate}%")
print(f"Best student: {best_student} with {best_average}")


print("\nDepartment Summary")
print("--------------------")

departments = {}

for name, info in students.items():
    department = info["department"]
    average = calculate_average(info["midterm"], info["final"])

    if department not in departments:
        departments[department] = []

    departments[department].append(average)

for department, department_averages in departments.items():
    department_average = sum(department_averages) / len(department_averages)
    print(f"{department}: average = {department_average}")
