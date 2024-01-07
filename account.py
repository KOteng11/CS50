# account.py
# Account class with a constructor to validate and
# initialize instance variable balance of type float

from datetime import datetime
import re


class Account:
    @classmethod
    def get(cls):
        print("New Account\n")
        while True:
            name: str = input("Enter your name: ").strip().title()
            if matches := re.search(r"^([a-zA-Z]+) ([a-zA-Z]+ )?([a-zA-Z]+)$", name, re.IGNORECASE):
                break
            else:
                print("name is required.")

        while True:
            try:
                date: str = input("Enter date of birth (yyyy-mm-dd): ").strip()
                date_of_birth = datetime.fromisoformat(date)
                break
            except ValueError:
                pass

        while True:
            try:
                initial_deposit: float = float(input("Enter initial deposit: $"))
                if initial_deposit > 0:
                    break
            except ValueError:
                pass
        return cls(matches.group(1), matches.group(2), matches.group(3), date_of_birth, initial_deposit)

    def __init__(self, first_name: str, middle_name: str, last_name: str, date_of_birth: datetime, initial_deposit: float):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.balance = initial_deposit

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name: str = first_name

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name: str):
        self._middle_name: str = middle_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name: str = last_name

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: datetime):
        self._date_of_birth: datetime = date_of_birth

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance: float):
        self._balance: float = balance

    def get_age(self):
        date_diff = datetime.today() - self.date_of_birth
        days: int = date_diff.days
        return f"{days // 365}"

    def deposit(self):
        while True:
            try:
                amount: float = float(input("Enter amount to deposit: $").strip())
                if amount > 0:
                    break
            except ValueError:
                pass
        self.balance += amount

    def withdraw(self):
        while True:
            try:
                amount: float = float(input("Enter amount to withdraw: $").strip())
                if amount > 0:
                    break
            except ValueError:
                pass
        self.balance -= amount

    def __str__(self):
        print("Account Details")
        print("**********************")
        if not self.middle_name:
            return f"Name: {self.first_name} {self.last_name}\n" \
                   f"Balance: {self.balance}"
        else:
            return f"Name: {self.first_name} {self.middle_name} {self.last_name}\n" \
                   f"Balance: {self.balance}"


