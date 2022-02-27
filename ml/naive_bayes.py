import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

if __name__ == '__main__':

    # Adjusting the length so we can see the entire dataframe in Pycharm.
    width = 300
    pd.set_option('display.width', width)
    pd.set_option('display.max_columns', 12)

    df = pd.read_csv("data\\titanic.csv")
    print(df.head())

    df.drop(['PassengerId', 'Name', 'SibSp', 'Parch', 'Ticket', 'Cabin', 'Embarked'], axis='columns', inplace=True)
    print("\n", df.head())

    inputs = df.drop('Survived', axis='columns')
    target = df['Survived']

    # Adjusting the dataframe to have numerical values only.
    gender_dummies = pd.get_dummies(inputs['Sex'])
    inputs = pd.concat([inputs, gender_dummies], axis='columns')
    inputs.drop(['Sex', 'male'], axis='columns', inplace=True)  # Deleting the male column too to avoid errors.

    print("\n", inputs.columns[inputs.isna().any()])

    # Detecting some non-numerical values. Print first 10 columns of the Age column for observation.
    print("\n", inputs['Age'][:10])

    # NaN values, replace them with the age mean.
    inputs['Age'] = inputs['Age'].fillna(inputs['Age'].mean())

    # Building and training our model.
    x_train, x_test, y_train, y_test = train_test_split(inputs, target, test_size=0.3)
    model = GaussianNB()
    model.fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    print("\nGaussianNB Accuracy: ", accuracy)

    # Prediction with x_test's first 10 samples.
    prediction = model.predict(x_test[:10])

    print("\nPredicted: ", prediction,
          "\nActual: ", y_test[:10])

    print("\nDidn't Survive | Survived\n", model.predict_proba(x_test[:10]))
