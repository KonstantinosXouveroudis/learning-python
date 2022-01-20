# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


"""
List: []
Dictionary: {}
Tuple: ()
"""
from modules import calculations as calc

"""
If the module is in a completely different directory:
import sys
sys.path.append("C:\...")
import module
"""


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def number_tests():
    rent = 120
    groceries = 30.6
    total = rent + groceries
    print(f"Your rent is {rent}.")
    print("Total expenses for the month:", total)


def string_tests():
    food = "sandwich"
    print(f"I would like a {food}.")
    print(f"I hate {food[0:4]}.")  # food[:4] also works
    print(f"{food[4:]} {food} would you like?")  # food[4:8] also works

    price = 2
    cashier_message = "Your order costs " + str(price) + "$."
    print(cashier_message)


def list_tests(my_list):
    print(my_list[0])
    print(f"Important: {my_list[0:2]}")
    print(f"Secondary: {my_list[2:]}")

    my_list.append("butter")
    print(f"Added: {my_list[-1]}")  # -1 shows last item of list

    my_list.insert(1, "eggs")  # insert at index
    print(f"Added: {my_list[1]}")
    print(f"Total number of items: {len(my_list)}")

    print("Is bread on the list?", "bread" in my_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # number_tests()
    # string_tests()

    shopping_list = ["bread", "pasta", "fruits", "veggies"]
    list_tests(shopping_list)

    print()  # \n also works
    print_hi('PyCharm')

    print(calc.calculate_square_area(5))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
