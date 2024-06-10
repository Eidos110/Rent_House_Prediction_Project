import numpy as np
import json
import joblib


__locations = None
__data_columns =None
__model = None


def get_estimate_price(city,bhk,size,bathroom):
    try:
        loc_index = __data_columns.index(city.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = bhk
    x[1] = size
    x[2] = bathroom
    if loc_index>0:
        x[loc_index] = 1


    return round(__model.predict([x])[0],2)




def load_saved_artifacts():
    print("loading savad artifacts......Start!!!")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    if __model is None:
        with open("./artifacts/model_GB.pkl", "r") as f:
            __model = joblib.load(f)
    print("loading saved artifacts.....Done")


def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

