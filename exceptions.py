def generic_exception(x, y):
    try:
        z = int(x) / int(y)
    except Exception as e:
        print("Exception occurred: ", e)
        print("Exception type is: ", type(e).__name__)  # can be used to figure out what exception is occurring
        z = None

    print("Division is: ", z)


def specific_exception(x, y):
    try:
        z = int(x) / int(y)
    except ZeroDivisionError as e:
        print("You tried to divide by 0, Zero Division Exception occurred.")
        z = None

    print("Division is: ", z)


if __name__ == '__main__':
    input1 = input("Enter a number: ")
    input2 = input("Enter a 2nd number: ")

    generic_exception(input1, input2)
    specific_exception(input1, input2)

