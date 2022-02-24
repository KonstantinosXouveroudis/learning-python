import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

if __name__ == '__main__':
    df = pd.read_csv("data\\HR_comma_sep.csv")

    # Arranging for all the columns to be displayed in Pycharm.
    pd.set_option('display.width', 300)
    pd.set_option('display.max_columns', 10)

    print(df.head())

    mean_values = df.groupby("left").mean()
    print("\nMean values for employees who remained (0) and left (1):\n", mean_values)

    ct_sal = pd.crosstab(df['salary'], df['left'])
    # print("\n\n", ct_sal)
    ct_sal.plot(kind='bar', rot=0)
    plt.savefig("plots\\retention_salary_comparison.jpg")
    plt.clf()

    ct_dep = pd.crosstab(df['Department'], df['left'])
    # print("\n\n", ct_dep)
    ct_dep.plot(kind='bar', figsize=(10, 10))
    plt.savefig("plots\\retention_department_comparison.jpg")

    # --- Building and training our model ---
    lr = LogisticRegression(solver='lbfgs', max_iter=50000)

    """
    NOTE TO SELF: Accuracy was always 1.0, no matter the parameters.
    It turned out the problem was that I was initiating inputs via df.drop() like this: 
    df.drop(['last_evaluation', 'number_project', 'time_spend_company',
                      'Work_accident', 'Department'], axis='columns') 
    
    instead of just calling the columns I wanted like below. 
    """
    inputs = df[['satisfaction_level', 'average_montly_hours', 'promotion_last_5years', 'salary']]
    target = df['left']

    salary_dummies = pd.get_dummies(inputs['salary'], prefix='salary')
    train_df = pd.concat([inputs.drop(['salary'], axis='columns'), salary_dummies],
                         axis='columns')
    train_df.drop(['salary_medium'], axis='columns', inplace=True)
    print("\n\n\n", train_df.head())

    x_train, x_test, y_train, y_test = train_test_split(train_df, target, train_size=0.7)
    lr.fit(x_train, y_train)
    accuracy = lr.score(x_test, y_test)
    print("\nModel Accuracy: ", accuracy)

    """
    label_encoder = LabelEncoder()
    inputs = df.drop(['last_evaluation', 'number_project', 'time_spend_company',
                      'Work_accident', 'Department'], axis='columns')
    inputs['salary'] = label_encoder.fit_transform(inputs['salary'])
    target = df['left']

    lr = LogisticRegression(solver='lbfgs', max_iter=5000)

    x_train, x_test, y_train, y_test = train_test_split(inputs, target, test_size=0.3)
    lr.fit(x_train, y_train)
    accuracy = lr.score(x_test, y_test)
    print("\nModel Accuracy: ", accuracy)
    """
