class CartItem:
    def __init__(self, product, quantity=1):
        self.product = product
        self.quantity = quantity

    def increase_quantity(self, quantity=1):
        self.quantity += quantity

    def decrease_quantity(self, quantity=1):
        self.quantity -= quantity

    def get_subtotal(self):
        return self.product.get_price() * self.quantity

    def __str__(self):
        return (
            f"{self.product.name} | "
            f"Price: {self.product.get_price()} | "
            f"Quantity: {self.quantity} | "
            f"Subtotal: {self.get_subtotal()}"
        )