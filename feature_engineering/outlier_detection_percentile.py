import pandas as pd

def heights(dfl):
    # What number is above 95%, 75%, 50%, 5% of the dataset.
    quan95 = dfl['height'].quantile(0.95)  # All numbers above this can be considered outliers.
    quan75 = dfl['height'].quantile(0.75)
    quan50 = dfl['height'].quantile(0.50)
    quan5 = dfl['height'].quantile(0.05)

    print(quan5, "\n", quan50, "\n", quan75, "\n", quan95)

    outliers_min = dfl[dfl['height'] < quan5]
    print("\nThe outliers from the minimum threshold are:\n", outliers_min)

    outliers_max = dfl[dfl['height'] > quan95]
    print("\nThe outliers from the maximum threshold are:\n", outliers_max)

    # Removing outliers
    dfl = dfl[(dfl['height'] > quan5) & (dfl['height'] < quan95)]
    print("\n", dfl)


def houses(dfl):
    dfl.describe()
    min_threshold, max_threshold = dfl['price_per_sqft'].quantile([0.001, 0.999])
    print(min_threshold, max_threshold)

    outliers_min = dfl[dfl['price_per_sqft'] < min_threshold]
    outliers_max = dfl[dfl['price_per_sqft'] > max_threshold]

    print("\nExamples of outliers from the minimum threshold\n", outliers_min.head())
    print("\nExamples of outliers from the maximum threshold\n", outliers_max.head())

    print("\nShape with outliers: ", dfl.shape)
    dfl = dfl[(dfl['price_per_sqft'] > min_threshold) & (dfl['price_per_sqft'] < max_threshold)]
    print("Shape without outliers: ", dfl.shape)


if __name__ == '__main__':
    df = pd.read_csv("data\\heights.csv")
    # heights(df)

    df = pd.read_csv("data\\bhp.csv")
    houses(df)


