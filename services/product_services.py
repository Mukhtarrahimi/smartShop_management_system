from data.storage import products

class ProductService:
    @staticmethod
    def get_all_products():
        return products


    @staticmethod
    def find_product_by_id(product_id):
        for product in products:
            if product.id == product_id:
                return product
        
        return None

    @staticmethod
    def add_product(product):
        products.append(product)

    @staticmethod
    def remove_product(product_id):
        product = ProductService.find_product_by_id(product_id)

        if product in None:
            return False

        products.remove(product)
        return True