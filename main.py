from services.product_service import ProductService
from services.cart_service import CartService
from services.auth_service import AuthService

cart_service = CartService()


def show_products():
    products = ProductService.get_all_products()

    print("\n====== PRODUCTS ======")

    for product in products:
        print(product)


def register():
    print("\n====== REGISTER ======")

    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")

    try:
        user = AuthService.register_customer(name, email, password)
        print("Registration successful.")
        print(user)

    except ValueError as error:
        print("Error:", error)


def login():
    print("\n====== LOGIN ======")

    email = input("Email: ")
    password = input("Password: ")

    user = AuthService.login(email, password)

    if user is None:
        print("Invalid email or password")
        return

    print("Login successful.")
    print("Welcome", user.name)


def add_to_cart():
    if not AuthService.is_customer():
        print("Only customers can add products to cart.")
        return

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
    product.reduce_stock(quantity)

    print("Product added to cart.")


def remove_from_cart():
    cart_service.show_cart()

    product_id = int(input("\nEnter product ID to remove: "))

    removed = cart_service.remove_from_cart(product_id)

    if removed:
        print("Product removed.")
    else:
        print("Product not found in cart.")


def show_users():
    if not AuthService.is_admin():
        print("Only admin can see users.")
        return

    print("\n====== USERS ======")

    for user in AuthService.get_all_users():
        print(user)


def customer_menu():
    while True:
        print("\n====== CUSTOMER MENU ======")
        print("1. Show Products")
        print("2. Add To Cart")
        print("3. Show Cart")
        print("4. Remove From Cart")
        print("5. Clear Cart")
        print("6. Logout")

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
            AuthService.logout()
            print("Logged out.")
            break

        else:
            print("Invalid choice.")


def admin_menu():
    while True:
        print("\n====== ADMIN MENU ======")
        print("1. Show Products")
        print("2. Show Users")
        print("3. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            show_products()

        elif choice == "2":
            show_users()

        elif choice == "3":
            AuthService.logout()
            print("Logged out.")
            break

        else:
            print("Invalid choice.")


def main_menu():
    while True:
        print("\n====== SMART SHOP ======")
        print("1. Register")
        print("2. Login")
        print("3. Show Products")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()

        elif choice == "2":
            login()

            if AuthService.is_admin():
                admin_menu()

            elif AuthService.is_customer():
                customer_menu()

        elif choice == "3":
            show_products()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main_menu()