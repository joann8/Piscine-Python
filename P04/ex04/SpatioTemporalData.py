import pandas as pd

class SpatioTemporalData:

    def __init__(self, df):
        try:
            if not isinstance(df, pd.DataFrame):
                raise TypeError        
            self.df = df 
        except TypeError:
            print("Wrong Type of inputs")

    def when(self, location):
        if isinstance(location, str):
            dloc = self.df[self.df['City'] == location]
            mylist = [] 
            for index, row in dloc.iterrows():
                if row['Year'] not in mylist:
                    mylist.append(row['Year'])
            return mylist   

    def where(self, date):
        if isinstance(date, int):
            ddate = self.df[self.df['Year'] == date]
            mylist = [] 
            for index, row in ddate.iterrows():
                if row['City'] not in mylist:
                    mylist.append(row['City'])
            return mylist   