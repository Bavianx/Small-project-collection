import json, os

def to_do_list():
    filename = "To_do_list.json"

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
                return []
            
            except json.JSONDecodeError:
                print(f"Corruption of your {filename} file")
                backup = filename + ".corrupted"
                print(f"Saving corrupted file as {backup}")     

                try:
                    os.rename(filename, backup)                 
                except:
                    pass                                     
                print("Starting with empty grade book.")
                return []                                     
            
            except PermissionError:
                print(f"ERROR: Don't have permission to read {filename}!")
                print("Try running as administrator or check file permissions.")
                print("Starting with empty grade book.")
                return []  
            
            except Exception as e:
                print(f"ERROR: Unexpected error loading {filename}")
                print(f"Details: {e}")
                print("Starting with empty grade book.")
                return []


    def save_to_file(tasks, filename):
        try:
            
            if os.path.exists(filename):                      
                with open(filename, 'r') as f:
                    old_data = f.read()
                with open(filename + ".backup", 'w') as f:
                    f.write(old_data)
            
            with open(filename, 'w') as f:                     
                json.dump(tasks, f, indent=4)
            
            print(f"Data saved to {filename}")
            return True
            
        except Exception as e:
            print(f"Save failed: {e}")
            return False
        
    
    tasks = load_from_file(filename) 



    def show_menu():
        """Display the menu options"""
        print("\n" + "="*40)
        print("TO-DO LIST MANAGER")
        print("="*40)
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        print("="*40)


    def add_task(tasks):
        """Add a new task to the list"""
        task_name = input("Enter task: ").strip()
        
        if not task_name:  
            print(" Task cannot be empty!")
            return
        
        for task in tasks:
                if task['name'] == task_name:
                    print("You have already created this task.")
                    create_task = input("If you would like to create a duplicate task, type 'y'. Otherwise, type 'n' to cancel: ").lower()
                    if create_task == 'y':
                        print("The task has successfully been added to the list.")
                        break  
                    else:
                        print("Task not added.")
                        return  
        
        new_task = {
            "name": task_name,
            "completed": False
        }
        tasks.append(new_task)
        print(f"Sucessfully Added: {task_name}")

    def view_tasks(tasks):
        if not tasks:
            print("There are no tasks for you to view yet!")
            return
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            status = "Complete!" if task["completed"] else "Not Complete"
            print(f"{i}. {status} {task['name']}")

    def mark_task_as_complete(tasks):
        if not tasks:
            print("No tasks to complete!")
            return
        
        view_tasks(tasks)
        
        try:

            task_number = int(input("Enter the number of the task you would like to mark as complete: ")) - 1
            
            if 0 <= task_number < len(tasks):
                tasks[task_number]["completed"] = True
                print(f"✅ Task '{tasks[task_number]['name']}' has been marked as completed!")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_task(tasks):
        if not tasks:
            print("No tasks to remove.")
            return
        view_tasks(tasks)

        try:
            tasks_number = int(input("Please choose the task number to remove: ")) - 1
            if 0 <= tasks_number < len(tasks):
                remove = tasks.pop(tasks_number)
                print(f"Deleted task {remove['name']}")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please input a valid number")

    while True:
        show_menu()
        choice = input("Choose option (1-6): ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_as_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            confirm = input("Save & Exit? (y/n): ")
            if confirm.lower() == 'y':
                save_to_file(tasks, filename)
                print("Goodbye!")
                break
            else:
                print("Continuing..")

to_do_list()