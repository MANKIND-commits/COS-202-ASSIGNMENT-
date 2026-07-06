print("===== PERSONAL POCKET CGPA CALCULATOR =====")
while True:
    total_units = 0
    total_grade_points = 0
    num_courses = int(input("\nEnter the number of courses: "))
    for i in range(num_courses):
        print("\nCourse", i + 1)
        course = input("Course code: ")
        unit = int(input("Course unit: "))
        grade = input("Grade (A, B, C, D, E, F): ").upper()
        # Selection control statements
        if grade == "A":
            point = 5
        elif grade == "B":
            point = 4
        elif grade == "C":
            point = 3
        elif grade == "D":
            point = 2
        elif grade == "E":
            point = 1
        elif grade == "F":
            point = 0
        else:
            print("Invalid grade entered!")
            point = 0
        total_units += unit
        total_grade_points += unit * point
    if total_units > 0:
        cgpa = total_grade_points / total_units
    else:
        cgpa = 0
    print("\n===== RESULT =====")
    print("Total Units =", total_units)
    print("Total Grade Points =", total_grade_points)
    print("CGPA =", round(cgpa, 2))
    option = input("\nEnter C to clear or OFF to turn off: ").upper()
    if option == "OFF":
        print("CGPA Calculator turned off.")
        break
    elif option == "C":
        continue
    else:
        print("Invalid option. Calculator turned off.")
        break