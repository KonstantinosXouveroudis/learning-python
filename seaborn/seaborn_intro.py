import seaborn as sb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def bar_plots():
    # Seaborn has a list of pre-processed datasets that can be used.
    print(sb.get_dataset_names())

    # tips is one of said datasets.
    tips = sb.load_dataset('tips')
    print(tips.head())  # First 5 lines

    sb.barplot(x='day', y='total_bill', data=tips)
    # plt.show()
    plt.savefig("plots\\plot1v.jpg")
    plt.clf()

    sb.barplot(x='total_bill', y='day', data=tips)  # Same plot, but horizontal.
    plt.savefig("plots\\plot1h.jpg")
    plt.clf()

    sb.barplot(x='day', y='total_bill', data=tips,
               hue='sex',  # hue gives us a legend and splits the data based a column
               order=['Sun', 'Fri', 'Thur', 'Sat'],
               ci=60,  # Size of confidence intervals (black lines))
               capsize=0.3)  # Adds ca to ci
    plt.savefig("plots\\plot1_custom_order.jpg")
    plt.clf()

    sb.barplot(x='day', y='total_bill', data=tips,
               hue='sex',
               estimator=np.median)
    plt.savefig("plots\\plot1_custom_estimator.jpg")
    plt.clf()


def palette_testing():
    """
    color_palette alone shows us a string of numbers, so we use palplot() to see the colors.
    Seaborn has six variations of its default color palette: deep, muted, pastel, bright, dark, and colorblind.
    Other palettes include light, winter_r, spring.
    """
    sb.palplot(sb.color_palette('deep', 10))  # Show us 10 colors of the deep palette.
    # plt.show()
    plt.savefig("plots\\palette_deep.jpg")
    plt.clf()

    sb.palplot(sb.color_palette('spring', 5))
    plt.savefig("plots\\palette_spring.jpg")
    plt.clf()

    # Create a custom palette
    custom = ['red', 'blue', 'green']
    sb.set_palette(custom)
    sb.palplot(sb.color_palette())
    # plt.show()
    plt.savefig("plots\\palette_custom.jpg")
    plt.clf()


if __name__ == '__main__':
    # bar_plots()
    # palette_testing()

    # Save fig alternative:
    sb_plot = sb.barplot(x='day', y='total_bill', data=sb.load_dataset('tips'))
    fig = sb_plot.get_figure()
    fig.savefig("plots\\plot1_seaborn_method.jpg")
