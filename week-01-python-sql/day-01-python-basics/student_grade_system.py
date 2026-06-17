students = {
    "Ali": 90,
    "Mehmet": 72,
    "Ayse": 40
}


def calculate_letter_grade(grade):
    if grade >= 85:
        return "AA"
    elif grade >= 70:
        return "BB"
    elif grade >= 55:
        return "CC"
    else:
        return "FF"


for name, grade in students.items():
    result = calculate_letter_grade(grade)
    print(f"{name}: {grade} -> {result}")
