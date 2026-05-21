from models.product import Product
from models.user import Admin, Customer

products = [
    Product(1, "Laptop", 10000, 5, "Electronics"),
    Product(2, "Phone", 8500, 10, "Mobile"),
    Product(3, "Keyboard", 760, 20, "Accessories"),
    Product(4, "Mouse", 450, 30, "Accessories"),
    Product(5, "Monitor", 3200, 8, "Electronics"),
    Product(6, "Headphone", 1200, 15, "Gaming"),
    Product(7, "Smart Watch", 2500, 12, "Mobile"),
]
users = [
    Admin(1, 'Admin', 'admin@gmail.com', 'admin123'),
    Customer(2, 'Mukhtar', 'mukhtarrahimi@gmail.com', 'mukhtar123')
]