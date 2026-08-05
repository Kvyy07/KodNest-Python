
marks = int(input())
attendance = int(input())
project_status = input()

# Compound condition for marks and attendance
if marks >= 60 and attendance >= 75:
    # Nested condition for project completion
    if project_status == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")
