class BodyMassCalculator:
    bmi_info = """
    BMI VALUES
    Underweight: less than 18.5
    Normal:      between 18.5 and 24.9
    Overweight:  between 25 and 29.9
    Obese:       30 or greater
    """

    @classmethod
    def get_input(cls):
        print(f"{BodyMassCalculator.bmi_info}")
        while True:
            try:
                weight: int = int(input("Enter weight (Pounds): "))
                if weight > 0:
                    break
            except ValueError:
                pass

        while True:
            try:
                height: int = int(input("Enter height (inches): "))
                if height > 0:
                    break
            except ValueError:
                pass

        return cls(weight, height)

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    def get_bmi(self):
        return round(self.weight * 703 / self.height ** 2, 1)

    def __str__(self):
        return f"Your BMI is: {self.get_bmi()}"


def main():
    bmi = BodyMassCalculator.get_input()

    print(bmi)


if __name__ == "__main__":
    main()
