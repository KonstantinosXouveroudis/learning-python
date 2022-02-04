import seaborn as sb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    penguins = sb.load_dataset('penguins')
    print(penguins.head())

    sb.displot(penguins.flipper_length_mm)  # distplot (NOT displot) will be removed in future versions
    plt.savefig("plots\\distplots\\penguins.jpg")

    sb.displot(penguins.flipper_length_mm, kde=True)
    plt.savefig("plots\\distplots\\penguins_kde.jpg")

    sb.displot(penguins.flipper_length_mm, rug=True)
    plt.savefig("plots\\distplots\\penguins_rug.jpg")

    sb.displot(penguins.flipper_length_mm, rug=True,
               rug_kws={'color': 'red', 'height': 0.30})
    plt.savefig("plots\\distplots\\penguins_rug2.jpg")

    sb.displot(penguins.flipper_length_mm, bins=20)
    plt.savefig("plots\\distplots\\penguins_20bins.jpg")

    sb.displot(penguins.flipper_length_mm, bins=20)
    plt.savefig("plots\\distplots\\penguins_20bins.jpg")

    sb.displot(penguins.flipper_length_mm, bins=[160, 170, 180, 190, 200, 240])
    plt.savefig("plots\\distplots\\penguins_custom_bins.jpg")
