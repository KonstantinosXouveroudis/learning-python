import json
import pickle
import numpy as np

# Local variables
__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    # Catching it in an exception in case we don't find the index.
    try:
        loc_index = __data_columns.index(location.lower())  # Lowercase, like our json file.
    except:
        loc_index = -1

    """
    The x array has one value for each column in our dataset.
    Give our sqft, bath and bhk values to the first 3 values.
    All other values will be 0 except for our location, which will be 1.
    We do this to find the correct column for our location. 
    """
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    # Return a double array. Since it only has one value, return [0]. Also round it to 2 decimals.
    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns  # Treat these 2 as global variables.
    global __locations

    # Data columns json file
    with open("artifacts\\columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        # The first 3 columns are total_sqft, bath and bhk. We want the locations, so everything after that.
        __locations = __data_columns[3:]

    global __model  # Need to define it as global to avoid 'NoneType' error.

    # The trained model
    with open("artifacts\\banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)
    print("Loading saved artifacts...complete")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())

    # Predictions (location, sqft, bhk, bath)
    print(get_estimated_price('1st Phas JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phas JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))
