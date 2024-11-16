from helpers.ProductHelper import ProductHelper
from models.Product import Product

if __name__ == "__main__":
    # Örnek ürün oluşturma
    product1 = Product("Comp", 750, 3)
    product2 = Product("Tablet", 500, 2)
    
    print(f"{product1} - Total Price: {product1.get_total_price()}")
    print(f"{product2} - Total Price: {product2.get_total_price()}")

    # Products.txt dosyasını okuma
    products = ProductHelper.create_item_from_text("Products.txt")
    print("Total balance with VAT:", ProductHelper.get_total_balance(products))
