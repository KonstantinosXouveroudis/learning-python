import pandas as pd
import openpyxl  # Was needed to read excel

# Different ways to create a dataframe using pandas
# More to experiment with (in exercises directory): https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

if __name__ == '__main__':
    # 1) Read Excel
    df_excel = pd.read_excel(
        "dataframes\\weather_data.xlsx", "Sheet1")
    print("Excel:\n", df_excel)

    # 2) Read a CSV file
    df_csv = pd.read_csv("dataframes\\weather_data.csv")
    print("\nCSV:\n", df_csv)

    # 3) Python dictionary
    weather_dict = {
        'Day': ['1/1/2022', '1/2/2022', '1/3/2022', '1/4/2022', '1/5/2022', '1/6/2022'],
        'Temperature': [32, 35, 28, 24, 32, 31],
        'Wind Speed': [6, 7, 2, 7, 4, 2],
        'Event': ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny']
    }
    df_dict = pd.DataFrame(weather_dict)
    print("\nPython Dictionary:\n", df_dict)

    # 4) List of Python dictionaries
    weather_dict_list = [
        {'Day': '1/1/2022', 'Temperature': 32, 'Wind Speed': 6, 'Event': 'Rain'},
        {'Day': '1/2/2022', 'Temperature': 35, 'Wind Speed': 7, 'Event': 'Sunny'},
        {'Day': '1/3/2022', 'Temperature': 28, 'Wind Speed': 2, 'Event': 'Snow'},
    ]
    df_dict_list = pd.DataFrame(weather_dict_list)
    print("\nList of Python Dictionaries:\n", df_dict_list)

    # 5) List of Python tuples
    weather_tuple = [
        ('1/1/2022', 32, 6, 'Rain'),
        ('1/2/2022', 35, 7, 'Sunny'),
        ('1/3/2022', 28, 2, 'Snow')
    ]
    df_tuple = pd.DataFrame(weather_tuple, columns=["Day", "Temperature", "Wind Speed", "Event"])
    print("\nPython Tuple:\n", df_tuple)
