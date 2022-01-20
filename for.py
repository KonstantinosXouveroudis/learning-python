def basics(exp):
    total = 0
    for item in exp:
        total = total + item
    print(f"Total: {total}")


def range_test():
    for i in range(1, 11):  # 1-10 (removing 1 will make the function start from 0)
        print(i)


def monthly_expenses(exp):
    for i in range(len(exp)):
        print(f"Month {i + 1} expenses: {exp[i]}")


def key_search(key_location):
    locations = ["garage", "living room", "table", "chair", "closet", "bedroom"]
    for i in locations:
        if i == key_location:
            print(f"I found the key at: {i}.")
            break


def continue_test():
    for i in range(1, 6):
        if i % 2 == 0:
            continue  # If the number is even, continue takes us back to the for loop a couple lines above.
        print(i * i)

    print("'continue' made it so that any time the if statement is satisfied, the rest of the for loop won't execute "
          "for that iteration.")


def while_test():
    i = 1
    while i <= 5:
        print(i)
        i = i + 1


if __name__ == '__main__':
    # expenses = [2340, 2500, 2100, 3100, 2980]
    # basics(expenses)
    # monthly_expenses(expenses)

    key_search("table")

    continue_test()
    while_test()
    
