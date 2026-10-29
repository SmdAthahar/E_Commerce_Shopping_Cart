from product import Product
from shopping_cart import ShoppingCart


# Create five products

product1 = Product(1, "Laptop", "Electronics", 65000, 2)
product2 = Product(2, "Phone", "Electronics", 25000, 3)
product3 = Product(3, "Mouse", "Accessories", 800, 5)
product4 = Product(4, "Keyboard", "Accessories", 1200, 4)
product5 = Product(5, "Headphones", "Electronics", 2000, 0)


products = [product1, product2, product3, product4, product5]

cart = ShoppingCart()


while True:

    print("\n======= E-COMMERCE SHOPPING CART =======")
    print("1. View Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. Calculate Total")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\n======= AVAILABLE PRODUCTS =======")

        for product in products:
            print(
                "ID:", product.product_id,
                "| Name:", product.name,
                "| Category:", product.category,
                "| Price: Rs.", product.price,
                "| Stock:", product.stock
            )

    elif choice == "2":

        try:
            product_id = int(input("Enter product ID to add: "))

            selected_product = None

            for product in products:
                if product.product_id == product_id:
                    selected_product = product
                    break

            if selected_product is None:
                print("Invalid product ID.")

            else:
                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than zero.")

                elif quantity > selected_product.stock:
                    print("Not enough stock available.")

                else:
                    for i in range(quantity):
                        cart.add_product(selected_product)

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":

        try:
            product_id = int(input("Enter product ID to remove: "))
            cart.remove_product(product_id)

        except ValueError:
            print("Please enter a valid product ID.")

    elif choice == "4":

        cart.display_cart()

    elif choice == "5":

        cart.calculate_total()

    elif choice == "6":

        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice. Please select from 1 to 6.")
