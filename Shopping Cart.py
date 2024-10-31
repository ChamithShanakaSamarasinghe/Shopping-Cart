class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock -= quantity

class BillingSystem:
    def __init__(self):
        # Sample products
        self.products = {
            1: Product(1, "Laptop", 1000, 10),
            2: Product(2, "Mouse", 25, 100),
            3: Product(3, "Keyboard", 45, 50)
        }
        self.cart = {}

    def display_products(self):
        print("\nAvailable Products:")
        print("ID\tName\tPrice\tStock")
        for product_id, product in self.products.items():
            print(f"{product.product_id}\t{product.name}\t{product.price}\t{product.stock}")

    def add_to_cart(self, product_id, quantity):
        if product_id in self.products and self.products[product_id].stock >= quantity:
            if product_id in self.cart:
                self.cart[product_id] += quantity
            else:
                self.cart[product_id] = quantity
            self.products[product_id].update_stock(quantity)
            print(f"Added {quantity} {self.products[product_id].name}(s) to the cart.")
        else:
            print("Product not available or insufficient stock.")

    def display_cart(self):
        if not self.cart:
            print("\nCart is empty.")
            return
        
        print("\nItems in Cart:")
        total = 0
        print("Name\tQuantity\tPrice")
        for product_id, quantity in self.cart.items():
            product = self.products[product_id]
            price = product.price * quantity
            print(f"{product.name}\t{quantity}\t\t${price}")
            total += price
        print(f"Total: ${total}")

    def checkout(self):
        if not self.cart:
            print("Cart is empty. Cannot checkout.")
            return
        
        self.display_cart()
        print("\nCheckout successful!")
        self.cart.clear()

# Sample usage
def main():
    billing_system = BillingSystem()
    
    while True:
        print("\n1. Display Products\n2. Add to Cart\n3. View Cart\n4. Checkout\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            billing_system.display_products()
        elif choice == '2':
            try:
                product_id = int(input("Enter Product ID: "))
                quantity = int(input("Enter Quantity: "))
                billing_system.add_to_cart(product_id, quantity)
            except ValueError:
                print("Invalid input. Please enter valid product ID and quantity.")
        elif choice == '3':
            billing_system.display_cart()
        elif choice == '4':
            billing_system.checkout()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
