import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('C:\\Users\\Kostas\\PycharmProjects\\learning-python\\pandas\\dataframes\\nyc_weather.csv')
    # df = datafrane
    print(df)

    print("\nThe maximum temperature is: ", df['Temperature'].max())

    print("\nIt rained during the following days:")
    print(df['EST'][df['Events'] == 'Rain'])

    print("\nThe average wind speed is: ", df['WindSpeedMPH'].mean())

    print("Note: The dataframe contains some null values (NaN), which are affecting the mean. Replacing them with 0.")
    df.fillna(0, inplace=True)
    print("True wind speed average: ", df['WindSpeedMPH'].mean())

    temperatures = df['Temperature'].value_counts().sort_index()
    print("\nList of temperatures shown in the dataframe and number of appearances for each:", temperatures)

    print("\nHighest temperature recorder: ", df['Temperature'].max())
    print(df[df['Temperature'] == df['Temperature'].max()])

    print("\nMinimum temperature recorder: ", df['Temperature'].min())
    print(df[df['Temperature'] == df['Temperature'].min()])

    print("\nWind direction degrees before clip:\n", df['WindDirDegrees'].values)
    clip_wind_degrees = df['WindDirDegrees'].clip(50, 275).values
    print("\nAfter clip (50 - 275):\n", clip_wind_degrees)
