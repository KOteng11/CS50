class Circle:
    PI = 3.14159

    @classmethod
    def get_input(cls):
        while True:
            try:
                radius = int(input("Enter Radius: "))
                if radius > 0:
                    break
            except ValueError:
                pass

        return cls(radius)

    def __init__(self, radius):
        self.radius = radius

    # Getter
    @property
    def radius(self):
        return self._radius

    # Setter
    @radius.setter
    def radius(self, radius):
        self._radius = radius

    def get_diameter(self):
        return 2 * self.radius

    def get_circumference(self):
        return 2 * Circle.PI * self.radius

    def get_area(self):
        return Circle.PI * self.radius ** 2


def main():
    circle = Circle.get_input()

    print(circle.get_diameter())
    print(circle.get_circumference())
    print(circle.get_area())


if __name__ == "__main__":
    main()
