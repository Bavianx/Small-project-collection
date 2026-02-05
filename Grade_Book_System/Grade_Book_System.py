import json , os
def grade_booking_system():
    filename = "grades.json"
    
    def load_from_file(filename):                           #Define load function for json
        try:    
            with open(filename, 'r') as f:
                data = json.load(f)

            with open(filename + ".backup", 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Loaded data from {filename}")
            return data
        
        except FileNotFoundError:
            print(f"No saved data found. Starting fresh!")
            return {}
        
        except json.JSONDecodeError:
            print(f"Corruption of your {filename} file")
            backup = filename + ".corrupted"
            print(f"Saving corrupted file as {backup}")     #takes data corrupted data and stores it as backup 

            try:
                os.rename(filename, backup)                 #backup created 
            except:
                pass                                        #If it already exists just continue
            print("Starting with empty grade book.")
            return {}                                       #creates new file to add data to
        
        except PermissionError:
            print(f"ERROR: Don't have permission to read {filename}!")
            print("Try running as administrator or check file permissions.")
            print("Starting with empty grade book.")
            return {}  # Start fresh with a new file, can't access old data
        
        except Exception as e:
            print(f"ERROR: Unexpected error loading {filename}")
            print(f"Details: {e}")
            print("Starting with empty grade book.")
            return {}

    
    def save_to_file(gradebook, filename):
        try:
            
            if os.path.exists(filename):                            # Create backup of existing file BEFORE overwriting
                with open(filename, 'r') as f:
                    old_data = f.read()
                with open(filename + ".backup", 'w') as f:
                    f.write(old_data)
            
            with open(filename, 'w') as f:                          # Now save new data
                json.dump(gradebook, f, indent=4)
            
            print(f"Data saved to {filename}")
            return True
            
        except Exception as e:
            print(f"Save failed: {e}")
            return False
        
    
    grade_book = load_from_file(filename) 

    def get_letter_grade(average):                                  #function which can be called to provide the grade based on the students average 

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def add_student(grade_book, student, subject, grade):           #Add new student with their first grade.

        if student not in grade_book:
            grade_book[student] = {}
        grade_book[student][subject] = grade
        print(f"Sucessfully added {student}'s {subject} grade of {grade}")
        save_to_file(grade_book, filename)
        print(grade_book)

    def add_grade(grade_book, student, subject, grade):             #Add additional grade to existing student
        if student in grade_book:
            grade_book[student][subject] = grade
            print(f"Added {subject}: {grade} for {student}")
        else:
            print(f"Please enter a students name who is already enlisted or add student within (option 1).")

    def view_student(grade_book, student):                          #Display individual student's grades and average.
        if student in grade_book:
            print(f"{student}'s grade")
            for subject, grade in grade_book[student].items():
                print(f"{subject}: {grade}")

            student_grade = grade_book[student].values()
            average = sum(student_grade) / len(student_grade)
            letter = get_letter_grade(average)
            
            print(f"Average: {average:.2f} ({letter})")
        else:
            print(f"Student {student} not found")

    def show_all_students(grade_book):                              #Display all students with their averages.
        group_grades = {}
        if not grade_book:
            print("No students added yet!")
            return

        for student, grades in grade_book.items():
            average = sum(grades.values()) / len(grades.values()) 
            letter = get_letter_grade(average)
            if letter not in group_grades:
                group_grades[letter] = []
            group_grades[letter].append((student, average))

        print("\nAll Students(Grade Group):")
        for letter in ["A", "B", "C", "D", "F"]:
            if letter in group_grades:
                students_formatted = []
                for student, average in group_grades[letter]:
                    students_formatted.append(f"{student} ({average:.2f})")
                students =", ".join(students_formatted)
                print(f"{letter} Grade: {students} ")

    def view_all_passing(grade_book):                               #Show students grouped by passing (≥65) vs failing (<65).
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

    def remove_student(grade_book, student):
        if student in grade_book:
            grade_book.pop(student)
            print(f"Removed {student} from the grade book")
            save_to_file(grade_book, filename)
        else:
            print(f"{student} not found!")

    while True:             
        print("=====================================================")                                 
        print("Welcome to the grade booking system")
        print("1. Add student")
        print("2. Add additional grades")
        print("3. View student")
        print("4. View all students")
        print("5. View all passing")
        print("6. Delete/ remove student")
        print("7. Exit....")
        print("=====================================================")
        try:
            choice = int(input("Please input correlating number of where you would like to go: "))
        except ValueError:
            print("Please input the correlating number")
            print("=====================================================")
            continue 

        if choice == 1:
            student = input("Students name: ").lower()
            if not student.strip():
                print("Name cannot be empty!")
                print("=====================================================")
                continue

            if not all(character.isalpha() or character.isspace() for character in student):
                print("Name should only contain letters!")
                print("=====================================================")
                continue 

            subject = input("Subject: ")
            valid_subjects = ["math", "english", "science", "history", "geography", "art"]
            if subject.lower() not in valid_subjects:
                print(f"Subjects must be one of: {', '.join(valid_subjects)}")
                print("=====================================================")
                continue
            try:
                grade = int(input("Grade: "))
                if grade < 0 or grade > 100:
                    print("Please input a valid grade between 0-100")
                    print("=====================================================")
                    continue

            except ValueError:
                print("Grade must be a number!")
                print("=====================================================")
                continue
            add_student(grade_book, student, subject, grade)

        elif choice == 2:
            student = input("Student name: ").lower()
            if not student.strip():
                print("Name cannot be empty!")
                print("=====================================================")
                continue

            if not all(c.isalpha() or c.isspace() for c in student):
                print("Name should only contain letters!")
                continue 

            subject = input("Subject: ")
            if not subject.strip():
                print("Subject cannot be empty!")
                print("=====================================================")
                continue

            try:
                grade = int(input("Grade: "))
                if not 0 <= grade <= 100:
                    print("Grade must be between 0-100!")
                    print("=====================================================")
                    continue

            except ValueError:
                print("Grade must be a number!")
                print("=====================================================")
                continue
            add_grade(grade_book, student, subject, grade)

        elif choice == 3:
            student = input("Student name: ").lower()
            if not student.strip():
                print("Name cannot be empty!")
                print("=====================================================")
                continue

            if not all(c.isalpha() or c.isspace() for c in student):
                print("Name should only contain letters!")
                print("=====================================================")
                continue 
            view_student(grade_book, student)

        elif choice == 4:
            show_all_students(grade_book)

        elif choice == 5:
            view_all_passing(grade_book)

        elif choice == 6:
            student = input("Student name: ").lower()
            if not student.strip():
                print("Name cannot be empty!")
                print("=====================================================")
                continue
            confirm = input(f"Remove {student}? Once done cannot be undone (y/n)")
            if confirm == "y":
                remove_student(grade_book, student)
            else:
                print("Cancelled")

        elif choice == 7:
            confirm = input("Save & Exit? (y/n): ")
            if confirm.lower() == 'y':
                save_to_file(grade_book, filename)
                print("Goodbye!")
                break
            else:
                print("Continuing..")

grade_booking_system()










