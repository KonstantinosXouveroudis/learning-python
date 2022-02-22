import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    df = pd.read_csv("data\\carprices.csv")
    print(df)

    plt.scatter(df['Mileage'], df['Sell Price($)'])
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.savefig("plots\\tr_te_car_mileage.jpg")
    plt.clf()

    plt.scatter(df['Age(yrs)'], df['Sell Price($)'])
    plt.xlabel("Age")
    plt.ylabel("Price")
    plt.savefig("plots\\tr_te_car_age.jpg")

    x = df[['Mileage', 'Age(yrs)']]
    y = df['Sell Price($)']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)  # Training set 80%, Testing set 20%

    model = LinearRegression()
    model.fit(x_train, y_train)

    prediction = model.predict(x_test)
    print("\nPrediction:\n", prediction, "\n\nActua data:\n", y_test)

    print("\nAccuracy: ", model.score(x_test, y_test))

