import seaborn as sb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':

    # Load the mpg dataset and store it in a variable called cars.
    cars = sb.load_dataset('mpg')
    print(cars.head())

    # 1) Load a distplot for the displacement column.
    sb.displot(cars.displacement)
    plt.savefig("plots\\distplots\\cars_displacement.jpg")

    # 2) Another distplot with the kde enabled.
    sb.displot(cars.displacement, kde=True)
    plt.savefig("plots\\distplots\\cars_displacement_kde.jpg")

    # 3) Yet another displot with the rug enabled and 20 bins. Give the rug a red color.
    sb.displot(cars.displacement, rug=True, bins=20,
               rug_kws={"color": "red", "height": 0.1})
    plt.savefig("plots\\distplots\\cars_displacement_rug.jpg")

    # 4) Same plot as 1) but with 15 bins.
    sb.displot(cars.displacement, bins=15)
    plt.savefig("plots\\distplots\\cars_displacement_15bins.jpg")

    # plt.show()
    # plt.clf()
