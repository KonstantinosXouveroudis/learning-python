import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer


def one_hot_encoder(dfl, modell):
    """
       We want to be able to predict prices per town accordingly. For example, 2 towns could both have a house with an
       area of 5000, but different prices for it. We want to be able to predict their prices accordingly.

       To that end, we use the One Hot Encoding method. We need to create dummy variables.
       Dummy variables: variables containing values such as 1 or 0 representing the presence
       or absence of the categorical value.
    """

    town_dummies = pd.get_dummies(dfl["town"])
    merged_df = pd.concat([dfl, town_dummies], axis='columns')
    print("\n", merged_df)

    # In order to avoid the infamous Dummy Variable Trap, we need to drop the town column and/or 1 of the dummies.
    final_df = merged_df.drop(['town', 'robinsville'], axis='columns')
    print("\n", final_df)

    # Building and training our model using the customized dataset we just created.
    x = final_df.drop(['price'], axis='columns')
    y = final_df['price']

    modell.fit(x.values, y)

    # Predict price for a house with an area of 3400 in West Windsor.
    prediction = modell.predict([[3400, 0, 1]])
    print("\n", prediction)

    # Predict price for a house with an area of 2800 in Robinsville.
    prediction = modell.predict([[2800, 0, 0]])
    print(prediction)

    # Predict all the prices in x and compare them to y (supplied actual prices)
    print("\nModel accuracy: ", modell.score(x.values, y))


def sklearn_ohe(dfl, modell):
    # Sklearn's One Hot Encoder
    # We need to do Label Encoding on the town column
    le = LabelEncoder()

    # Replacing the town labels with numbers
    dfle = dfl
    dfle['town'] = le.fit_transform(dfle['town'])
    print("\n", dfle)

    x = dfle[['town', 'area']].values  # values returns the columns as a 2d array
    y = dfle['price']

    ohe = OneHotEncoder()
    # The [0] arg (x's town) is our categorical feature, the list of columns we want to transform in this step.
    ct = ColumnTransformer([('town1', ohe, [0])], remainder="passthrough")

    x = ct.fit_transform(x)

    # Our new x replaced the town column with 3 dummy columns for the 3 towns included previously.
    print("\n", x)

    # Removing one column to avoid the One Hot Encoder Trap.
    x = x[:, 1:]  # Take all rows. Take all columns from index 1 onwards.
    print("\n", x)

    modell.fit(x, y)

    # Predict price for a house with an area of 2800 in Robinsville.
    prediction = modell.predict([[1, 0, 2800]])
    print("\n", prediction)

    # Predict price for a house with an area of 3400 in West Windsor.
    prediction = modell.predict([[0, 1, 3400]])
    print(prediction)


if __name__ == '__main__':
    df = pd.read_csv("data\\homeprices_towns.csv")
    print(df)

    model = LinearRegression()
    # one_hot_encoder(df, model)
    sklearn_ohe(df, model)

