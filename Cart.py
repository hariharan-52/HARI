class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product):
        if product.id in self.items:
            self.items[product.id]['quantity'] += 1
        else:
            self.items[product.id] = {'product': product, 'quantity': 1}

    def remove_product(self, product):
        if product.id in self.items:
            if self.items[product.id]['quantity'] > 1:
                self.items[product.id]['quantity'] -= 1
            else:
                del self.items[product.id]

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        print("Your Cart:")
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            print(f"{product.name} - ${product.price} x {quantity}")

    def checkout(self):
        if not self.items:
            print("Your cart is empty. Add some products before checking out.")
            return
        total = sum(item['product'].price * item['quantity'] for item in self.items.values())
        self.items = {}
        print(f"Checkout successful. Total amount: ${total:.2f}")
		# ecommerce.py (continued)

def main():
    products = [
        Product(1, 'Product 1', 10.00),
        Product(2, 'Product 2', 20.00),
        Product(3, 'Product 3', 30.00)
    ]
    cart = Cart()

    while True:
        print("\n1. View Products\n2. View Cart\n3. Add to Cart\n4. Remove from Cart\n5. Checkout\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nProducts:")
            for product in products:
                print(f"{product.id}. {product.name} - ${product.price}")
        elif choice == '2':
            cart.view_cart()
        elif choice == '3':
            product_id = int(input("Enter product ID to add to cart: "))
            product = next((p for p in products if p.id == product_id), None)
            if product:
                cart.add_product(product)
                print(f"{product.name} added to cart.")
            else:
                print("Invalid product ID.")
        elif choice == '4':
            product_id = int(input("Enter product ID to remove from cart: "))
            product = next((p for p in products if p.id == product_id), None)
            if product:
                cart.remove_product(product)
                print(f"{product.name} removed from cart.")
            else:
                print("Invalid product ID.")
        elif choice == '5':
            cart.checkout()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
