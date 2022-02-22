import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt


if __name__ == '__main__':
    # Using the carprices dataset, predict car prices based on car model, age, mileage.

    df = pd.read_csv("data\\carprices.csv")
    print(df.head())

    model_dummies = pd.get_dummies(df['Car Model'])
    df2 = pd.concat([df['Mileage'], df['Sell Price($)'], df['Age(yrs)'], model_dummies], axis='columns')
    df2.drop(['Mercedez Benz C class'], axis='columns', inplace=True)
    print("\n", df2)

    x = df2.drop(['Sell Price($)'], axis='columns')
    y = df2['Sell Price($)']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)  # Training set 80%, Testing set 20%
    model = LinearRegression()
    model.fit(x_train.values, y_train)

    print("\nAccuracy: ", model.score(x_test.values, y_test))
    prediction = model.predict([[45000, 4, 1, 0]])
    print("\nPredicted price for a 4 year old Audi A5 with a mileage of 45000: ", prediction)
