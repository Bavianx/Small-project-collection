#Bank Account 
class BankAccount:
    def __init__(self, owner, starting_balance):
        self.owner = owner
        self.balance = starting_balance

    def deposit(self, amount):

        check = input(f"Are you sure you would like to deposit £{amount}? (y/n): ")
        if check == "y":
            self.balance += amount
            print(f"Deposited £{amount}. Your New balance is: £{self.balance}")
        else:
            print("Cancelled")
            return 

    def withdraw(self, amount):
        if amount > self.balance: 
            print(f"You have insuffient funds to withdraw. £{self.balance}")
            return False
        
        self.balance -= amount 
        print(f"You have withdrew £{amount} current balance is: £{self.balance}")

    def check_balance(self):
        print(f"{self.owner}'s balance: £{self.balance}")

Test_account = BankAccount("Ben", 50)

Test_account.deposit(200)
Test_account.withdraw(50)
Test_account.check_balance()

# ===========================================================================================================================
#To do list task list

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False
    
    def mark_complete(self):
        self.completed = True

    
    def mark_incomplete(self):
        self.completed = False

    def display(self):
        print(f"Title:{self.title} , {self.completed}")

task1 = Task("Buy groceries")
task1.display()

task1.mark_complete()
task1.display()

task1.mark_incomplete()
task1.display()

class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f"Added task: {title}")
    
    def view_all_tasks(self):
        if not self.tasks:
            print("No tasks!")
            return
        
        print("\n=== All Tasks ===")
        for i, task in enumerate(self.tasks):
            print(f"{i}. ", end="")
            task.display()
    
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print("Task marked complete!")
        else:
            print("Invalid task number!")
            

my_list = TodoList()

my_list.add_task("Buy groceries")
my_list.add_task("Finish coding project")
my_list.add_task("Call mom")
my_list.view_all_tasks()
my_list.complete_task(0)
my_list.view_all_tasks()