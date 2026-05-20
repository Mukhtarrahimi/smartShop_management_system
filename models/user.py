class User:
    def __init__(self, user_id, name, email, password, role):
        self.id = user_id
        self.name = name
        self.email = email
        self.__password = password
        self.role = role


    def check_password(self, password):
        return self.__password == password

    def change_password(self, old_password, new_password):
        if not self.change_password(old_password):
            raise ValueError('old password is incorrect')

        if len(new_password) < 8:
            raise ValueError('password must be least at 8 character')

        self.__password = new_password


    def show_info(self):
        return f'id: {self.user_id} | name: {self.name} | email: {self.email} | role: {self.role}'

    def __str__(self):
        return self.show_info()


class Customer(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password, 'customer')
        self.orders = []


def Admin(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password, 'admin')
