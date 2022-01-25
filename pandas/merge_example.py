import pandas as pd


def merge_simple():
    us_temperature = pd.DataFrame({
        "City": ["New York", "California", "Chicago"],
        "Temperature": [3, 9, -12]
    })

    us_humidity = pd.DataFrame({
        "City": ["California", "New York", "Chicago"],
        "Humidity": [87, 68, 61]
    })

    print("Original dataframes:\n", us_temperature, "\n\n", us_humidity)

    # Note: no need to add indexes in order to combine the dfs the right away, unlike with concat.
    us_complete = pd.merge(us_temperature, us_humidity, on="City")
    print("\nAfter merging the two:\n", us_complete)


def merge_types():
    """
    Merge 2 dataframes whose data don't line up perfectly.
    For example below: both dfs include cities that are missing from the other.
    Only cities included in both dfs will be added from the merge (like an SQL INNER JOIN).
    """
    us_temperature = pd.DataFrame({
        "City": ["New York", "California", "Orlando", "Ohio"],
        "Temperature": [3, 9, 11, -7]
    })

    us_humidity = pd.DataFrame({
        "City": ["California", "New York", "Chicago"],
        "Humidity": [87, 68, 61]
    })

    print("Original dataframes:\n", us_temperature, "\n\n", us_humidity)

    # Note: no need to add indexes in order to combine the dfs the right away, unlike with concat.
    us_merge1 = pd.merge(us_temperature, us_humidity, on="City")
    print("\nAfter merging the two (inner):\n", us_merge1)

    us_merge2 = pd.merge(us_temperature, us_humidity, on="City", how="outer")
    print("\nAfter merging the two (outer):\n", us_merge2)

    us_merge3 = pd.merge(us_temperature, us_humidity, on="City", how="left")
    print("\nAfter merging the two (left):\n", us_merge3)

    us_merge4 = pd.merge(us_temperature, us_humidity, on="City", how="right",
                         indicator=True)  # Displays from which df each row is.
    print("\nAfter merging the two (right):\n", us_merge4)


def merge_suffixes():
    us_weather1 = pd.DataFrame({
        "City": ["New York", "California", "Orlando", "Ohio"],
        "Temperature": [3, 9, 11, -7],
        "Humidity": [68, 87, 58, 81]
    })

    us_weather2 = pd.DataFrame({
        "City": ["California", "New York", "Chicago"],
        "Temperature": [9, 3, -12],
        "Humidity": [87, 68, 61]
    })

    us_merge = pd.merge(us_weather1, us_weather2, on="City")
    print(us_merge)

    us_merge = pd.merge(us_weather1, us_weather2, on="City", suffixes=["_A", "_B"])
    print("\n", us_merge)


if __name__ == '__main__':
    # merge_simple()
    # merge_types()
    merge_suffixes()
