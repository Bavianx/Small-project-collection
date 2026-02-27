import json

#Brief Inventory system which allows users to add remove and view all of the stock within a system.


class Product:
    def __init__(self, product_id, name, price, stock_amount):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_amount = stock_amount
    
    def __str__(self):  #just allows you to print without error is terminal (controls what print(object) shows)
        return(f"{self.name} | {self.price} | {self.stock_amount}")
    

    def restock(self, amount):
        self.stock_amount += amount
    def sell_stock(self, amount):
        if amount < self.stock_amount:
            self.stock_amount-= amount
            if self.stock_amount <= 5:
                print("Low stock!")
        else:
            print(f"We do not have enough units {amount} units.")

def low_stock(Inventory):
    print("============ Low Stock Alert ===========")
    found_low_stock = False
    for product_id, product in Inventory.items():
        if product.stock_amount < 10:
            print(f"Product ID: {product_id} | Product: {product} | Stock Quantity: {product.stock_amount} remaining!")
            found_low_stock == True
    if not found_low_stock:
        print("Stock records are looking good!")
    print("="*40)


def View_all_stock(Inventory):
    if not Inventory:
        print(f"You have no products in stock!")
        return False
    print(f"Current Stock: ")
    for product_id, product in Inventory.items():
        print(f"Product ID: {product_id} | Product: {product}")
    print("="*40)

def save_to_file(Inventory, filename):
    data = {}
    
    for product_id, product in Inventory.items():
        data[product_id] = {
            "name": product.name,
            "price": product.price,
            "stock": product.stock_amount
        }
    
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"✓ Data saved to {filename}")


def load_from_file(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        Inventory = load_from_file(filename)
        
        Inventory = {}
        for product_id, product_data in data.items():
            product = Product(
                product_id,
                product_data["name"],
                product_data["price"],
                product_data["stock"]
            )
            Inventory[product_id] = product
        
        print(f"Loaded {len(Inventory)} products from {filename}")
        return Inventory
    
    except FileNotFoundError:
        print("No saved data found. Starting fresh!")
        return {}


def main():

    filename = "Inventory.json"

    Inventory = load_from_file(filename)


    while True:                                                                                
        print("="*15)
        print("1.) Add Product")
        print("2.) View All Stock")
        print("3.) Restock Product")
        print("4.) Sell Product")
        print("5.) Remove Product")
        print("6.) Inventory stock check")
        print("7.) Exit...")
        print("="*15)
        try: 
            choice = int(input("Please input a corresponding integer (1-6): "))
        except ValueError:
            print("Please enter a valid integer from the list")
            continue

        if choice == 1:
            product_id = input("Product ID: ")
            if product_id in Inventory:
                print("This product has already been added to the inventory system!")
                continue

            name = input("Product Name: ")
            price = int(input("Product Price:£ "))
            stock = int(input("stock quantity: "))

            Inventory[product_id] = Product(product_id, name, price, stock)
            print(f"You have successfull added {product_id} ({name}) to the inventory system!")
        elif choice == 2:
            View_all_stock(Inventory)
        elif choice == 3:
            product_id = input("Product ID for Restock: ")

            if product_id in Inventory:
                amount = int(input("How much are we restocking?: "))
                Inventory[product_id].restock(amount)
                print(f"Successfully added {amount} to {product_id}")
            else:
                print(f"Product {product_id} has not been found")
        elif choice == 4:
            product_id = input("Product ID for sale:")

            if product_id in Inventory:
                amount = int(input("How much are we selling?: "))
                Inventory[product_id].sell_stock(amount)
                print(f"Successfully sold {amount} for {product_id}")
            else:
                print(f"Product {product_id} has not been found")
        elif choice == 5:
            product_id = input("Please input the product ID to remove!: ")

            if product_id in Inventory:
                confirm = input(f"Are you sure you would like to remove {Inventory[product_id]} (y/n): ").lower()
                if confirm == "y":
                    del Inventory[product_id]
                    print(f"Successfully removed {product_id} from the Inventory System!")
                else:
                    print("Cancelled...")
        elif choice == 6:
            low_stock(Inventory)
        elif choice == 7:
            exit = input("Would you like to exit the Inventory System? (y/n): ")
            if exit == "y":
                save_to_file(Inventory, filename)
                print("Thank you for using the Inventory System!")
                break
            else:
                print("Continuing...")

main()

