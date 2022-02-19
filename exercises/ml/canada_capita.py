import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

if __name__ == '__main__':
    df = pd.read_csv("data\\canada_per_capita_income.csv")
    print(df)

    plt.plot(df['year'], df['per capita income (US$)'])
    plt.xticks([1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020])
    plt.xlabel('Year')
    plt.ylabel('Per Capita Income (US$)')
    # plt.show()

    reg = linear_model.LinearRegression()

    year_reshape = df['year'].values.reshape(-1, 1)
    reg.fit(year_reshape, df['per capita income (US$)'])

    prediction = reg.predict([[2020]])
    print("\nCapita in the year 2020: ", prediction)

