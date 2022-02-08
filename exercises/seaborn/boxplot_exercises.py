import seaborn as sb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Load the mpg dataset and print its stats using the describe() function
    mpg = sb.load_dataset('mpg')
    print(mpg)
    print("\n", mpg.describe())

    # 1) Boxplot for mpg column.
    sb.boxplot(y=mpg.mpg)
    plt.savefig("plots\\boxplots\\mpg.jpg")
    plt.clf()

    # 2) Boxplot with origin column for x-axis and mpg column for y-axis.
    sb.boxplot(x=mpg.origin, y=mpg.mpg)
    plt.savefig("plots\\boxplots\\mpg_origin.jpg")
    plt.clf()

    # 3) Boxplot above, but with the hue set to the cylinders column.
    sb.boxplot(x=mpg.origin, y=mpg.mpg, hue=mpg.cylinders)
    plt.savefig("plots\\boxplots\\mpg_cylinders.jpg")
    plt.clf()

    # 4) Same plot as 2), custom order.
    sb.boxplot(x=mpg.origin, y=mpg.mpg, order=['japan', 'europe', 'usa'])
    plt.savefig("plots\\boxplots\\mpg_custom_order.jpg")
    plt.clf()

    # 4) Same plot as 2), custom order.
    sb.boxplot(x=mpg.origin, y=mpg.mpg, order=['japan', 'europe', 'usa'], color='red', width=0.3)
    plt.savefig("plots\\boxplots\\mpg_red_lowwidth.jpg")
    plt.clf()


