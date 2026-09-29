students = {
    "Kavi": [85, 90, 80],
    "Ravi": [75, 85, 90],
    "Arun": [90, 88, 95],
    "Priya": [80, 79, 85]
}

for name, marks in students.items():
    if all(mark >= 80 for mark in marks):
        print(name)