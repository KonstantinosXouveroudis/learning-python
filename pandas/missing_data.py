import pandas as pd
import scipy


def fillna_examples():
    dfl = df.fillna({  # Replace NaN values. Specific values for each column.
        'temperature': 'Data Unavailable',
        'windspeed': 0,
        'event': 'Data Unavailable'
    })
    print("\n", dfl)

    dfl = df.fillna(method="ffill",  # Replaces NaN with the previous value of the same column.
                       limit=1)  # If there is >1 consecutive NaNs, replace only the 1st.
    # new_df = df.fillna(method="bfill")  # Same as ffill, but instead copies the next available value.
    print("\n", dfl)


def interpolation_examples():
    dfl = df.interpolate()  # Default interpolation. Fills NaNs with the mean of the values they're surrounded by.
    print("\n", dfl)

    dfl = df.interpolate(method="time")  # Time interpolation. Considers the dates in our csv.
    print("\n", dfl)

    dfl = df.interpolate(method="pad", limit=1)  # Replace NaN with previous value, but not in consecutive NaNs.
    print("\n", dfl)

    # df.reset_index(inplace=True)
    dfl = df.interpolate(method="polynomial", order=2)
    print("\n", dfl)

    dfl = df.interpolate(method="polynomial", order=3)
    print("\n", dfl)


def dropna_examples():
    dfl = df.dropna()  # Drop rows with at least one NaN.
    print("\n", dfl)

    dfl = df.dropna(how="all")  # Drop rows where all columns are NaN.
    print("\n", dfl)

    dfl = df.dropna(thresh=2)  # Keep only the rows with at least 2 valid values (not NaN)
    print("\n", dfl)


if __name__ == '__main__':
    df = pd.read_csv("dataframes\\missing_data\\weather_data.csv")
    print("Type of Day column: ", type(df["day"][0]))

    df = pd.read_csv("dataframes\\missing_data\\weather_data.csv",
                     parse_dates=["day"])  # Parse day column as a date type.
    print("Type of Day column: ", type(df["day"][0]))

    df.set_index("day",
                 inplace=True)  # Edit the current dataframe instead of returning a copy
    print(df)
    # fillna_examples()
    # interpolation_examples()
    dropna_examples()

    # Create a new dataframe that includes the missing dates from the old one.
    dates = pd.date_range("01-01-2022", "01-11-2022")
    new_index = pd.DatetimeIndex(dates)
    new_df = df.reindex(new_index)
    print("\n", new_df)

