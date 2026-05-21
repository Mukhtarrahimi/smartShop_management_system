from data.storage import users
from models.user import Customer
from utils.validators import validate_email, validate_password, validate_name


class AuthService:
    current_user = None

    @staticmethod
    def get_all_users():
        return users

    @staticmethod
    def find_user_by_email(email):
        for user in users:
            if user.email == email:
                return user
        return None

    @staticmethod
    def register_customer(name, email, password):
        if not validate_name(name):
            raise ValueError("Name must be at least 2 characters")

        if not validate_email(email):
            raise ValueError("Invalid email")

        if not validate_password(password):
            raise ValueError("Password must be at least 8 characters")

        existing_user = AuthService.find_user_by_email(email)

        if existing_user is not None:
            raise ValueError("Email already exists")

        new_id = len(users) + 1

        customer = Customer(new_id, name, email, password)

        users.append(customer)

        return customer

    @staticmethod
    def login(email, password):
        user = AuthService.find_user_by_email(email)

        if user is None:
            return None

        if not user.check_password(password):
            return None

        AuthService.current_user = user

        return user

    @staticmethod
    def logout():
        AuthService.current_user = None

    @staticmethod
    def is_authenticated():
        return AuthService.current_user is not None

    @staticmethod
    def is_admin():
        return AuthService.current_user is not None and AuthService.current_user.role == "admin"

    @staticmethod
    def is_customer():
        return AuthService.current_user is not None and AuthService.current_user.role == "customer"