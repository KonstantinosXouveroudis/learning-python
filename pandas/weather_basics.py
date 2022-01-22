import pandas as pd

if __name__ == '__main__':
    # df = pd.read_csv("dataframes\\weather_data.csv")
    # Alternatively, we use a dictionary:
    weather_data = {
        'Day': ['1/1/2022', '1/2/2022', '1/3/2022', '1/4/2022', '1/5/2022', '1/6/2022'],
        'Temperature': [32, 35, 28, 24, 32, 31],
        'Wind Speed': [6, 7, 2, 7, 4, 2],
        'Event': ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny']
    }

    df = pd.DataFrame(weather_data)
    print("Shape of the dataframe:", df.shape)
    print("\nFirst 3 rows:\n", df.head(3))
    print("\nLast 2 rows:\n", df.tail(2))
    print("\nRows 1-3:\n", df[1:4])

    print("\nAll columns:", df.columns)
    print("\n\t Day")
    print(df['Day'])  # or df.Day

    print("\n", df[['Event', 'Temperature']])  # print only the selected columns

    print("\nData statistics:\n", df.describe())

    print("\nTemperatures above 31 degrees:")
    print(df[df['Temperature'] >= 32])

    print("\nDay with the maximum temperature:")
    print(df[['Day', 'Temperature']][df['Temperature'] == df['Temperature'].max()])

    # print("\nSwitching the index:\n", df.set_index('Day'))
    # Or:
    df.set_index('Day', inplace=True)  # edits the original dataframe instead of returning a copy.
    print("\nSwitching the index:\n", df)
    print("\n", df.loc['1/5/2022'])

    df.reset_index(inplace=True)
    print("\nAfter resetting index:\n", df)
