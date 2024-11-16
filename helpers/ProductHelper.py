import os
from models.Product import Product

class ProductHelper:
    @staticmethod
    def create_item_from_text(file_path):
        products = []
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                for line in file:
                    name, price, quantity = line.strip().split(',')
                    product = Product(name, float(price), int(quantity))
                    products.append(product)
        else:
            print(f"File {file_path} not found.")
        return products

    @staticmethod
    def get_total_balance(products):
        total = sum(product.get_total_price() for product in products)
        return total * 1.2  # %20 KDV ekleniyor
