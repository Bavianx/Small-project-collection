#Step 1 
# The project is a contact manager, this application will store worker data provided ranging from full name, mobile number, email address and job role. this is data which is provided by the USER so input will be taken from them and stored within a nested dictionary (data under user profile). Users will need to be  added, edited and removed from this dictionary meaning there is at least 3 functions that we will be using. 

#INPUT / users NAME , EMAIL , MOBILE , JOB ROLE
#Output / upon request of user data each or all will be provided
#FEATURES / added, edited and removed function , Nested content, main menu to flow through the sections, error handling for input data, Json for storing and keeping data alive after application closure

#Create json file to store all of the data within 
import json, os
def contact_catalogue():
    filename = "contact_catalogue.json"

    def load_from_file(filename):                        
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
            print(f"Saving corrupted file as {backup}")     

            try:
                os.rename(filename, backup)                
            except:
                pass                                     
            print("Starting with empty catalogue.")
            return {}                                 
        
        except PermissionError:
            print(f"ERROR: Don't have permission to read {filename}!")
            print("Try running as administrator or check file permissions.")
            print("Starting with empty catalogue.")
            return {}  
        
        except Exception as e:
            print(f"ERROR: Unexpected error loading {filename}")
            print(f"Details: {e}")
            print("Starting with empty catalogue.")
            return {}

    
    def save_to_file(workers, filename):
        try:
            
            if os.path.exists(filename):                            
                with open(filename, 'r') as f:
                    old_data = f.read()
                with open(filename + ".backup", 'w') as f:
                    f.write(old_data)
            
            with open(filename, 'w') as f:                          
                json.dump(workers, f, indent=4)
            
            print(f"Data saved to {filename}")
            return True
            
        except Exception as e:
            print(f"Save failed: {e}")
            return False
        
    workers = load_from_file(filename) 

    def add_user(workers, name, email, mobile, role):
        if name not in workers:
            workers[name] = {
                "email": email,
                "mobile": mobile,
                "role": role
            }
        print(f"Worker {name} has been added to the catalogue!")
        save_to_file(workers, filename)
        print("=========================================")


    def edit_user(workers, name):
        if name not in workers:
            print(f"{name} not found within the catalogue")
            return False
        
        worker = workers[name]

        print(f"Current email: {worker['email']}")
        print(f"Current mobile: {worker['mobile']}") 
        print(f"Current role: {worker['role']}") 
        print("=========================================")

        while True:
            print("Welcome to the Worker edit menu")
            print("1. Edit Email")
            print("2. Edit Mobile")
            print("3. Edit Role")
            print("4. Exit Edit mode")
            print("=========================================")
            try:
                change = int(input("Please choose one of the menu paths: "))
                print("============================================")
            except ValueError:
                print("Please input a valid integer")
                print("============================================")
                continue
            
            if change == 1:
                new_email = input("Enter new email address: ")
                confirm = input(f"Change email to {new_email}? (y/n): ")
                if confirm == "y":
                    workers[name]["email"] = new_email
                    print(f"Email for {name} updated to {new_email}!")
                else:
                    print("Change cancelled!")

            elif change == 2:
                new_mobile = input("Enter new mobile number: ")
                confirm = input(f"Change mobile to {new_mobile}? (y/n): ")
                if confirm == "y":
                    workers[name]["mobile"] = new_mobile
                    print(f"Mobile for {name} updated to {new_mobile}!")
                else:
                    print("Change cancelled!")

            elif change == 3:
                new_role = input("Enter new Job Role: ")
                confirm = input(f"Change role to {new_role}? (y/n): ").lower()
                if confirm == "y":
                    workers[name]["role"] = new_role
                    print(f"Role for {name} updated to {new_role}!")
                else:
                    print("Change cancelled!")

            elif change == 4:
                break
        
        return True

    def remove_user(workers, name):
        if name not in workers:
            print(f"{name} has not been found within the catalogue")
            return False

        worker = workers[name]
        print(f"Removing: {name}")
        print(f"Email: {worker['email']}")
        print(f"Role: {worker['role']}")

        confirm = input(f"Are you sure you would like to remove {name}? (y/n): ").lower()
        if confirm == "y":
            workers.pop(name)
            print(f"{name} was successfully removed!")
            save_to_file(workers, filename)
        else:
            print("Action was stopped!")
            return False

    def view_all_users(workers):
        if not workers:
            print("Please input workers into the catalogue")
            return 
        
        for name, worker in workers.items():
            email = worker["email"]
            mobile = worker["mobile"]
            role = worker["role"]
            print(f"Name:{name}, Email: {email}, Mobile: {mobile}, Role: {role}")

    while True:
        print("=====================Main Menu=====================")
        print("1. Add a user")
        print("2. Edit a user")
        print("3. Remove a user")
        print("4. View all users")
        print("5. Save & Exit")
        print("==========================================")
        try: 
            choice = int(input("Please choose one of the menu paths: "))
            print("============================================")
        except ValueError:
            print("Please input the correlating number")
            print("============================================")
            continue

        if choice == 1:
            name = input("Please enter your name: ").lower()
            if not name.strip():
                print("Name cannot be empty!")
                print("=====================================================")
                continue
            
            if not all(character.isalpha() or character.isspace() for character in name):
                print("Name should only contain letters!")
                print("=====================================================")
                continue 

            email = input("Please enter your email: ")
            if not email.strip():
                print("Email cannot be empty!")
                print("=====================================================")
                continue
            mobile = input("Please enter your mobile: ")
            if not mobile.strip():
                print("Mobile cannot be empty!")
                print("=====================================================")
                continue
            role = input("Please enter your role: ")
            if not role.strip():
                print("Role cannot be empty!")
                print("=====================================================")
                continue

            add_user(workers, name, email, mobile, role)
        elif choice == 2: 
            name = input("Please input the workers name: ").lower()
            edit_user(workers, name)
        elif choice == 3:
            name = input("Please input the workers name: ").lower()
            if not name.strip():
                print("Name cannot be empty!")
                print("=====================================================")
                continue
            if not all(character.isalpha() or character.isspace() for character in name):
                print("Name should only contain letters!")
                print("=====================================================")
                continue 
            remove_user(workers, name)
        elif choice == 4:
            view_all_users(workers)
        elif choice == 5:
            confirm = input("Save & Exit? (y/n): ").lower()
            if confirm.lower() == 'y':
                save_to_file(workers, filename)
                print("Goodbye!")
                break
            else:
                print("Continuing..")

contact_catalogue()

