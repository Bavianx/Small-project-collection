
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
    students = []

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
            name = input("Please input the students name: ")
            if not name:
                print("student could not be empty")
                continue 
            student = Student(name)
            students.append(student)
        elif choice == "2": #Finish tomorrow
            pass
            print(f"Successfully added {name}")
        elif choice == "3":
            name = input("Please input the students name: ")

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
                print(f"- {student.name}")
            pass
        elif choice == "5":#Finish tomorrow
            pass
        elif choice == "6":#Finish tomorrow
            pass
        elif choice == "7":#Finish tomorrow
            break
main()



