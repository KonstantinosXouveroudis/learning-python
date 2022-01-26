import pandas as pd
import random as rnd


def io_json():
    # Not quite the right format, but still displaying it to remember how pandas reads it.
    df_json = pd.read_json("io_data\\book.json")
    print(df_json)

    # Correct format.
    df_json = pd.read_json("io_data\\weather_data.json")
    print("\n", df_json)

    """
    Below we play around with the weather data slightly.
    We use a random integer (either 0 or 1) to decide whether we will increase the temperature for each row
    by 1, or increment it by 1. We then write the data we end up with in a new json.
    """
    rand_choice = rnd.randrange(0, 2)
    for idx, row in df_json.iterrows():
        if rand_choice == 0:  # If our random equals 0, decrease. Otherwise increase.
            df_json.at[idx, 'Temperature'] = row['Temperature'] - 1
        else:
            df_json.at[idx, 'Temperature'] = row['Temperature'] + 1

    print("\n", df_json)
    df_json.to_json("io_data\\weather_data_edit.json")

    # This also works if you don't want the indexes. However, we won't be able to read it as a json if we need it again.
    # df_json.to_json("dataframes\\io_data\\weather_data_edit.json", orient="split", index=False)


if __name__ == '__main__':
    io_json()
