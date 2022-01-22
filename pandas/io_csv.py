import pandas as pd


# Several read_csv features. Also returns a cleaner version of stock_data.csv
def reading_csvs():
    dfl = pd.read_csv("dataframes\\stock_data.csv",
                      skiprows=1)  # Ignore the header in the first row. Also works with header=1
    print(dfl)  # dfl = data frame local

    # Similar csv file, but without any headers. So we insert our own.
    dfl = pd.read_csv("dataframes\\stock_data2.csv",
                      header=None, names=["Tickers", "EPS", "Revenue", "Price"])
    print("\n", dfl)

    dfl = pd.read_csv("dataframes\\stock_data.csv",
                      header=1,
                      nrows=4,  # Read first 4 rows, excluding the header (tickers, eps, etc...)
                      na_values=['not available', 'n.a.']  # These 2 values will be replaced by NaN
                      )
    print("\n", dfl)

    dfl = pd.read_csv("dataframes\\stock_data.csv",
                      header=1,
                      na_values={  # Using a dictionary, we specify what values we want replaced for each column.
                          'eps': ['not available', 'n.a.'],
                          'revenue': ['not available', 'n.a.', -1],
                          'price': ['not available', 'n.a.'],
                          'people': ['not available', 'n.a.']
                      })
    print("\n", dfl)
    return dfl


# Some to_csv features that can be useful when writing a new csv file.
def writing_csvs(dfl):
    dfl.to_csv("dataframes\\stock_data_clean.csv",
               index=False,
               columns=["tickers", "eps"],  # Only write these 2 columns.
               header=False  # Without the header.
               )


if __name__ == '__main__':
    df = reading_csvs()
    # print("\nReturned:\n", df)
    df.to_csv("dataframes\\stock_data_clean.csv", index=False)  # Don't insert the index to the new csv

    writing_csvs(df)
