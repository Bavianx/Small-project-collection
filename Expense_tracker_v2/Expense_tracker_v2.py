import json, os
import time
from datetime import datetime

def expense_tracker_v2():

    filename = "Expense_tracker.json"

    def load_from_file(filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            print(f"Loaded data from {filename}")
            return data

        except FileNotFoundError:
            print(f"No saved data found. Starting fresh!")
            return {}

        except json.JSONDecodeError:
            print(f"Corruption of your {filename} file")
            backup = filename + ".corrupted"
            print(f"Saving corrupted file as {backup}")
            try:
                os.rename(filename, backup)
            except:
                pass
            print("Starting with empty category.")
            return {}

        except PermissionError:
            print(f"ERROR: Don't have permission to read {filename}!")
            print("Try running as administrator or check file permissions.")
            print("Starting with empty category.")
            return {}

        except Exception as e:
            print(f"ERROR: Unexpected error loading {filename}")
            print(f"Details: {e}")
            print("Starting with empty category.")
            return {}

    def save_to_file(expenses, filename):
        try:
            with open(filename, 'w') as f:
                json.dump(expenses, f, indent=4)
            print(f"Data saved to {filename}")
        except Exception as e:
            print(f"Save failed: {e}")

    expenses = load_from_file(filename)

    def add_expense(expenses, category, amount, description, date):
        if category not in expenses:
            expenses[category] = []  
        expense = {
            "amount": float(amount),
            "description": description,
            "date": date
        }
        expenses[category].append(expense)
        print(f"Added £{amount} expense to {category}")
        save_to_file(expenses, filename)
        print("=========================================")
            

    def View_expense_by_category(expenses, category):
        if category in expenses:
            category_expense = expenses[category][0]
            print(f"{category}: £{category_expense}")           
        else:
            print(f"No expense found for {category}")
       
        
        print(f"\n{category.upper()} expenses:")
        for expense in expenses[category]: 
            print(f"  £{expense['amount']} - {expense['description']} ({expense['date']})")

    def View_all_expenses(expenses):
        if not expenses:
            print("No expenses!")
            return
        
        for category, expense_list in expenses.items(): 
            print(f"\n{category.upper()}:")
            for expense in expense_list:  
                print(f" £{expense['amount']} - {expense['description']} ({expense['date']})")



    def view_all_expenses(expenses):
        if not expenses:
            print("Please add some expenses to your expense tracker!")
            return 
        
        for category, expense_list in expenses.items():
            for expense in expense_list:
                print(f"{category}, {amount}, {description}, {date}")

    def Total_spending(expenses):
        if not expenses:
            print("No expenses!")
            return 0
        
        total = 0
        
        for category, expense_list in expenses.items():
            for expense in expense_list:
                total += expense["amount"]
        
        print(f"Total spending: £{total:.2f}")
        return total
        
    def remove_expense(expenses, category):
        if category not in expenses:
            print(f"No expenses found for category: {category}")
            return

        print(f"Expenses within category: {category}")

        for i, expense in enumerate(expenses[category]):
            print(f"{i}. Value: £{expense['amount']} | Description: {expense['description']} | Date: {expense['date']}")

        try:
            expense_index = int(input(f"Enter the index number of the expense you want to remove (0 to {len(expenses[category]) - 1}): "))
            if 0 <= expense_index < len(expenses[category]):
                expense_to_remove = expenses[category][expense_index]
                print(f"You selected: £{expense_to_remove['amount']} - {expense_to_remove['description']} on {expense_to_remove['date']}")

                confirm = input(f"Are you sure you would like to remove this expense from your tracker? (y/n): ")
                if confirm.lower() == "y":
                    removed = expenses[category].pop(expense_index)
                    print(f"Removed: £{removed['amount']} - {removed['description']} from category '{category}'.")
                    save_to_file(expenses, filename)
                else:
                    print("Cancelled...")

            else:
                print("Invalid index. No expense removed.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the index.")
        except IndexError:
            print("Index out of range. Please enter a valid index.")


    while True:
        print("============Welcome to your Expense Tracker============")
        print("1. Add expense")
        print("2. View expense by category")
        print("3. View all expenses")
        print("4. Total spending")
        print("5. Remove expense")
        print("6. Exit")
        try:
            choice = int(input("Please choose one of the menu paths: "))
            print("============================================")
        except ValueError:
            print("Please input the correlating number")
            print("============================================")
            continue

        if choice == 1:
            category = input("Please input the categorys name: ").lower()
            if not category.strip():
                print("Category cannot be empty!")
                continue
            
            if not all(character.isalpha() or character.isspace() for character in category):
                print("Category should only contain letters!")
                continue 
            amount = input("Please input the Amount spent: £")
            if not amount.isdigit():
                print("Please input a valid number for the amount.")
                continue
            description = input("Please provide a description of the expense: ").lower()
            if not description.strip():
                print("Description cannot be empty!")
                continue
            date = input("Please provide the date of the expense (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD.")
                continue
            add_expense(expenses, category, amount, description, date)
        elif choice == 2:
            category = input("Please input the category you would like to see the expenses for: ").lower()
            if not category.strip():
                print("Category cannot be empty!")
                continue
            View_expense_by_category(expenses, category)
        elif choice == 3:
            View_all_expenses(expenses)
        elif choice == 4:
            Total_spending(expenses)
        elif choice == 5:
            category = input("Please input the expense category you would like to remove an expense from: ")
            if not category.strip():
                print("Parameter empty. Please add something.")
                continue
            remove_expense(expenses, category)
        elif choice == 6:
            leave = input("Are you sure you would like to Save & Exit? (y/n): ")
            if leave.lower() == "y":
                print("Thank you for stopping by!")
                save_to_file(expenses, filename)
                print("=========================================")
                break
            else:
                print("Great! what else can we help you with?")
                continue

expense_tracker_v2()





    





