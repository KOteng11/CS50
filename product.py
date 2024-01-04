# # Calculate the product of three integers
#
#
# x = int(input("Enter first integer: "))  # Prompt user for the first integer
# y = int(input("Enter second integer: "))  # Prompt user for the second integer
# z = int(input("Enter third integer: "))  # Prompt user for the third integer
#
# result = x * y * z  # save the product of all three integers in result
#
# print(f"Product is {result}")

while True:
    try:
        number_1: int = int(input("Number 1: "))  # prompt user for the first integer
        break
    except ValueError:
        pass

while True:
    try:
        number_2: int = int(input("Number 2: ") ) # prompt user for the second integer
        break
    except ValueError:
        pass

print(f"sum: {number_1 + number_2}")
print(f"difference: {number_1 - number_2}")
print(f"product: {number_1 * number_2}")
print(f"quotient: {number_1 / number_2}")


