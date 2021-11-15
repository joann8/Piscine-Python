import pandas as pd

def howManyMedals(df, participant):
    dico = {}
    if isinstance(df, pd.DataFrame) and isinstance(participant, str):
        df_part = df[df['Name'] == participant]
        for index, row in df_part.iterrows():
            if list(dico.keys()).count(row['Year']) == 0:
                dico[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
            if isinstance(row['Medal'], str):
                dico[row['Year']][row['Medal'][0]] += 1
    else:
        print("MEDALS: wrong inputs types")
    return dico

