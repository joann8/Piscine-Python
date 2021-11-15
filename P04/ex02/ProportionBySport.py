import pandas as pd
from FileLoader import FileLoader

#Enonce : We assume that we are always using appropriate arguments as input, and thus do notneed to handle input errors.
#verifier proportion  de l'exemple
def proportionBySport(df, year, sport, sex):
    dfyear = df[df['Year'] == year]
    dfsex = dfyear[dfyear['Sex'] == sex]
    dfsport = dfsex[dfsex['Sport']== sport]
    return dfsport.shape[0] / dfsex.shape[0] 
