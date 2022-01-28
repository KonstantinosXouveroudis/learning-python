import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [50, 51, 52, 48, 47, 49, 46]
    y2 = [43, 42, 40, 44, 33, 35, 37]
    y3 = [45, 48, 48, 46, 40, 42, 41]

    plt.plot(x, y, 'g*--')  # green, * marks, dash. Order doesn't matter.
    # plt.show()
    plt.cla()

    # It's possible to be more specific if we want:
    plt.plot(x, y, color='purple', marker='o', linestyle='dotted',
             alpha=0.4)  # alpha is transparency.
    # plt.show()

    # We can add multiple axes to one plot.
    plt.cla()
    plt.xlabel("Days")
    plt.ylabel("Temperature")
    plt.title("Weather Plot")
    plt.plot(x, y, linewidth=3, label='Max')  # Labels are for the legend.
    plt.plot(x, y2, 'r', label='Mim')
    plt.plot(x, y3, 'g', label='Avg')
    plt.legend()  # We can use the loc parameter to set the location, but by default it picks the best spot.
    plt.grid()  # Add a grid to our plot figure, so we can better distinguish the values.
    plt.show()

