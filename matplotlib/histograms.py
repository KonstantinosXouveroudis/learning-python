import matplotlib.pyplot as plt


def blood_sugar_basic():
    blood_sugar = [112, 84, 90, 150, 149, 88, 93, 115, 135, 80, 77, 85, 129]

    plt.hist(blood_sugar)
    # plt.show()

    plt.clf()
    plt.hist(blood_sugar, bins=3,  # Have 3 bins (default: 10)
             rwidth=0.95)  # Slightly decrease the width of the bars, so they don't look joined.
    # plt.show()

    """
    Diabetes blood sugar levels:
    80-100: Normal | 100-125: Pre-diabetic | > 125: Diabetic
    """
    plt.clf()
    plt.xlabel("Blood Sugar Level")
    plt.ylabel("Occurrences")
    plt.hist(blood_sugar, bins=[80, 100, 125, 180],  # Specify our bins by hand. 180 is a max value.
             rwidth=0.95)
    plt.show()


def blood_sugar_by_gender():
    blood_sugar_m = [112, 84, 90, 150, 149, 88, 93, 115, 135, 80, 77, 85, 129]
    blood_sugar_f = [66, 98, 89, 120, 134, 150, 54, 69, 89, 79, 120, 112, 100]

    plt.xlabel("Blood Sugar Level")
    plt.ylabel("Occurrences")
    plt.hist([blood_sugar_m, blood_sugar_f], color=['#a48158', '#90d36b'], label=['Males', 'Females'],
             bins=[80, 100, 125, 180],  # Specify our bins by hand. 180 is a max value.
             # orientation='horizontal',  # In case we want to edit the orientation.
             rwidth=0.9)  # Slightly decrease the width of the bars, so they don't look joined.
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # blood_sugar_basic()
    blood_sugar_by_gender()
