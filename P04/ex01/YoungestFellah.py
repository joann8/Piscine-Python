import pandas as pd

def youngfellah(df, year):
    """
    Get the name of the youngest woman and man for the given year.
    Args:
        df: pandas.DataFrame object containing the dataset.
        year: integer corresponding to a year.
    Returns:
        dct: dictionary with 2 keys for female and male athlete.
    """
    if isinstance(df, pd.DataFrame) and isinstance(year,int):
        df2 = df[df['Year'] == year][['Sex', 'Age']]
        dff = df2[df2['Sex'] == 'F']
        dfm = df2[df2['Sex'] == 'M']
        return {'f' : dff.min()['Age'] , 'm' : dfm.min()['Age']}