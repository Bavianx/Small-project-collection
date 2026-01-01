# Expense tracker 
def track_expenses():
    utilities = []
    rent = []
    groceries = []
    leisure = []
    investments = []
    
    print("Welcome to your personalised Expense tracker")   
    user_income = int(input("How much was your monthly income this month: $ ")) 

    while True:
        print("----------------------------------------------------------------------")
        print(" 1) Utilities              2) Rent ")
        print(" 3) Groceries              4) leisure")
        print(" 5) Investments            6) Total outflow")
        print(" 7) exit")
        print("----------------------------------------------------------------------")
        try:
            user_spending = int(input("Please enter which monthly expense you would like to add to: "))
        except:
            print("Invalid input, please enter a number from 1 to 5.")
            continue

        if user_spending == 1:
            utilities.append(int(input("Utilities! How much did you spend on Utilities this month?: ")))
        elif user_spending == 2: 
            rent.append(int(input("Rent! How much did you spend on Rent this month?: ")))
        elif user_spending == 3: 
            groceries.append(int(input("Groceries! How much did you spend on Groceries this month?: ")))
        elif user_spending == 4: 
            leisure.append(int(input("Leisure! How much did you spend on Leisure this month?: ")))
        elif user_spending == 5: 
            investments.append(int(input("Investments! How much did you spend on Investments this month?: ")))
        elif user_spending == 6:
            total = sum(utilities + rent + groceries + leisure + investments)
            total_saved = user_income - total  
            if total_saved > 300:
                investments.append(100)
                print("You did a good job this month, $100 has been added to your investment fund")
                percent_spent = ( total / user_income) * 100
                percent_saved = (total_saved / user_income) * 100
            print("                       Total outflow costs")
            print("----------------------------------------------------------------------")
            print("Utilities outflow", utilities)
            print("Rent outflow", rent)
            print("Groceries outflow", groceries)
            print("Leisure outflow", leisure)
            print("Investments outflow", investments)
            print("----------------------------------------------------------------------")
            print(f'total amount of money spent: {total}, Percentage spent: {percent_spent} %')
            print(f'total amount of money saved: {total_saved}, Percentage saved: {percent_saved} %')
            if total_saved > 0:
                print("Great job this month")
        elif user_spending == 7:
            print("Thank you for using me!")
            break
        else:
            print("Invalid Input")


track_expenses()
