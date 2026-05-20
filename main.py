from services.product_service import ProductService
from services.cart_service import CartService

cart_service = CartService()


def show_products():
    products = ProductService.get_all_products()

    print("\n====== PRODUCTS ======")

    for product in products:
        print(product)


def add_to_cart():

    show_products()

    product_id = int(input("\nEnter product ID: "))
    quantity = int(input("Enter quantity: "))

    product = ProductService.find_product_by_id(product_id)

    if product is None:
        print("Product not found.")
        return

    if quantity > product.get_stock():
        print("Not enough stock.")
        return

    cart_service.add_to_cart(product, quantity)

    print("Product added to cart.")


def remove_from_cart():

    cart_service.show_cart()

    product_id = int(input("\nEnter product ID to remove: "))

    removed = cart_service.remove_from_cart(product_id)

    if removed:
        print("Product removed.")
    else:
        print("Product not found in cart.")


def main():

    while True:

        print("\n====== SMART SHOP ======")
        print("1. Show Products")
        print("2. Add To Cart")
        print("3. Show Cart")
        print("4. Remove From Cart")
        print("5. Clear Cart")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_products()

        elif choice == "2":
            add_to_cart()

        elif choice == "3":
            cart_service.show_cart()

        elif choice == "4":
            remove_from_cart()

        elif choice == "5":
            cart_service.clear_cart()
            print("Cart cleared.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()

