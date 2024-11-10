import os
import product as pro
import productmanager as pm



def main():
    filename = 'product.txt'
    manager = pm.ProductManager(filename)

    while True:
        print("\n options:")
        print("1.add product")
        print("2.view product")
        print("3.sell product")
        print("4.restock")
        print("5.delete")
        print("6.exists")


        choice = input("choose an option:")
        if choice == "1":
            name = input("enter product name:")
            price = float(input("enter product price:"))
            quantity = int(input("enter product quantity:"))
            product = pro.Product(name, price, quantity)
            manager.add_product(name, product)
            if product.name == name:
                print("product already exist")
            else:
                print(f"Added product: {product}")

        elif choice == "2":
            manager.display_products()
            

        elif choice == "3":
            name=input("enter product name")
            amount= int(input("enter quantity to sell:"))
            if manager.sell_products(name, amount):
                print(f"sold {amount} of {name}.")
                manager.save_products()
            else:
                print(f"failed o sell {amount} of {name}.")
            

        elif choice == "4":
            name=input("enter product name")
            amount= int(input("enter quantity to restock:"))
            if manager.restock_product(name, amount):
                print(f"restock {amount} of {name}.")
                manager.save_products()
            else:
                print(f"failed to restock {amount} of {name}")

       
        elif choice =="5":
            name=input("enter the product u want to delete")
            if manager.delete_product(name):
                print(f"product {name} deleted succesfully")
            else:
                print(f"product{name}not found in the list")
            
       
        elif choice =="6":
            print("existing...")
            break
            

        else:
            print("invalid option. pls try again")

if __name__ == "__main__":
    main()