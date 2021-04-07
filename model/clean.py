import pandas as pd


def clean(df):

    # Dropping columns not necessary for data analysis
    df.drop(['Timestamp', 'comments', 'state', 'Country', 'phys_health_interview', 'phys_health_consequence'],
            axis=1, inplace=True)

    # Dropping nan values and changing age column to intg.
    try:
        df.work_interfere.dropna(inplace=True)
    except Exception:
        pass

    df.self_employed.dropna(inplace=True)
    df['Age'] = df['Age'].astype(int)

    # creating a uniform values for vairous unique gender values

    df['Gender'] = df['Gender'].replace({'f': 'F'})
    df['Gender'] = df['Gender'].replace({'female': 'F'})
    df['Gender'] = df['Gender'].replace({'Male': 'M'})
    df['Gender'] = df['Gender'].replace({'male': 'M'})
    df['Gender'] = df['Gender'].replace({'Female': 'F'})
    df['Gender'] = df['Gender'].replace({'m': 'M'})
    df['Gender'] = df['Gender'].replace({'Make': 'M'})
    df['Gender'] = df['Gender'].replace({'Woman': 'F'})
    df['Gender'] = df['Gender'].replace({'Man': 'M'})
    df['Gender'] = df['Gender'].replace({'Femake': 'F'})
    df['Gender'] = df['Gender'].replace({'Malr': 'M'})
    df['Gender'] = df['Gender'].replace({'Mail': 'M'})
    df['Gender'] = df['Gender'].replace({'femail': 'F'})
    df['Gender'] = df['Gender'].replace({'Female ': 'F'})
    df['Gender'] = df['Gender'].replace({'Female (trans)': 'trans'})
    df['Gender'] = df['Gender'].replace({'Trans-female': 'trans'})
    df['Gender'] = df['Gender'].replace({'Trans woman': 'trans'})
    df['Gender'] = df['Gender'].replace({'Cis Male': 'M'})
    df['Gender'] = df['Gender'].replace({'Cis Male': 'M'})
    df['Gender'] = df['Gender'].replace({'cis-female/femme': 'F'})
    df['Gender'] = df['Gender'].replace({'cis male': 'M'})
    df['Gender'] = df['Gender'].replace({'Cis Man': 'M'})
    df['Gender'] = df['Gender'].replace({'maile': 'M'})
    df['Gender'] = df['Gender'].replace({'Mal': 'M'})
    df['Gender'] = df['Gender'].replace({'Cis Female': 'F'})
    df['Gender'] = df['Gender'].replace({'woman': 'F'})
    df['Gender'] = df['Gender'].replace({'Female (cis)': 'F'})
    df['Gender'] = df['Gender'].replace({'Male ': 'M'})
    df['Gender'] = df['Gender'].replace({'Male (CIS)': 'M'})
    df['Gender'] = df['Gender'].replace({'msle': 'M'})
    df['Gender'] = df['Gender'].replace({'queer/she/they': 'queer'})
    df['Gender'] = df['Gender'].replace({'queer': 'queer'})
    df['Gender'] = df['Gender'].replace({'Genderqueer': 'queer'})
    df['Gender'] = df['Gender'].replace({'fluid': 'queer'})
    df['Gender'] = df['Gender'].replace({'non-binary': 'queer'})
    df['Gender'] = df['Gender'].replace({'Androgyne': 'queer'})
    df['Gender'] = df['Gender'].replace({'male leaning androgynous': 'queer'})
    df['Gender'] = df['Gender'].replace({'Agender': 'queer'})
    df['Gender'] = df['Gender'].replace({'something kinda male?': 'other'})
    df['Gender'] = df['Gender'].replace({'Nah': 'other'})
    df['Gender'] = df['Gender'].replace({'Agender': 'other'})
    df['Gender'] = df['Gender'].replace({'Neuter': 'other'})
    df['Gender'] = df['Gender'].replace({'p': 'other'})
    df['Gender'] = df['Gender'].replace({'Guy (-ish) ^_^': 'other'})
    df['Gender'] = df['Gender'].replace({'Male-ish': 'other'})
    df['Gender'] = df['Gender'].replace({'A little about you': 'other'})
    df['Gender'] = df['Gender'].replace({'Enby': 'other'})
    df['Gender'] = df['Gender'].replace({'All': 'other'})
    df['Gender'] = df['Gender'].replace(
        {'ostensibly male, unsure what that really means': 'other'})

    try:
        df['work_interfere'] = df['work_interfere'].replace(
            {'Sometimes': 'yes'})
        df['work_interfere'] = df['work_interfere'].replace({'Often': 'yes'})
        df['work_interfere'] = df['work_interfere'].replace({'Rarely': 'no'})
        df['work_interfere'] = df['work_interfere'].replace({'Never': 'no'})
    except Exception:
        pass

    # consoldating two employee sizes

    df['no_employees'] = df['no_employees'].replace({'1-5': '1-25'})
    df['no_employees'] = df['no_employees'].replace({'6-25': '1-25'})

    df.self_employed.dropna(axis=0, inplace=True)
    # df.self_employed.isna().sum()

    # Dropping all null values in df
    df.dropna(inplace=True)

    # Replacing unique(incorrectly entered age values with 1 in order to change it with the mean after)
    for age in df.Age.values:
        if age <= 17 or age >= 80:
            df.Age.replace(age, 1, inplace=True)

    # changing ones with the column mean and rounding it in to two
    df['Age'] = df['Age'].replace({1: df.Age.mean()})
    df.Age = df.Age.round(2)

    return df
