import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_string_dtype
import seaborn

def check_data(df, categorical_var, numerical_var):
    if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
        return 1
    if not is_string_dtype(df[categorical_var]) or not is_numeric_dtype(df[numerical_var]):
        return 1
    return 0

class Komparator(object):

    def __init__(self, df):
        try:
            if not isinstance(df, pd.DataFrame):
                raise TypeError
            self.df = df
        except TypeError:
            print("Wrong Type of inputs")        

    def compare_box_plots(self, categorical_var, numerical_var):           
        if check_data(self.df, categorical_var, numerical_var) == 1:
            print('COMPARE BOX PLOTS: error data types')
        dfilter = self.df[[categorical_var, numerical_var]].dropna()
        seaborn.boxplot(y=categorical_var, x=numerical_var, data=dfilter, orient='h')
        plt.show()

    
    def density(self, categorical_var, numerical_var):
        if check_data(self.df, categorical_var, numerical_var) == 1:
            print('DENSITY: error data types')
        dfilter = self.df[[categorical_var, numerical_var]].dropna()
        categories = dfilter[categorical_var].drop_duplicates().to_list()
        dfinal = dfilter.groupby(categorical_var)
        for i, rdm in enumerate(dfinal):
            ax = dfinal.get_group(categories[i])
            seaborn.distplot(ax[numerical_var], hist=False, kde=True, label=categories[i])
        plt.legend()
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        if check_data(self.df, categorical_var, numerical_var) == 1:
            print('COMPARE HIST: error data types')
        dfilter = self.df[[categorical_var, numerical_var]].dropna()
        categories = dfilter[categorical_var].drop_duplicates().to_list()
        dfinal = dfilter.groupby(categorical_var)
        for i, rdm in enumerate(dfinal):
            ax = dfinal.get_group(categories[i])
            plt.hist(ax[numerical_var], label=categories[i])
        plt.legend()
        plt.show()