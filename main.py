from services.product_service import ProductService


def show_products():
    products = ProductService.get_all_products()

    print("\n--- Product List ---")

    for product in products:
        print(product)


def main():
    while True:
        print("\n====== SmartShop ======")
        print("1. Show Products")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_products()

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


main()