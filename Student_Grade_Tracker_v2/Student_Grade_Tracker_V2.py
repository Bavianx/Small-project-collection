import json, os
class Student:

    def __init__(self, name):
        self.name = name
        self.grades = []
     
    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"{self.grades} has been added to {self.name}'s account")

    def get_average(self):
        if not self.grades:
            print("Please add a grade to the students account")
            return 0
        return sum(self.grades) / len(self.grades)
    def is_passing(self):
        return self.get_average() >= 65 

    def display(self):
        avg = self.get_average()
        
        if self.is_passing():
            status = f"Passing - Congratulations {self.name}!"
        else:
            status = f"Failing - Need 65 or higher, achieved {avg:.1f}"
        
        print(f"Student: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average: {avg:.1f}")
        print(f"Status: {status}")

def main():
    filename = "students.json"

    students = load_from_file(filename)

    while True:
        print("\n" + "="*40)
        print("    STUDENT GRADE TRACKER")
        print("="*40)
        print("1. Add Student")
        print("2. Add Grade to Student")
        print("3. View Student")
        print("4. View All Students")
        print("5. Remove Student")
        print("6. Class Average")
        print("7. Exit")
        print("="*40)
        try:
            choice = input("Choose menu option (1-7): ")
            print("============================================")
        except ValueError:
            print("Please input a valid menu integer!")
            print("============================================")

        if choice == "1": 
            name = input("Please input the students name: ").lower()
            if not name.strip():
                print("Name cannot be empty!")
                print("=====================================================")
                continue

            if not all(character.isalpha() or character.isspace() for character in name):
                print("Name should only contain letters!")
                print("=====================================================")
                continue 

            if not name:
                print("Student is not within the system!")
                continue 

            student = Student(name)
            students.append(student)
        elif choice == "2":
            if not students:
                print("No students in system!")
                continue
            
            name = input("Please input the student's name: ").strip().lower()
        
            if not name:
                print("Name cannot be empty!")
                continue
            
            if not all(char.isalpha() or char.isspace() for char in name):
                print("Name should only contain letters!")
                continue
            
            found_student = None
            for student in students:
                if student.name.lower() == name:
                    found_student = student
                    break
            
            if found_student:
                print(f"\n{found_student.name}'s current grades: {found_student.grades}")
                grade = input("Enter grade to add: ").strip()
                try:
                    grade = float(grade)
                    if 0 <= grade <= 100:
                        found_student.add_grade(grade)
                        print(f"Grade {grade} added to {found_student.name}")
                    else:
                        print("Grade must be between 0-100!")
                except ValueError:
                    print("Invalid grade! Please enter a number.")
            else:
                print(f"Student '{name}' not found in system!")

        elif choice == "3":
            name = input("Please input the students name: ").lower()

            found = False
            for student in students:
                if student.name == name:
                    student.display()
                    found = True
                    break
            if not name:
                print(f"{name} is not within our database")
                continue
        elif choice == "4":            
            for student in students:
                print(f"Student: {student.name} Grades: {student.grades} Average: {student.get_average()}")
            pass
        elif choice == "5":
            if not students:
                print("No students within our system!")
                continue
            name = input("Please enter the students name: ").lower()

            if not name:
                print("Name cannot be empty!")
                continue

            found_student = None
            for student in students:
                if student.name == name:
                    found_student = student
                    break

            if found_student:
                found_student.display()
                confirm = input("Would you still like to remove the student? (y/n): ")
                if confirm == "y":
                    students.remove(found_student)
                    print(f"Successfully removed {student.name} from the system")
                else:
                    print("Cancelled...")
            else:
                print("Student was not found within our system.")

        elif choice == "6":
            if not students:
                print("No students in system!")
                continue
            
            total = 0
            count = 0
            
            for student in students: 
                avg = student.get_average()  
                if avg > 0:  
                    total += avg
                    count += 1
            
            if count > 0:
                class_avg = total / count
                print(f"Class Average: {class_avg:.1f}")
                print(f"Students with grades: {count}/{len(students)}")
            else:
                print("No students have grades yet!")
        elif choice == "7":
            confirm = input("Would you like to exit the application? (y/n):")
            if confirm == "y":
                save_to_file(students, filename)
                print("Exiting...")
                break
            else:
                print("Continuing!")

    def save_to_file(students, filename):
        data = {}
        for student in students:
            data[student.name] = student.grades
        
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        
        print(f"Data saved to {filename}")

    def load_from_file(filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            
            students = []
            for name, grades in data.items():
                student = Student(name)
                student.grades = grades
                students.append(student)
            
            print(f"Loaded {len(students)} students from {filename}")
            return students
        
        except FileNotFoundError:
            print("No saved data found. Starting fresh!")
            return []
main()







