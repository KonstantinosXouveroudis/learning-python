import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from scipy.stats import norm
# %matplotlib inline
matplotlib.rcParams['figure.figsize'] = (10, 6)


if __name__ == '__main__':
    df = pd.read_csv('data\\weight-height.csv')
    print(df.sample(5))

    plt.hist(df['Height'], bins=20, rwidth=0.8, density=True)
    plt.xlabel('Height (inches)')
    plt.ylabel('Count')

    # Creating the plot's bell curve (histogram's density must be set to True).
    rng = np.arange(df['Height'].min(), df['Height'].max(), 0.1)
    plt.plot(rng, norm.pdf(rng, df['Height'].mean(), df['Height'].std()))

    # plt.show()

    # Using 3 standard deviations to find the outliers
    # In general, the bigger the dataset the more stds we should use.
    upper_limit = df['Height'].mean() + 3 * df['Height'].std()
    lower_limit = df['Height'].mean() - 3 * df['Height'].std()

    outliers = df[(df['Height'] > upper_limit) | (df['Height'] < lower_limit)]
    print("\nOutliers:\n", outliers)

    print("\nShape with outliers: ", df.shape)
    df = df[(df['Height'] < upper_limit) & (df['Height'] > lower_limit)]
    print("Shape without outliers: ", df.shape)

