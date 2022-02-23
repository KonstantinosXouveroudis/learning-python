import pandas as pd
import numpy as np
from sklearn import linear_model
import math

if __name__ == '__main__':
    df = pd.read_csv("data\\homeprices2.csv")
    print(df)

    median_bedrooms = math.floor(df['bedrooms'].median())  # We want an integer, so we use the floor method.
    print("\n", median_bedrooms)

    # Replace NaN values on the bedrooms column with the median.
    df['bedrooms'].fillna(median_bedrooms, inplace=True)
    print("\n", df)

    reg = linear_model.LinearRegression()
    # The fit method is used to train your model using your training set (1st parameter). Price is the target variable.
    reg.fit(df[['area', 'bedrooms', 'age']].values, df['price'])
    print("\nCoefficients for area, bedrooms and age in that order: ", reg.coef_)
    print("Intercept: ", reg.intercept_)

    prediction = reg.predict([[3000, 3, 40]])
    print("\nA 40 year old building, with 3 bedrooms and an area of 3000. \nPredicted price: ", prediction)

    calculation = (reg.coef_[0] * 3000) + (reg.coef_[1] * 3) + (reg.coef_[2] * 40) + reg.intercept_
    print("Same prediction calculated by hand: ", calculation)
