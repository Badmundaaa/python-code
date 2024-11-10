import os
import product as pro

class ProductManager:
    def __init__(self, filename):
        self.filename =filename
        self.products = []
        self.load_products()

    def add_product(self, name, product,):
        # for product in self.products:
        #     if product.name == name:
        #         print("product name already exist")
        #     else:
        #         False
        self.products.append(product)
        self.save_products()
        
    def save_products(self):
        with open(self.filename, "w") as f:
            for product in self.products:
                f.write(str(product) + '\n')

    
        
    def load_products(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                for line in f:
                    name, price, quantity = line.strip().split(",")
                    product =pro.Product(name,float(price),int(quantity))
                    self.products.append(product)

    
    def display_products(self):
        if not self.products:
            print("no product found.!!")
        else:
            print("product list")
            print(self.products.index("name"))
            for i, products in enumerate(self.products ,start=1):
                print(f"{i}.Name:{products.name},price:{products.price},Quantity:{products.quantity}")



    def sell_products(self, name, amount):
        for product in self.products:
            if product.name == name:
                return product.sell(amount)
        print(f"product{name} not found")
        return False

    def restock_product(self, name, amount):
        for product in self.products:
            if product.name == name:
                return product.restock(amount)
        print(f"product {name} not found.")
        return False
        
    # def delete_product(self, name):
    #     if name in self.products:
    #         del self.products[name]
    #         index=self.products.index(name)
    #         del self.products[index]
    #         self.save_products()
    #         print(f"product {name} deleted.")
    #         print(index)
    #     else:
    #         print(f"product {name}, not deleted.")
    #         print(index)

    def delete_product(self,name):
        for index,product in enumerate(self.products):
            if product.name==name:
                del self.products[index]
                self.save_products()
                print(f"product {name} deleted successfully.")
                return True
        print(f"product {name} not found, not deleted.")
        return False

