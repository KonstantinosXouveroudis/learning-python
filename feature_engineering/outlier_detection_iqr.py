import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv("data\\heights2.csv")
    print(df.describe())

    quan25 = df['height'].quantile(0.25)
    quan75 = df['height'].quantile(0.75)
    iqr = quan75 - quan25

    lower_limit = quan25 - 1.5 * iqr
    upper_limit = quan75 + 1.5 * iqr

    outliers = df[(df['height'] < lower_limit) | (df['height'] > upper_limit)]
    print("\nOutliers:\n", outliers)

    print("\nShape with outliers: ", df.shape)
    df = df[(df['height'] > lower_limit) & (df['height'] < upper_limit)]
    print("Shape without outliers: ", df.shape)
