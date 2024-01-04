"""
Compare integers using if statements, relational operations and equality operators.
"""

# prompt user for the first number
number_1 = int(input("Enter number 1: "))

# prompt user for the second number
number_2 = int(input("Enter number 2: "))

if number_1 < number_2:
    print(f"{number_1} < {number_2}")
elif number_1 > number_2:
    print(f"{number_1} > {number_2}")
else:
    print(f"{number_1} == {number_2}")