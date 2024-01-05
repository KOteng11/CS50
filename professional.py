def some_calculation(x: int | float, y: int | float) -> int | float:
    return (x + y) ** 2


print(some_calculation(10, 20))
print(some_calculation(10.78, 8.91))
