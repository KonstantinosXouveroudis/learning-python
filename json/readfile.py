import json

f = open("C:\\Users\\Kostas\\PycharmProjects\\learning-python\\json\\book.txt", "r")
s = f.read()

book = json.loads(s)  # loads = load string. Converts it into a dictionary.
book_type = type(book)
print(f"Type of book: {book_type}")
print(book)

print(f"Bob's phone number is {book['bob']['phone']}")

for person in book:
    print(book[person])

