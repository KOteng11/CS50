class BodyMassCalculator:
    @classmethod
    def display_metrics(cls):
        print("BMI VALUES\n"
              "Underweight: less than 18.5\n"
              "Normal:      between 18.5 and 24.9\n"
              "Overweight:  between 25 and 29.9\n"
              "Obese:       30 or greater\n")

    @classmethod
    def get_input(cls):
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
    BodyMassCalculator.display_metrics()
    bmi = BodyMassCalculator.get_input()

    print(bmi)


if __name__ == "__main__":
    main()
