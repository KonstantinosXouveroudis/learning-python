import pandas as pd
import numpy as np


def replace_list():
    # Replacing a list with a different list.
    dfl = pd.DataFrame({
        "Student": ["Rob", "Maya", "Parthiv", "Tom", "Julian", "Erica"],
        "Score": ["Exceptional", "Average", "Good", "Poor", "Average", "Exceptional"]

    })

    dfl.replace(["Poor", "Average", "Good", "Exceptional"], [1, 2, 3, 4],
                inplace=True)
    print(dfl)


if __name__ == '__main__':
    df = pd.read_csv("dataframes\\missing_data\\weather_data2.csv")

    """
    Note: The zeros in the event column are strings
    And because of our metrics (F, C, mph), the values in the temperature and windspeed columns are also strings now.
    
    Additionally, by specifying what values we want replaced for each column, we get a more valid result.
    For example, 0 could be a useful value in temperature, but not in event.
    """
    new_df = df.replace({
                        'temperature': -99999,
                        'windspeed': -99999,
                        'event': "0"
                        }, np.NaN)
    print(new_df)

    # Alternatively, we can use a dictionary to specify what we want each value to be replaced with.
    new_df = df.replace({
                        "-99999": np.NaN,
                        "0": "Sunny"
                        })
    print("\n", new_df)

    new_df = new_df.replace({
                        'temperature': '[A-Za-z]',
                        'windspeed': '[A-Za-z]'
                        }, '', regex=True)
    print("\n", new_df)

    print("\n")
    replace_list()
