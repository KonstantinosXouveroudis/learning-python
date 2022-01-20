def process_file():
    try:
        f = open("C://Users//Kostas//PycharmProjects//learningBasics310//readwrite//file.txt")
        x = 1/0
    except FileNotFoundError as e:
        print(f"An exception occurred: {e}")
    finally:
        # We're not covering the zero division exception, therefore 'finally' ensures the file will close despite that.
        # if f.close() was outside of finally, it wouldn't execute before the program terminates.
        print("Closing the file.")
        f.close()


if __name__ == '__main__':
    process_file()

