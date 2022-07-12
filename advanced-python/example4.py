class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        result = self.radius**2
        result = result * Circle.pi

        return result

    def perimeter(self):
        return 2 * self.radius * Circle.pi

    def double_radius(self):
        self.radius = self.radius * 2
        print(f'Radius has been doubled to {self.radius}')

    def multiply_radius(self, number):
        self.radius = self.radius * number
        print(f'Radius has been changed to {self.radius}')


my_circle = Circle(4)
my_circle.multiply_radius(20)
# my_circle.double_radius()
# print(my_circle.radius)
# my_circle.double_radius()
# print(my_circle.radius)
# print(my_circle.area)
# print(my_circle.area())
# print(my_circle.perimeter())
