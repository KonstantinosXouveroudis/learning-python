import pandas as pd


def concat_rows():
    us_weather = pd.DataFrame({
        "City": ["New York", "California", "Chicago"],
        "Temperature": [3, 9, -12],
        "Humidity": [68, 87, 61]
    })

    england_weather = pd.DataFrame({
        "City": ["London", "Manchester", "Bristol"],
        "Temperature": [3, 2, 3],
        "Humidity": [83, 84, 90]
    })

    greece_weather = pd.DataFrame({
        "City": ["Athens", "Thessaloniki", "Kavala"],
        "Temperature": [4, 1, 2],
        "Humidity": [59, 39, 40]
    })

    dfl = pd.concat([us_weather, england_weather, greece_weather],
                    ignore_index=True)
    print(dfl)

    dfl = pd.concat([us_weather, england_weather, greece_weather],
                    keys=["US", "England", "Greece"])  # We can't use keys if we set ignore_index to true.
    print("\n", dfl)

    print("\nShow me the weather data for Greece only:\n", dfl.loc["Greece"])


def concat_columns():
    us_weather = pd.DataFrame({
        "City": ["New York", "California", "Chicago"],
        "Temperature": [3, 9, -12]
    })

    us_windspeed = pd.DataFrame({
        "City": ["New York", "California", "Chicago"],
        "Wind Speed": [8, 2, 16]
    })

    df = pd.concat([us_weather, us_windspeed["Wind Speed"]],
                   axis=1)  # Concats columns. By default, axis=0 (concats rows).
    print(df)

    """"
    Same example, but the windspeed dataframe doesn't match with the weather one
    (different order of cities, missing cities).
    In order for the concat to be accurate, we add corresponding indexes.
    """
    us_weather = pd.DataFrame({
        "City": ["New York", "California", "Chicago"],
        "Temperature": [3, 9, -12]
    }, index=[0, 1, 2])

    us_windspeed = pd.DataFrame({
        "City": ["Chicago", "California"],
        "Wind Speed": [16, 2]
    }, index=[2, 1])

    df = pd.concat([us_weather, us_windspeed['Wind Speed']], axis=1)
    print("\n", df)

    """
    Concat a series of additional data (Event) to us_weather.
    """
    us_events = pd.Series(["Cloudy", "Fog", "Clear"], name="Event", index=[0, 1, 2])
    print("\n", us_events)
    us_weather = pd.concat([us_weather, us_events], axis=1)
    print("\nAfter adding Event column to the rest of the weather dataframe:\n", us_weather)


if __name__ == '__main__':
    # concat_rows()
    concat_columns()


