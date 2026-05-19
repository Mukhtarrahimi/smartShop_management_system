from models.cart_item import CartItem

class Cart:
    def __init__(self):
        self.items = []
    
    def add_product(self, product, quantity=1):
        for item in self.items:
            if item.product.id == product.id:
                item.increase_quantity(quantity)
                return

            
        cart_item = CartItem(product, quantity)
        self.items.append(cart_item)

    def remove_product(self, product_id):
        for item in self.items:

            if self.product.id == product_id:
                self.items.remove(item)
                return True

        return False

    def clear_cart(self):
        self.items.clear()

    def calculate_total(self):
        total = 0

        for item in self.items:
            total += item.get_subtotal()

        return total


    def apply_discount(self):

        total = self.calculate_total()
        if total >= 10000:
            return total * 0.10

        return 0

    def get_final_price(self):
        
        total = self.calculate_total()
        discount = self.apply_discount()

        return total - discount

    
    def show_cart(self):
        if len(self.items) == 0:
            print('\ncart is empty')
            return
        print('\n ==== your cart ====')

        for item in self.items:
            print(item)

        print('------------------')
        print('total: ', self.calculate_total())
        print('discount: ', self.apply_discount())
        print('final price: ', self.get_final_price())