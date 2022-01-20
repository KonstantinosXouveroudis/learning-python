def calculate_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total


def sum_of(a, b=0):  # If you don't pass an argument for b, it will be 0 by default.
    total = a + b
    return total


if __name__ == '__main__':
    """
    tom_exp_list = [2000, 3400, 3500]
    joe_exp_list = [200, 500, 700]

    tom_total = calculate_total(tom_exp_list)
    joe_total = calculate_total(joe_exp_list)

    print("Tom's total: ", tom_total)
    print("Joe's total: ", joe_total)
    """

    n = sum_of(4, 5)
    print("Total: ", n)

