import pickle
import pandas as pd


from constants import COLUMNS
from encode import encode
from clean import clean


filename = 'model.sav'
model = pickle.load(open(filename, 'rb'))


def __build_input():
    df = pd.read_csv("input.csv")

    cleaned = clean(df)
    encoded = encode(cleaned)

    # print(encoded)

    final_df = pd.DataFrame([], columns=COLUMNS)

    print(pd.concat([final_df, encoded]))
    print(final_df.head())


def run_model(input):
    output = model.predict(input)
    print(output)


# run_model(__build_input())

__build_input()
