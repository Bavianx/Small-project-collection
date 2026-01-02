def atm_machine():
    balance = 0

    while True:
        print("\n" + "="*70)
        print("Welcome! How can we help you today?")
        print("1 - Deposit")
        print("2 - Withdraw")
        print("3 - Check Balance")
        print("4 - Exit")
        print("="*70)
        
        try:
            user = int(input("Please select your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number 1-4.")
            continue
            
        if user == 1:
            try:
                deposit = int(input("Enter deposit amount: $"))
                if deposit <= 0:
                    print("Deposit must be positive!")
                    continue
                question = input(f"Deposit ${deposit}? (y/n): ").lower()
                if question == 'y':
                    balance += deposit
                    print(f"Deposited ${deposit}. New balance: ${balance}")
                else:
                    print("Deposit cancelled.")
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif user == 2:
            try:
                withdraw = int(input("Enter withdrawal amount: $"))
                if withdraw <= 0:
                    print("Withdrawal must be positive!")
                    continue
                if withdraw > balance:
                    print(f"Insufficient funds! Your balance is ${balance}")
                else:
                    question = input(f"Withdraw ${withdraw}? (y/n): ").lower()
                    if question == 'y':
                        balance -= withdraw
                        print(f"Withdrew ${withdraw}. New balance: ${balance}")
                    else:
                        print("Withdrawal cancelled.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif user == 3:
            print(f"Your current balance is: ${balance}")
        elif user == 4:
            print(f"Thank you for banking with us! Final balance: ${balance}")
            break
        else:
            print("Invalid choice. Please select 1-4.")
    return balance

final_balance = atm_machine()
