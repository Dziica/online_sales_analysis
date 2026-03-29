from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

p1 = Product("Phone", 800, 1)
p2 = Product("Headphones", 100, 3)
p3 = Product("Monitor", 300, 2)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

cart = Cart()
cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.add_to_cart(p3)

print("CART TOTAL:", cart.total_price())
