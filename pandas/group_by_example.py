import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv("dataframes\\weather_by_cities.csv")
    print(df)

    group = df.groupby('city')
    for city, city_df in group:
        print("\nCity: ", city)
        print(city_df)

    print("\nPrinting just Paris:\n", group.get_group("paris"))

    print("\nMax value for each column of each group:\n", group.max())

    print("\nMedian value for each column of each group:\n", group.median())

    print("\nStatistics for each group:\n", group.describe())

    print("\n\n------------------\n\n")

    # plt.interactive(False)
    for city, city_df in group:
        city_df.plot()
        plt.savefig(f"plots\\plot-{city}.jpg")
    # group.plot()
    # plt.savefig('test.jpg')
