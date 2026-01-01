def atm_machine():

    balance = 0

    while True:
        print("-------------------------------------------------------------------------")
        print("- Welcome, how can we help you today")
        print("1 - Deposit")
        print("2 - Withdraw")
        print("3 - Check balance")
        print("4 - Exit")
        print("-------------------------------------------------------------------------")
        try:
            user = int(input("Please select your choice (1-4): "))
        except ValueError:
            print("Please input the correct parameters!")
            continue
            
        if user == 1:
            deposit = int(input("Please input the amount you would like to deposit: $ "))
            balance += deposit
            print(f"Your balance is now: $", {balance} )

        elif user == 2:
            withdraw = int(input("Please request how much money you would like to withdraw: $ "))
            if withdraw > balance:
                print("You have insufficient funds!")
            else:
                balance -= withdraw
                print(f"You have withdrawn:", {withdraw} ,"Your balance is now: $ ", {balance})

        elif user == 3:
            print(f"Your balance is: $", {balance})

        elif user == 4:
            print("Thank you for using us today")
            break

final_balance = atm_machine()
print(final_balance)
