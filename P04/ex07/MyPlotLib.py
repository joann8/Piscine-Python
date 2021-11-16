import pandas as pd
from pandas.api.types import is_numeric_dtype
import seaborn

def check_data(data, features):
    if isinstance(data, pd.DataFrame) and isinstance(features, list):
        for word in features:
            if not isinstance(word, str):
                return 1
        return 0
    return 1

class MyPlotLib(object):

    @staticmethod
    def histogram(data, features):
        if check_data(data, features) == 1:
            print('HISTOGRAM: error data types')
        else:
            for word in features:
                if not is_numeric_dtype(data[word]):
                    print('HISTOGRAM: %s - error data types' %(word))
                    features.remove(word)
            dfilter = data[features]
            dfilter.hist()

    @staticmethod
    def density(data, features):
        if check_data(data, features) == 1:
            print('DENSITY: error data types')
        else:       
            for word in features:
                if not is_numeric_dtype(data[word]):
                    print('DENSITY: %s - error data types' %(word))
                    features.remove(word)
            dfilter = data[features]
            dfilter.plot.kde()
    
    @staticmethod
    def pair_plot(data, features):
        if check_data(data, features) == 1:
            print('PAIR_PLOT: error data types')
        else:
            for word in features:
                if not is_numeric_dtype(data[word]):
                    print('PAIT PLOT: %s - error data types' %(word))
                    features.remove(word)
            dfilter = data[features]
            seaborn.pairplot(dfilter)

    @staticmethod
    def box_plot(data, features):   
        if check_data(data, features) == 1:
            print('BOX_PLOT: error data types')
        else:
            for word in features:
                if not is_numeric_dtype(data[word]):
                    print('BOX PLOT: %s - error data types' %(word))
                    features.remove(word)
            dfilter = data[features]
            dfilter.boxplot()