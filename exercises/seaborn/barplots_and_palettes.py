import seaborn as sb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    """
    Load the flights dataset and: 
    1) Draw a bar plot with year on the x axis and passengers on the y axis.
    2) A second bar plot, but with the months on the x axis instead.
    3) Set the palette of the first bar plot to winter_r.
    """

    flights = sb.load_dataset("flights")
    print(flights.head())
    sb.barplot(x='year', y='passengers', data=flights, palette='winter_r')
    sb.set_palette('winter_r')
    plt.savefig("plots\\bar_years.jpg")
    plt.clf()

    sb.barplot(x='month', y='passengers', data=flights)
    plt.savefig("plots\\bar_months.jpg")

    """
    1) Display 5 colors of the spring palette.
    2) Create a list of 4 colors and display them as a palette. 
    """

    sb.palplot(sb.color_palette('spring', 5))
    plt.savefig("plots\\palette_spring.jpg")

    my_colors = ['purple', 'red', 'orange', 'yellow']
    sb.set_palette(my_colors)
    sb.palplot(sb.color_palette())
    plt.savefig("plots\\palette_custom.jpg")

