def write_file(file):
    f = open(file, "w")  # w+ and r+ open the file for both reading and writng.
    f.write("Text sample from Python")
    f.close()


def append_file(file):
    f = open(file, "a")
    f.write("\nAdditional text from a different function")
    f.close()


def read_file(file):
    f = open(file, "r")
    # print(f.read())  # reads the entire file
    for line in f:  # reads it line by line
        print(line)
    f.close()


def count_words(file):
    f = open(file, "r")
    # New file with the next AND the word count of the original.
    fwc = open("C://Users//Kostas//PycharmProjects//learningBasics310//readwrite//file_wc.txt", "w")

    for line in f:
        tokens = line.split(" ")
        fwc.write("Word Count: " + str(len(tokens)) + " | " + line)
    f.close()
    fwc.close()


def with_statement_test(file):
    with open(file, "r") as f:  # the with statement automatically closes a file once it's done.
        print(f.read())

    if f.closed:  # closed function returns true/false depending on if the file is closed.
        print("\nThe file is closed.")
    else:
        print("\nThe file is still open!!!")


if __name__ == '__main__':
    txt_file = "C://Users//Kostas//PycharmProjects//learningBasics310//readwrite//file.txt"
    txt_file2 = "C://Users//Kostas//PycharmProjects//learningBasics310//readwrite//file2.txt"

    # write_file(txt_file)
    # append_file(txt_file)
    # read_file(txt_file2)
    count_words(txt_file)
    with_statement_test(txt_file2)
