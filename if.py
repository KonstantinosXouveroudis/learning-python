def cuisine():
    indian = ["samosa", "daal", "naan"]
    chinese = ["egg roll", "pot sticker", "fried rice"]
    italian = ["pizza", "pasta", "risotto"]

    dish = input("Enter a dish name: ")
    message = "This dish is "
    if dish in indian:
        print(message + "indian.")
    elif dish in chinese:
        print(message + "chinese.")
    elif dish in italian:
        print(message + "italian.")
    else:
        print(f"Based on the little knowledge I have, I don't know what cuisine {dish} belongs to.")


def basics():
    num = input("Enter a number: ")
    num = int(num)  # Because input returns a string.
    limit = 10

    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

    if num % 2 == 0 and num < limit:
        print(f"The number is even and does not extend beyond the accepted limit ({limit}).")

    if not num % 2 != 0:
        print(f"Yep, still even.")


if __name__ == '__main__':
    cuisine()

