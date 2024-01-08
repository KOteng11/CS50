# def square_digits(num):
#     numbers: list = []
#
#     str_num: str = str(num)
#     for c in str_num:
#         square = int(c) ** 2
#         numbers.append(str(square))
#     return "".join(numbers)
#
#
# print(square_digits(9119))

def number(bus_stops):
    total = 0
    for people in bus_stops:
        people_remaining = people[0] - people[1]
        total += people_remaining

    return total

print(number([[10,0],[3,5],[5,8]]))