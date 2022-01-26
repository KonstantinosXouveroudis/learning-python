import pandas as pd
from numpy import random as rnd
import jinja2  # For LaTeX
from astropy.table import Table  # To read a LaTeX table
import lxml


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


if __name__ == '__main__':
    # io_json()
    # io_LaTeX()
    io_xml()

