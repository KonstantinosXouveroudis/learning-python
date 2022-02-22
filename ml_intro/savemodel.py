import numpy as np
import pandas as pd
import pickle
import joblib
from sklearn import linear_model

if __name__ == '__main__':
    df = pd.read_csv("data\\homeprices.csv")
    print(df.head())

    model = linear_model.LinearRegression()
    model.fit(df[['area']].values, df['price'])

    prediction = model.predict([[5000]])
    print("\nA house with an area of 5000 should cost: ", prediction)

    # 1) Saving a model with pickle
    # Saving the trained model in a binary file called model_pickle, then reading the same model from the file.
    with open("models\\model_pickle", "wb") as f:
        pickle.dump(model, f)

    with open("models\\model_pickle", "rb") as f:
        mp = pickle.load(f)

    prediction_p = mp.predict([[5000]])
    print("Same prediction from a saved model (using pickle): ", prediction_p)

    # 2) Saving a model with joblib. Preferred when dealing with large numpy arrays.
    # Saving the trained model in a file, then reading that file and using the model from there.
    joblib.dump(model, "models\\model_joblib")
    mj = joblib.load("models\\model_joblib")
    prediction_j = mj.predict([[5000]])
    print("Same prediction from a saved model (using joblib): ", prediction_j)
