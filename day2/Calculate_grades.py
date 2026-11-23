n = int(input("Enter the number of subjects: "))
for i in range(n):
    try:
        marks = float(input(f"Enter marks for subject {i + 1}: "))
        if marks < 0 or marks > 100:
            print("Invalid input. Marks should be between 0 and 100.")
            continue
        if marks >= 90:
            grade = 'A'
        elif marks >= 80:
            grade = 'B'
        elif marks >= 70:
            grade = 'C'
        elif marks >= 60:
            grade = 'D'
        else:
            grade = 'F'
        print(f"Grade for subject {i + 1}: {grade}") #i was too lazy to wirte all the different grades.
    except ValueError as err:
        print("Invalid input. Please enter a valid number for marks." + str(err))