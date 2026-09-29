students = {
    "Kavi": [80, 75, 90],
    "Ravi": [70, 85, 95],
    "Arun": [60, 72, 68]
}

for name, marks in students.items():
    average = sum(marks) / len(marks)
    print(name, round(average, 2))