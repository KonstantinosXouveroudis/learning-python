import pandas as pd
import numpy as np
from sklearn import linear_model
import math
from word2number import w2n

"""
hiring.csv is a dataset containing the years of experience for a number of employees, their scores
in a test and their interview, as well as their salary.
Using this dataset, create a model that predicts what salary the company should offer to new candidates based
on their experience and scores. Predict the salary for the following candidates:
- Someone with 2 years of experience, a test score of 9 and an interview score of 6.
- Someone with 12 years of experience, a test score of 10 and an interview score of 10.
"""

if __name__ == '__main__':
    df = pd.read_csv('data\\hiring.csv')
    print(df)

    # Replace the NaN values in the experience column with 'zero'. Then turn all word numbers into actual numbers.
    df['experience'].fillna('zero', inplace=True)
    df['experience'] = df['experience'].apply(w2n.word_to_num)

    # Calculate the median for the test scores and replace NaN values in that column with it.
    test_median = math.floor(df['test_score(out of 10)'].median())
    df['test_score(out of 10)'].fillna(test_median, inplace=True)

    print('\n', df)

    reg = linear_model.LinearRegression()
    reg.fit(df[['experience', 'test_score(out of 10)', 'interview_score(out of 10)']].values, df['salary($)'])

    print('\nCoefficients for experience, test score and interview score in that order: ', reg.coef_)
    print('Intercept: ', reg.intercept_)

    # First candidate.
    prediction = reg.predict([[2, 9, 6]])
    print("\nPredicted salary for a candidate with 2 years of experience, a test score of 9 and "
          "an interview score of 6: ", prediction)
    calculation = (reg.coef_[0] * 2) + (reg.coef_[1] * 9) + (reg.coef_[2] * 6) + reg.intercept_
    print("Same prediction, but calculated by hand: ", calculation)

    # Second candidate.
    prediction = reg.predict([[12, 10, 10]])
    print("\nPredicted salary for a candidate with 12 years of experience and a score of 10 "
          "in both the test and the interview: ", prediction)
    calculation = (reg.coef_[0] * 12) + (reg.coef_[1] * 10) + (reg.coef_[2] * 10) + reg.intercept_
    print("Same prediction, but calculated by hand: ", calculation)

