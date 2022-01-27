import pandas as pd
from numpy import random as rnd
import jinja2  # For LaTeX
from astropy.table import Table  # To read a LaTeX table
import pymysql
from sqlalchemy import create_engine


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
    rand_choice = rnd.randint(0, 2)
    for idx, row in df_json.iterrows():
        if rand_choice == 0:  # If our random equals 0, decrease. Otherwise increase.
            df_json.at[idx, 'Temperature'] = row['Temperature'] - 1
        else:
            df_json.at[idx, 'Temperature'] = row['Temperature'] + 1

    print("\n", df_json)
    df_json.to_json("io_data\\weather_data_edit.json")

    # This also works if you don't want the indexes. However, we won't be able to read it as a json if we need it again.
    # df_json.to_json("dataframes\\io_data\\weather_data_edit.json", orient="split", index=False)


def io_LaTeX():
    # The basic example from the pandas documentation.
    df_latex = pd.DataFrame([[1, 2], [3, 4]], index=["a", "b"], columns=["c", "d"])
    print(df_latex)
    print("\n\n", df_latex.style.to_latex())

    """"
    A dictionary containing characters from the game Dead by Daylight, 
    converted to LaTeX format and exported to a .tex
    """
    df_dbd = pd.DataFrame({'Name': ['Evan MacMillan', 'Philip Ojomo', 'Anna', 'Michael Myers', 'Carmina Mora'],
                           'Title': ['The Trapper', 'The Wraith', 'The Huntress', 'The Shape', 'The Artist'],
                           'Weapon': ['Cleaver', 'Azarov\'s Skull', 'Broad Axe', 'Kitchen Knife',
                                      'Sharp Palette Blade'],
                           'Power': ['Bear Trap', 'Wailing Bell', 'Hunting Hatchets', 'Evil Within', 'Birds of Torment']
                           })
    print("\n", df_dbd)
    print("\n", df_dbd.style.to_latex())
    df_dbd.to_latex("io_data\\dbd_killers_list.tex", index=False)

    df = Table.read("io_data\\dbd_killers_list.tex").to_pandas()
    print("\nReading the tabular from the .tex file:\n", df)
    print("Class of the table above:", type(df))


def io_xml():
    df_xml = pd.read_xml("io_data\\bookstore.xml")
    print("Reading an xml from our own directories:\n", df_xml)

    # Creating a new dataframe which we'll append to the xml.
    df_custom = pd.DataFrame({
        "category": ["music", "literature"],
        "title": ["Just Kids", "Deaf Sentence"],
        "author": ["Patti Smith", "David Lodge"],
        "year": [2010, 2008],
        "price": [32.99, 24.00]
    })

    df_xml = df_xml.append(df_custom, ignore_index=True)
    print("\n\nAfter appending some new lines:\n", df_xml)

    df_xml.to_xml("io_data\\bookstore_edit.xml")

    df_xml2 = pd.read_xml("https://www.w3schools.com/xml/books.xml")
    print("\n\nReading an xml from an online source:\n", df_xml2)


def io_mysql():
    passwd = input('Enter password: ')
    engine = create_engine(f'mysql+pymysql://root:{passwd}@localhost:3306/my_test_db')
    df_sql = pd.read_sql_table("shop", engine)
    print(df_sql)

    # Select these 2 columns from the shop table in the database my_test_db.
    df_sql = pd.read_sql_table("shop", engine, columns=['dealer', 'price'])
    print("\n", df_sql)

    # Inner Join
    query = """
    SELECT customers.name, customers.phone_number, orders.name, orders.amount
    FROM customers INNER JOIN orders
    ON customers.id = orders.customer_id;
    """
    df_sql = pd.read_sql_query(query, engine)
    print("\n", df_sql)

    # Writing new data in the db.
    df = pd.read_csv("io_data\\customers.csv")
    df.rename(columns={  # We need to rename the dataframe's columns to match the db's.
        'Customer Name': 'name',
        'Customer Phone': 'phone_number'
    }, inplace=True)
    print("\n", df)

    df.to_sql(
        name='customers',
        con=engine,
        index=False,
        if_exists='append'
    )
    """
    if_exists{‘fail’, ‘replace’, ‘append’}, default ‘fail’
    How to behave if the table already exists.
        fail: Raise a ValueError.
        replace: Drop the table before inserting new values.
        append: Insert new values to the existing table.
    """

    # We can also add a query as the first parameter
    print(pd.read_sql("customers", engine, columns=['name', 'phone_number']))


if __name__ == '__main__':
    # io_json()
    # io_LaTeX()
    # io_xml()
    io_mysql()
