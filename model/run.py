import pickle
import pandas as pd
import numpy as np


from .constants import COLUMNS
from .encode import encode
from .clean import clean


filename = './model/model.sav'
model = pickle.load(open(filename, 'rb'))


def build_input(input_dict):
    # df = pd.read_csv("./model/input.csv")
    df = pd.DataFrame.from_dict(convert_to_dict_array(input_dict))

    cleaned = clean(df)
    # print(cleaned)

    encoded = encode(cleaned)

    final_df = pd.DataFrame([], columns=COLUMNS)

    concated_df = pd.concat([final_df, encoded], sort=True)
    concated_df = concated_df.replace(np.nan, 0)
    return concated_df.head()


def run_model(input):
    output = model.predict(input)
    return output[0]


input_dict = {
    "Timestamp": "27-08-2014 11:33",
    "Age": "36",
    "Gender": "Male",
    "Country": "United States",
    "state": "CT",
    "self_employed": "Yes",
    "family_history": "Yes",
    "treatment": "No",
    "no_employees": "500-1000",
    "remote_work": "No",
    "tech_company": "Yes",
    "benefits": "Don't know",
    "care_options": "Not sure",
    "wellness_program": "No",
    "seek_help": "Don't know",
    "anonymity": "Don't know",
    "leave": "Don't know",
    "mental_health_consequence": "No",
    "phys_health_consequence": "No",
    "coworkers": "Yes",
    "supervisor": "Yes",
    "mental_health_interview": "No",
    "phys_health_interview": "No",
    "mental_vs_physical": "Don't know",
    "obs_consequence": "No",
    "comments": "I'm not on my company's health insurance which could be part of the reason I answered Don't know to so many questions."
    # 27-08-2014 11:33,36,Male,United States,CT,Yes,Yes,No,500-1000,No,Yes,Don't know,Not sure,No,Don't know,Don't know,Don't know,No,No,Yes,Yes,No,No,Don't know,No,I'm not on my company's health insurance which could be part of the reason I answered Don't know to so many questions.
}


def convert_to_dict_array(input_dict):
    for (key, value) in input_dict.items():
        input_dict[key] = [value]
    return input_dict


print(run_model(build_input(input_dict)))
