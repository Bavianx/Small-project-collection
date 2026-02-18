import json, os
def library_catalogue_system():

    filename = "Library_catalogue.json"

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
        
    catalogue = load_from_file(filename) 


    def add_book(catalogue, ISBN, Title, Author):
        if ISBN in catalogue:
            print(f"Book {ISBN} already exists!")
            return False

        catalogue[ISBN] = {
            "Title": Title,
            "Author": Author,
            "Available": True
        }
        print(f"Thank you for adding {ISBN} - {Title} to the catalogue!")
        save_to_file(catalogue, filename)
        print("=========================================")
    

    def view_all_books(catalogue):
        if not catalogue:
            print("There are no books in the catalogue")
            return

        for ISBN, book in catalogue.items():
            status = "Available" if book.get("Available", True) else "Checked Out"   
            print(f"ISBN: {ISBN} | {book['Title']} by {book['Author']} | {status}")

 
    def search_book(catalog, search_term):
        matches = []
        for ISBN, book in catalog.items():  # Saying if the searched book is under any of nested values it will match and return the book either by the title, author or ISBN #.
            if (search_term.lower() in book["Title"].lower() or
                search_term.lower() in book["Author"].lower() or
                search_term == ISBN):
                matches.append((ISBN, book))
        return matches
            
    def check_out_book(catalogue, ISBN):
        if ISBN not in catalogue:
            print("This book is not in our catalogue, maybe you should add it.")
            return False
        book = catalogue[ISBN]

        if not book["Available"]:
            print("This book is not currently Available")
            return False
        
        confirm = input(f"Check out book {book['Title']}? (y/n): ")
        if confirm.lower() == "y":

            book['Available'] = False 
            print(f"Great! Enjoy reading {book['Title']}!")
            save_to_file(catalogue, filename)
            return True
        else:
            print("Cancelled transaction..")
            return False
            

    def return_book(catalogue, ISBN):
        if ISBN not in catalogue:
            print("This book was not in our catalogue!")
            return False
        
        book = catalogue[ISBN]
        if book['Available']:
            print(f"'{book['Title']}' wasn't checked out!")
            return None
        
        confirm = input(f"Return '{book['Title']}'? (y/n): ")
        if confirm.lower() == "y":

            book['Available'] = True 
            print(f"Thanks for returning '{book['Title']}'!")
            save_to_file(catalogue, filename)
            return True
        else:
            print("Cancelled transaction..")
            return False
        


    while True:
        print("========== Library Catalog ==========")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Check Out Book")
        print("5. Return Book")
        print("6. Save & Exit")
        print("=====================================")

        try:
            choice = int(input("Please choose one of the menu paths: "))
        except ValueError:
            print("Please input a valid integer")
            print("============================================")
            continue

        if choice == 1:
            ISBN = input("Please input the Books ISBN  : ") 
            Title = input("Please enter the Books Title: ")
            Author = input("Please enter the Books Author: ")
            add_book(catalogue, ISBN, Title, Author)
        elif choice == 2:
            view_all_books(catalogue)
        elif choice == 3: 
            search_term = input("Search (Title/Author/ISBN): ")
            matches = search_book(catalogue, search_term)
            
            if not matches:
                print("No books found!")
            else:
                print(f"Found {len(matches)} book(s):")
                for ISBN, book in matches:
                    status = "Available" if book["Available"] else "Checked Out"
                    print(f"ISBN: {ISBN} | {book['Title']} by {book['Author']} | {status}")
            print("=========================================")

        elif choice == 4:
            ISBN = input("Please input the ISBN of the book: ")
            check_out_book(catalogue, ISBN)
            print("=========================================")
        elif choice == 5:
            ISBN = input("Please input the ISBN of the book: ")
            return_book(catalogue, ISBN)     
            print("=========================================")
        elif choice == 6:
            leave = input("Are you sure you would like to Save & Exit? (y/n): ")
            if leave.lower() == "y":
                print("Thank you for stopping by!")
                save_to_file(catalogue, filename)
                print("=========================================")
                break
            else:
                print("Great! what else can we help you with?")
                continue

library_catalogue_system()