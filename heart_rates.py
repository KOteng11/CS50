from datetime import date


class HeartRates:
    GENDER_LIST = ["male", "female"]

    @classmethod
    def get(cls):
        while True:
            first: str = input("Enter firstname: ").strip().capitalize()
            if first:
                break

        while True:
            last: str = input("Enter lastname: ").strip().capitalize()
            if last:
                break

        while True:
            gender: str = input("Enter gender: ").strip().lower()
            if gender in HeartRates.GENDER_LIST:
                break

        while True:
            try:
                dob: str = input("Enter date of birth (yyyy-mm-dd): ").strip()
                date_of_birth: date = date.fromisoformat(dob)
                break
            except ValueError:
                pass

        while True:
            try:
                height: float = float(input("Enter height (Inches): "))
                if height > 0:
                    break
            except ValueError:
                pass

        while True:
            try:
                weight: int = int(input("Enter weight (Pound): "))
                if weight > 0:
                    break
            except ValueError:
                pass

        return cls(first, last, gender, date_of_birth, height, weight)

    def __init__(self, first_name: str, last_name: str, gender: str, date_of_birth: date, height: float, weight: int):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.gender: str = gender
        self.date_of_birth: date = date_of_birth
        self.height: float = height
        self.weight: int = weight

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        self._last_name = last_name

    @property
    def gender(self) -> str:
        return self._gender

    @gender.setter
    def gender(self, gender: str) -> None:
        self._gender = gender

    @property
    def date_of_birth(self) -> date:
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: date):
        self._date_of_birth = date_of_birth

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: float) -> None:
        self._height = height

    @property
    def weight(self) -> int:
        return self._weight

    @weight.setter
    def weight(self, weight: int) -> None:
        self._weight = weight

    def calculate_age(self):
        date_diff = date.today() - self.date_of_birth
        days: int = date_diff.days
        return f"{days // 365}"

    def max_heart_rate(self):
        return 220 - int(self.calculate_age())

    def target_heart_rate(self):
        min_target_heart_rate = round((50 / 100) * self.max_heart_rate())
        max_target_heart_rate = round((85 / 100) * self.max_heart_rate())

        return {"min": min_target_heart_rate, "max": max_target_heart_rate}

    def calculate_bmi(self) -> float:
        return round(self.weight * 703 / self.height ** 2, 1)

    def __str__(self):
        return (
            f"\nName: {self.first_name} {self.last_name}\n"
            f"Gender: {self.gender.capitalize()}\n"
            f"Date of Birth: {self.date_of_birth}\n"
            f"Age: {self.calculate_age()}\n"
            f"Maximum Heart Rate: {self.max_heart_rate()}\n"
            f"Target Heart Rate: {self.target_heart_rate()['min']}-{self.target_heart_rate()['max']} bpm\n"
            f"Body Mass Index: {self.calculate_bmi()}"
        )


def main():
    person1 = HeartRates.get()
    print(person1)


if __name__ == "__main__":
    main()
