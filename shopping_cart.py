class ShoppingCart:

    def __init__(self):

        self.cart = []

    def add_product(self, product):

        if product.stock <= 0:

            print(product.name, "is out of stock.")
            return

        product.stock = product.stock - 1

        self.cart.append(product)

        print(product.name, "added to cart successfully.")

    def remove_product(self, product_id):

        for product in self.cart:

            if product.product_id == product_id:

                product.stock = product.stock + 1

                self.cart.remove(product)

                print(product.name, "removed from cart.")
                return

        print("Product not found in cart.")

    def display_cart(self):

        if len(self.cart) == 0:

            print("Your shopping cart is empty.")
            return

        print()
        print("======= SHOPPING CART =======")

        for product in self.cart:

            print(
                product.name,
                "- Rs.",
                product.price
            )

        print("=============================")

    def calculate_total(self):

        total = 0

        for product in self.cart:

            total = total + product.price

        print("Total Amount: Rs.", total)

        return total
