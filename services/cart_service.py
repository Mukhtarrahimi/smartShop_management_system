from models.cart import Cart


class CartService:
    def __init__(self):
        self.cart = Cart()

    def add_to_cart(self, product, quantity=1):
        self.cart.add_product(product, quantity)

    def remove_from_cart(self, product_id):
        return self.cart.remove_product(product_id)

    def show_cart(self):
        self.cart.show_cart()

    def clear_cart(self):
        self.cart.clear_cart()