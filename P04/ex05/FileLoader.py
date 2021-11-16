from os import error
import pandas as pd

class FileLoader():

    @staticmethod
    def load(path):
        try:
            df = pd.read_csv(path)
            print("Loading data set of dimension %d x %d" %(df.shape[0], df.shape[1]))
            return df
        except Exception as err:
            print("LOAD : ", err.args[1])
            return None
        
    @staticmethod
    def display(df, n):
        if isinstance(df, pd.DataFrame) and isinstance(n,int) and n > 0:
            print(df[:n])
        else:
            print("DISPLAY : Types Error")
