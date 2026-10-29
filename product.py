class Product:

    def __init__(self, product_id, name, category, price, stock):

        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def display_product(self):

        print("Product ID:", self.product_id)
        print("Product Name:", self.name)
        print("Category:", self.category)
        print("Price: Rs.", self.price)
        print("Available Stock:", self.stock)