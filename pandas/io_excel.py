import pandas as pd
import openpyxl  # Was needed to read excel


def convert_people_cell(cell):
    if cell == "n.a." or cell == "not available":
        return "sam walton"
    return cell


def io_excel_basics():
    dfl = pd.read_excel("dataframes\\stock_data.xlsx", "Sheet1")
    print(dfl)

    dfl = pd.read_excel("dataframes\\stock_data.xlsx", "Sheet1",
                        converters={
                           'people': convert_people_cell
                       })
    print("\n", dfl)

    dfl.to_excel("dataframes\\stock_data_edit.xlsx", sheet_name="stocks",
                 startrow=1, startcol=3,
                 index=False)


def insert_two_dfs():
    df_stocks = pd.DataFrame({
        'Tickers': ['GOOGL', 'WMT', 'MSFT'],
        'Price': [845, 65, 64],
        'PE': [30.37, 14.26, 30.97],
        'EPS': [27.82, 4.61, 2.12]
    })

    df_weather = pd.DataFrame({
        'Day': ['1/1/2022', '1/2/2022', '1/3/2022'],
        'Temperature': [32, 35, 28],
        'Event': ['Rain', 'Sunny', 'Snow']
    })

    # Inserting both of these dfs into the same Excel file, in different sheets.
    with pd.ExcelWriter('dataframes\\stocks_weather.xlsx') as writer:
        df_stocks.to_excel(writer, sheet_name="Stocks", index=False)
        df_weather.to_excel(writer, sheet_name="Weather", index=False)


if __name__ == '__main__':
    # io_excel_basics()
    insert_two_dfs()


