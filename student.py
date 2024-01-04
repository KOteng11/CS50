class Student:
    @classmethod
    def get(cls):
        while True:
            name: str = input("Name: ").strip()
            if name:
                break

        house: str = input("House: ")

        return cls(name, house)

    def __init__(self, name, house):
        self.name = name
        self.house = house

    @property # Getter
    def name(self):
        return self._name

    @name.setter # Setter
    def name(self, name):
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = Student.get()
    student.house = "Number Four Privet Drive"


if __name__ == "__main__":
    main()
