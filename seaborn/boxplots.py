import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    penguins = sb.load_dataset('penguins')
    print(penguins.head())

    print("Penguins dataset stats:\n", penguins.describe())

    sb.boxplot(x=penguins.island, y=penguins.bill_length_mm)
    plt.savefig("plots\\boxplots\\penguins.jpg")
    plt.clf()

    sb.boxplot(y=penguins.island, x=penguins.bill_length_mm)
    plt.savefig("plots\\boxplots\\penguins_horizontal.jpg")
    plt.clf()

    sb.boxplot(x=penguins.island, y=penguins.bill_length_mm, hue=penguins.sex)
    plt.savefig("plots\\boxplots\\penguins_hue.jpg")
    plt.clf()

    sb.boxplot(x=penguins.island, y=penguins.bill_length_mm, hue=penguins.sex, color='g',
               order=['Biscue', 'Torgersen', 'Dream'])
    plt.savefig("plots\\boxplots\\penguins_order.jpg")
    plt.clf()

    sb.boxplot(y=penguins.island, x=penguins.bill_length_mm, hue=penguins.sex,
               width=0.7, whis=0.5)
    plt.savefig("plots\\boxplots\\penguins_width_whiskers.jpg")
    plt.clf()

    sb.boxplot(y=penguins.island, x=penguins.bill_length_mm, hue=penguins.sex, showcaps=False)
    plt.savefig("plots\\boxplots\\penguins_no_whiskers.jpg")
    plt.clf()
