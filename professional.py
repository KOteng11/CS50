class Coordinate:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y


cordinate = Coordinate(3, 4)

def to_jaden(string):
    final_word = []
    for word in string.split(" "):
        word = word.capitalize()
        final_word.append(word)
    return " ".join(final_word)

quote = "three Men, Six Options, Don't Choose."
print(to_jaden(quote))