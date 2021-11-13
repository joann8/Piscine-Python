import sys
from csvreader import CsvReader
import numpy as np
from random import randint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def distance(x, y):
    return np.sum(np.abs(y - x), axis=1)

def distortion(X, Y):
    return -np.sum(np.abs(X - Y) ** 2)

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        try:
            if max_iter is not None:
                if not isinstance(max_iter, int) or max_iter < 1: 
                    raise ValueError("Pbm max_iter")
            if ncentroid is not None:
                if not isinstance(ncentroid, int) or ncentroid < 1: 
                    raise ValueError("Pbm ncentroid")
            self.ncentroid = ncentroid # number of centroids
            self.max_iter = max_iter # number of max iterations to update the centroids
            self.centroids = [] # values of the centroid
        except IOError as err:
            sys.stderr.write("I/O error({0}): {1}".format(err.errno, err.strerror))
    
    def fit(self, X): 

        """
            Run the K-means clustering algorithm.
            For the location of the initial centroids, random pick ncentroids from the dataset.
            Args:
                X: has to be an numpy.ndarray, a matrice of dimension m * n.
            Returns:
                None.
            Raises:
                This function should not raise any Exception.
            """
        if not isinstance(X, np.ndarray):
            print("This array is not an numpy array")
            return 
        for i in range(self.ncentroid):
            x = randint(0, X.shape[0] - 1)
            self.centroids.append(X[x,:])
        print("\nSelf centroids are: ")
        print(self.centroids)

    def predict(self, X): 
        """
            Predict from wich cluster each datapoint belongs to.
            Args:
                X: has to be an numpy.ndarray, a matrice of dimension m * n.
            Returns:
                the prediction has a numpy.ndarray, a vector of dimension m * 1.
            Raises:
                This function should not raise any Exception.
        """



if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Wrong args")
        quit()
    file_path = sys.argv[1]
    ncentroid = int(sys.argv[2])
    max_iter = int(sys.argv[3])
    kmeans = KmeansClustering(max_iter, ncentroid)

    with CsvReader(file_path) as file:
        if file == None:
            print("File is corrupted")
            quit()
        file.header = True
        file.skip_top = 2
        print("\n******* GET DATA & HEADER ********")
        data = file.getdata()
        header = file.getheader()
        print(header) 
        raw_data = np.array(data)
        slice_data = raw_data[:, 1:]
        print(slice_data)

        fig = plt.figure(height=600, width=600, layout={'width':'100%', 'height':'100%'})
        scatter = plt.scatter(*slice_data.T, size=1, marker="sphere")
        plt.xyzlim(-10, 10)
        plt.show()


        # kmeans.fit(slice_data)
        # plt.rcParams["figure.figsize"] = [7.00, 3.50]
        # plt.rcParams["figure.autolayout"] = True
        # fig = plt.figure()
        # ax = fig.add_subplot(111, projection='3d')
        # data = np.random.random(size=(3, 3, 3))
        # z, x, y = data.nonzero()
        # ax.scatter(x, y, z, c=z, alpha=1)
        # plt.show()`






    
