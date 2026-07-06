#Create a class Circle with attribute radius. Add methods area() and circumference(). (Use 3.14159 for pi.)
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14159 * self.radius