import json, os
class Contact: 
    def __init__(self, name, email, mobile):  
        self.name = name
        self.email = email 
        self.mobile = mobile
    def __str__(self):   
        return f"{self.name} ({self.email}) {self.mobile}"

class ContactBook:
    def __init__(self, name):  
        self.name = name    #What we are using to identify the user to the contact    
        self.contacts = {}     #Initialising the object to be storing the content within a dictionary    
    def save_storage(self, filename):   #Function where the values are going to be stored  
        data = []  #Content will be stored within a list of dictionaries many pieces of data stored in one
        for contact in self.contacts.values():   #identifies contact (singular) within the contacts dictionary   
            data.append({"name":  contact.name, "email": contact.email, "mobile": contact.mobile}) #All of the data stored under a single value within the contact
        try:
            if os.path.exists(filename):                            # Create backup of existing file BEFORE overwriting
                with open(filename, 'r') as f:
                    old_data = f.read()
                with open(filename + ".backup", 'w') as f:
                    f.write(old_data)
            
            with open(filename, 'w') as f:                
                json.dump(data, f, indent=4) # Now save new data
            
            print(f"Data saved to {filename}")
            return True
            
        except Exception as e:
            print(f"Save failed: {e}")
            return False
        
    def load_storage(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            for contact_data in data:
                contact = Contact(
                    contact_data["name"],
                    contact_data["email"],
                    contact_data["mobile"]
                )
                self.contacts[contact.name] = contact

            with open(filename + ".backup", 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Loaded data from {filename}")

        except FileNotFoundError:
            print("Contact list not found, Starting fresh!")
            return {}
        except json.JSONDecodeError:
            print(f"Corruption of your {filename} file")
            backup = filename + ".corrupted"
            print(f"Saving corrupted file as {backup}")   

            try:
                os.rename(filename, backup)             
            except:
                pass                                       
            print("Starting with a new contact list.")
            return {}  
        
    def add_contact(self, contact):
        self.contacts[contact.name] = contact    #OBJECT[individual contacts name] = contact variable
    
    def view_contact(self, name):       #o(1) lookup as we are getting the users data directly from the dictionary key "name" 
        if name in self.contacts:           #searches if the individual input is within the contacts dictionary
            contact = self.contacts[name]   #if it is then it will get the contacts name and display this as contact for call back 
            print(f"Name: {name} | Email: {contact.email} | Mobile: {contact.mobile}")  #name is displayed from input and the contact call back is now used to leverage the object .notation
        else:
            print(f"{name} could not be found within your contact list.")

            
    def view_all_contacts(self):
        if not self.contacts:   #if there are no contacts within the dictionary it will return a print message
            print("You have no stocks within your portfolio")
            return
        print("Current Contacts:")
        for name, contact in self.contacts.items():     #gets all of the data for the names within the contacts dictionary
            print(f"Name: {name} | Email: {contact.email} | Mobile: {contact.mobile}")  #prints the data with all of the contacts as we are getting the items
        print("="*40)

    def search_email(self, email):           #o(n)lookup (searching for email within a name loop as the email isnt the key)  # functionality is useless but learning code efficiency
        for name, contact in self.contacts.items():
            if contact.email == email:
                print(f"Email: {contact.email} | Name: {name} | Mobile: {contact.mobile}")
                print("="*40)
                return
        print(f"{email} could not be found within your contacts")
    

contacts_list = ContactBook("My Contacts")
contacts_list.load_storage("Contact.json")
while True:
    print("================== Contact Manager ==================")
    print("1.) Add Contact")
    print("2.) View Contact")
    print("3.) View All Contacts")
    print("4.) Remove Contact")
    print("5.) Search Email")
    print("6.) Exit")
    print("==============================")
    try:
        choice = int(input("Please enter from the menu (1-6): "))
        print("==============================")
    except ValueError:
        print("Enter valid integer")
        print("==============================")
    
    if choice == 1:
        name = input("Enter Contacts Name or 'B' to return: ").upper()
        if name == 'B':
            continue
        if not name.strip():
            print("This field cannot be left empty!")
            print("============================================")
            continue
        email = input("Please input the Contacts email: ")
        if not email.strip():
            print("This field cannot be left empty!")
            print("============================================")
            continue
        mobile = input("Please input the Contacts Mobile number: ")
        if not mobile.strip():
            print("This field cannot be left empty!")
            print("============================================")
            continue
        
        new_contact = Contact(name, email, mobile)
        contacts_list.add_contact(new_contact)
        contacts_list.save_storage("Contact.json")
    elif choice == 2:
        name = input("Enter the contacts name: ")
        if name == 'B':
            continue
        if not name.strip():
            print("This field cannot be left empty!")
            print("============================================")
            continue
        contacts_list.view_contact(name)
    elif choice == 3:
        contacts_list.view_all_contacts()
    elif choice == 4:
        name = input("Please input the Contacts name you would like removing: ")
        if name == 'B':
            continue
        if not name.strip():
            print("This field cannot be left empty!")
            print("============================================")
            continue
        confirm = input(f"Are you sure you would like to remove {name}?: ").lower()
        if confirm == "y": 
            del contacts_list.contacts[name]
            contacts_list.save_storage("Contact.json")
            print(f"Successfully removed {name} from your contacts!")
        else:
            print("Operation has been cancelled!")
            continue
    elif choice == 5:
        email = input("Please input the email to search: ")
        if email == 'B':
            continue
        contacts_list.search_email(email)

    elif choice == 6:
        Exit = input("Are you sure you would like to leave the application?: ").lower()
        if Exit == "y":
            contacts_list.save_storage("Contact.json")
            print("Thank you for using your contact book!")
            break
        else:
            print("Returning back to the application!")
