class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius


    def set_radius(self, radius):
        self.radius = new_radius
        return new_radius

C1 = Circle(10.0)
print("Начальный радиус:", C1.get_radius())

user_input = input("Введите новый радиус: ")
new_radius = float(user_input)

C1.set_radius(new_radius)
print("Новый радиус:", C1.get_radius())
