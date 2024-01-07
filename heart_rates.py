from datetime import date
class HeartRates:
    @classmethod
    def get(cls):
        while True:
            first = input("Enter firstname: ")
            if first:
                break

        while True:
            last = input("Enter lastname: ")
            if last:
                break

        while True:
            try:
                dob = input("Enter date of birth (yyyy-mm-dd): ")
                date_of_birth = date.fromisoformat(dob)
                break
            except ValueError:
                pass
        
        return cls(first, last, date_of_birth)

    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    def calculate_age(self):
        date_diff = date.today() - self.date_of_birth
        days: int = date_diff.days
        return f"{days // 365}"
    def max_heart_rate(self):
        return 220 - int(self.calculate_age())

    def target_heart_rate(self):
        ...


def main():
    person1 = HeartRates.get()
    print(person1.calculate_age())


if __name__ == "__main__":
    main()
