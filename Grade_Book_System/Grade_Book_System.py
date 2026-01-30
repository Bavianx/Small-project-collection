
def grade_booking_system():
    grade_book = {}

    def add_student(grade_book, student, subject, grade):           #Add new student with their first grade.

        if student not in grade_book:
            grade_book[student] = {}
        grade_book[student][subject] = grade
        print(f"Sucessfully added {student}'s {subject} grade of {grade}")
        print(grade_book)

    def add_grade(grade_book, student, subject, grade):             #Add additional grade to existing student
        if student in grade_book:
            grade_book[student][subject] = grade
            print(f"Added {subject}: {grade} for {student}")
        else:
            print(f"Please enter a students name who is already enlisted or add student within (option 1).")

    def view_student(grade_book, student):                  #Display individual student's grades and average.
        if student in grade_book:
            print(f"{student}'s grade")
            for subject, grade in grade_book[student].items():
                print(f"{subject}: {grade}")

            student_grade = grade_book[student].values()
            average = sum(student_grade) / len(student_grade)
            print(f"average: {average:.2f}")

        else:
            print(f"Student {student} not found")

    def show_all_students(grade_book):                      #Display all students with their averages.
        if not grade_book:
            print("No students added yet!")
            return
        
        print("\nAll Students:")
        for student, grades in grade_book.items():
            average = sum(grades.values()) / len(grades.values()) 
            print(f"{student}: {average:.2f}")

    def view_all_passing(grade_book):           #Show students grouped by passing (≥65) vs failing (<65).
        if not grade_book:
            print("Please add a student")
        
        passing = []
        failing = []

        for student, grades in grade_book.items():
            average = sum(grades.values()) / len(grades.values()) 
            if average >= 65:
                passing.append((student, average))
            else:
                failing.append((student, average))

        print("\nPASSING:")
        for student, average in passing:
            print(f"  {student}: {average:.2f}")
        
        print("\nFAILING:")
        for student, average in failing:
            print(f"  {student}: {average:.2f}")

    while True:                                              
        print("Welcome to the grade booking system")
        print("1. Add student")
        print("2. Add additional grades")
        print("3. View student")
        print("4. View all students")
        print("5. View all passing")
        print("6. Exit....")

        choice = int(input("Please input correlating number of where you would like to go: "))

        if choice == 1:
            student = input("Students name: ")
            subject = input("Subject: ")
            grade = int(input("Grade: "))
            add_student(grade_book, student, subject, grade)
        elif choice == 2:
            student = input("Student name: ")
            subject = input("Subject: ")
            grade = int(input("Grade: "))
            add_grade(grade_book, student, subject, grade)
        elif choice == 3:
            student = input("Student name: ")
            view_student(grade_book, student)
        elif choice == 4:
            show_all_students(grade_book)
        elif choice == 5:
            view_all_passing(grade_book)
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

grade_booking_system()