from product import Product
from product_manager import ProductManager

manager = ProductManager()

# Dodavanje proizvoda
p1 = Product("Laptop", 1000, 2)
p2 = Product("Mouse", 20, 10)
p3 = Product("Keyboard", 50, 5)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# Prikaz
manager.display_products()

# Ukupna vrednost
print("Total inventory value:", manager.total_value())
