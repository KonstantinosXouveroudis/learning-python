"""
List: []
Dictionary: {}
Tuple: ()
"""


tel = {"tom": 7326789820, "rob": 7325730239, "joe": 732092323}  # Dictionary
ran = ("tom", 7326789820, "new york")


def dictionary_test():
    print(tel)
    print("Tom's number: ", tel["tom"])

    tel["sam"] = 7395679879
    print("\nAfter adding Sam:", tel)

    del tel["sam"]
    print("After deleting Sam:", tel, "\n")

    for key in tel:
        print("Key:", key, "Value: ", tel[key])

    print("\nDifferent way:")
    for k, v in tel.items():
        print("Key:", k, "Value: ", v)

    if "tom" in tel:
        print("We have Tom's phone number:", tel["tom"])

    if "jeff" not in tel:
        print("We don't have Jeff's phone number.")

    tel.clear()
    print("\nTelephone dictionary was cleared:", tel)


def tuple_test():
    print(f"{ran[0]} lives in {ran[2]} and his phone number is {ran[1]}.")


if __name__ == '__main__':

    dictionary_test()
    # tuple_test()
