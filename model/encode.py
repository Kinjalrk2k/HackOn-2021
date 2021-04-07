import pandas as pd
from sklearn.preprocessing import PolynomialFeatures, StandardScaler, OneHotEncoder


def encode(X):
    cont = X.select_dtypes(exclude='object')
    cat = X.select_dtypes(include='object')

    # ohe = OneHotEncoder(drop='first')
    ohe = OneHotEncoder()
    train = ohe.fit_transform(cat).toarray()
    train_df = pd.DataFrame(train, columns=ohe.get_feature_names(cat.columns))
    # print(train_df["Gender_M"])
    train_df.head(2)

    train_df.reset_index(inplace=True, drop='first')
    cont.reset_index(inplace=True, drop='first')

    return train_df.join(cont)
