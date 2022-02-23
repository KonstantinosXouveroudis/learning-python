import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import array


def basic_training():
    dfl = pd.read_csv('data\\homeprices.csv')
    print(dfl)

    plt.scatter(dfl['area'], dfl['price'], marker='+', color='red')
    plt.xlabel('Area (sqr ft)')
    plt.ylabel('Price (US$)')
    plt.savefig("plots\\homeprices.jpg")

    # Beginning linear regression
    regl = linear_model.LinearRegression()

    """
    Training the regression model using the available data points
    The first argument needs to be a 2d array so you can supply your dataframe. We use reshape to that end.
    """
    df_area_r = dfl['area'].values.reshape(-1, 1)
    regl.fit(df_area_r, dfl['price'])

    """
    We can only use predict on data that is of the same dimensionality as the training data (X) was. 
    So in our case, the parameter for predict needs to be a 2D array.
    """
    prediction = regl.predict([[3300]])
    print("\nPrice for an area of 3300: ", prediction)

    coefficient = regl.coef_
    intercept = regl.intercept_
    print("Coefficient: ", coefficient)
    print("Intercept: ", intercept)

    y = coefficient[0] * 3300 + intercept
    print("Same price when calculated by hand: ", y)

    # Creating new plot with the visual representation of the linear regression we executed.
    plt.clf()
    plt.xlabel('Area', fontsize=20)
    plt.ylabel('Price', fontsize=20)
    plt.scatter(dfl['area'], dfl['price'], color='red', marker='+')
    plt.plot(dfl['area'], regl.predict(dfl[['area']].values), color='blue')
    plt.savefig('plots\\homeprices_prediction.jpg', bbox_inches="tight")

    # Returning the regression model, so it can be used outside the function.
    return regl


if __name__ == '__main__':
    reg = basic_training()
    df = pd.read_csv('data\\areas.csv')

    price_prediction = reg.predict(df.values)

    # Creating new column in the dataframe to assign the predicted prices to.
    df['prices'] = price_prediction
    df.to_csv("data\\areas_predicted_prices.csv", index=False)
