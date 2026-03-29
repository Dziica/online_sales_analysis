from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

p1 = Product("Laptop", 1000, 2)
p2 = Product("Mouse", 20, 10)
p3 = Product("Keyboard", 50, 5)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

cart = Cart()

# dodavanje 3 proizvoda u korpu
cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.add_to_cart(p3)

print("\nCART CONTENT:")
cart.display_cart()

print("TOTAL CART VALUE:", cart.total_price())
