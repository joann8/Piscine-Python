import pandas as pd

def howManyMedalsByCountry(df, country):
    if isinstance(df, pd.DataFrame) and isinstance(country, str):
        team_sports = ['Basketball', 'Football',  'Tug-Of-War', 'Badminton', 'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh', 'Softball', 'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo']
        dcountry = df[df['Team'] == country]
        dco = dcountry[dcountry['Sport'].isin(team_sports)]
        dco2 = dco[['Year', 'Sport', 'Sex', 'Medal']].drop_duplicates().sort_values('Sport')
        dindiv = dcountry[~dcountry['Sport'].isin(team_sports)]
        dico = {}
        for index, row in dindiv.iterrows():
            if list(dico.keys()).count(row['Year']) == 0:
                dico[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
            if isinstance(row['Medal'], str):
                dico[row['Year']][row['Medal'][0]] += 1
        for index, row in dco2.iterrows():
            if list(dico.keys()).count(row['Year']) == 0:
                dico[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
            if isinstance(row['Medal'], str):
                dico[row['Year']][row['Medal'][0]] += 1
        return dico
        

