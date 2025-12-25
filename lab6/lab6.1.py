class UserAccaunt:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, new_password):
        self.password = new_password
        return new_password

    def check_password(self, input_password):
        if input_password == self.password: print("true")
        else: print("false")


U = UserAccaunt("Bob", "Bob@gmail.com", "1234")



user_input = input("Введите новый пароль: ")
U.set_password(user_input)

user_input2 = input("password?")
U.check_password(user_input2)