# import re
#
#
# url = input("URL: ").strip()
#
# if matches := re.search(r"^(?:https?://)?(?:www\.)?\twitter\.com/(\w+)$", url, re.IGNORECASE):
#     print(f"Username: {matches.group(1)}")




# for _ in range(1, 5):
#     for _ in range(1):
#         print("* " * 8)
#     print(" *" * 8)

number: str = input("Enter number: ")

for c in number:
    print(f"{c}   ", end="")