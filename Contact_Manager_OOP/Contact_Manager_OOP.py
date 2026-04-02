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
            if os.path.exists(filename):           # Create backup of existing file BEFORE overwriting
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
        
    def add_contact(self, contact):
        self.contacts[contact.name] = contact    #OBJECT[individual contacts name] = contact variable
    
    def remove_contact(self, name):
        if name in self.contacts:       # checks for the user input within the object contacts dictionary
            del self.contacts[name]     #If the name is found it deletes it from the contacts leveraging the name input 
            print(f"Successfully removed {name} from your contacts")
        else:
            print(f"{name} has not been found within your contacts!")

contacts_list = ContactBook("My Contacts")
while True:
    print("================== Contact Manager ==================")
    print("1.) Add Contact")
    print("2.) View Contact")
    print("3.) View All Contacts")
    print("4.) Remove Contact")
    print("5.) Exit")
    print("==============================")
    try:
        choice = int(input("Please enter from the menu (1-5): "))
        print("==============================")
    except ValueError:
        print("Enter valid integer")
        print("==============================")
    
    if choice == 1:
        name = input("Enter Contacts Name: ")        #Finish with error handling across all 3 inputs 
        print("==============================")
        email = input("Please input the Contacts email: ")
        print("==============================")
        mobile = input("Please input the Contacts Mobile number: ")
        print("==============================")
        new_contact = Contact(name, email, mobile)
        contacts_list.add_contact(new_contact)
    elif choice == 2:            #Finish the rest of these off 
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
