import json

book = {}

book['tom'] = {
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': '98989898'
}

book['bob'] = {
    'name': 'bob',
    'address': '1 green street, NY',
    'phone': '23232323'
}

# Takes the dictionary object and dumps it as a string, so it can be converted into json format.
s = json.dumps(book)

with open("C://Users//Kostas//PycharmProjects//learningBasics310//json//book.txt", "w") as f:
    f.write(s)
