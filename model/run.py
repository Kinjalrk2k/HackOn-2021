import pickle
import pandas as pd
import numpy as np


from constants import COLUMNS
from encode import encode
from clean import clean


filename = 'model.sav'
model = pickle.load(open(filename, 'rb'))


def __build_input():
    df = pd.read_csv("input.csv")

    cleaned = clean(df)
    # print(cleaned)

    encoded = encode(cleaned)

    final_df = pd.DataFrame([], columns=COLUMNS)

    concated_df = pd.concat([final_df, encoded], sort=True)
    concated_df = concated_df.replace(np.nan, 0)
    return concated_df.head()


def run_model(input):
    output = model.predict(input)
    print(output)


run_model(__build_input())
