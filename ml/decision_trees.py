import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


if __name__ == '__main__':
    df = pd.read_csv("data\\salaries.csv")
    print(df.head())

    inputs = df.drop('salary_more_then_100k', axis='columns')
    target = df['salary_more_then_100k']

    # We need to transform all the text in our dataframes into numbers so we can use them in our ml model.
    # Therefore, we'll use LabelEncoder.

    le_company = LabelEncoder()
    le_job = LabelEncoder()
    le_degree = LabelEncoder()

    # Creating new columns with the encoded values.
    inputs['company_n'] = le_company.fit_transform(inputs['company'])
    inputs['job_n'] = le_job.fit_transform(inputs['job'])
    inputs['degree_n'] = le_degree.fit_transform(inputs['degree'])

    print("\n", inputs)

    inputs_n = inputs.drop(['company', 'job', 'degree'], axis='columns')
    print("\n", inputs_n)

    # Train (70%) / test (30%) split
    x_train, x_test, y_train, y_test = train_test_split(inputs_n, target, test_size=0.3)

    # Creating our decision tree model
    model = tree.DecisionTreeClassifier()
    model.fit(x_train.values, y_train)

    accuracy = model.score(x_test.values, y_test)
    print("\nAccuracy: ", accuracy)

    # Predict the salary of an employee working at Google as a sales executive with a Master's degree
    prediction = model.predict([[2, 2, 1]])
    print("\n0: False, 1: True")
    print("Is that person getting more than 100k?",
          "\nGoogle Sales Executive with a Master's Degree:", prediction)

    prediction = model.predict([[2, 0, 1]])
    print("Google Business Manager with a Bachelor's Degree:", prediction)
