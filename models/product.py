class Product:
    def __init__(self, product_id, name, price, stock, category):
        self.id = product_id
        self.name = name
        self.__price = price
        self.__stock = stock
        self.category = category

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price <= 0:
            raise ValueError('price must be positive')

        self.__price = new_price
    
    def get_stock(self):
        return self.__stock

    def set_stock(self, quantity):
        if quantity < 0:
            raise ValueError('quantity must be positive')

        if quantity > self.__stock:
            raise ValueError('not enough stock')
        
        self.__stock -= quantity

    def show_info(self):
        return f'ID: {self.id} | Name: {self.name} | Price: {self.__price} | Stock: {self.__stock} | Category: {self.category}'


    def __str__(self):
        return self.show_info()