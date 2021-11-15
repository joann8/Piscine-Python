import sys
from csvreader import CsvReader
import numpy as np
from random import randint
import matplotlib.pyplot as plt
import copy

def distance(X, Y):
      return np.square(X[0] - Y[0]) + np.square(X[1] -Y[1]) + np.square(Y[2] - Y[2])

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
            self.scores = []
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
        all_centroids = []
        scores =[]
        for i in range(self.max_iter):
            self.centroids.clear()
            for j in range(self.ncentroid):
                x = randint(0, X.shape[0] - 1)
                self.centroids.append(X[x,:]) #effacee a chaque tour
            all_centroids.append([copy.deepcopy(self.centroids)])
            self.predict(X)
        index_min = self.scores.index(min(self.scores))
        self.centroids.clear()
        for i in range(0, len(all_centroids[index_min][0])):
            self.centroids.append(copy.deepcopy(all_centroids[index_min][0][i]))
    
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
        res = np.zeros((X.shape[0], self.ncentroid))
        for j in range(0, self.ncentroid): #pour les 4 points donnes
            for i in range(0, X.shape[0]): #pour toutes les lignes
                res[i, j] = distance(X[i], self.centroids[j]) # calcul de la distance du point
        new_tab = np.argmin(res, 1).reshape((X.shape[0], 1)) 
        #on prends la distance min --> on renvoie l'index avec argmin et on reshape le tableau em m * 1
        
        score = 0.0 #on peut ameliorer le score en changeant le pids du calcul par category (distance a differentier en fonction de l'echelle)
        for i in range(0, res.shape[0]): #pour toutes les lignes
            score += res[i, new_tab[i]] # calcul de la somme des distances
        self.scores.append(score[0])
        return new_tab


def plot_res_3d(X, y, header, kmeans):

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    color= ["lightpink", "cyan", "lightgreen", "salmon"]
    for j in range(0, kmeans.ncentroid):
        for i in range(X.shape[0]):
            if ord[i] == j:
                ax.scatter(X[i][0], X[i][1], X[i][2], c=color[j % 4])
    
    color2= ["magenta", "b", "g", "r"]
    for i in range(0, kmeans.ncentroid):
        ax.scatter(kmeans.centroids[i][0], kmeans.centroids[i][1], kmeans.centroids[i][2], c=color2[i % 4])
    ax.set_xlabel(header[1])
    ax.set_ylabel(header[2])
    ax.set_zlabel(header[3])

    plt.show()

def plot_res_2d(X, ord, header, kmeans, x, y):

    fig = plt.figure()
    ax = fig.subplots(1, 1)

    color= ["lightpink", "cyan", "lightgreen", "salmon"]
    for j in range(0, kmeans.ncentroid):
        for i in range(X.shape[0]):
            if ord[i] == j:
                ax.scatter(X[i][x], X[i][y], c=color[j % 4])
    
    color2= ["magenta", "b", "g", "r"]
    for i in range(0, kmeans.ncentroid):
        ax.scatter(kmeans.centroids[i][x], kmeans.centroids[i][y], c=color2[i % 4])
    
    ax.set_xlabel(header[x])
    ax.set_ylabel(header[y])

    plt.show()



if __name__ == "__main__":

    try:
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
            
            #print("\n******* GET DATA & HEADER ********")
            data = file.getdata()
            header = file.getheader()
            file.__exit__  
            
        #print("\n******* KMEANS FIT ET PREFICT ********")
        raw_data = np.array(data).astype(float)
        raw_data = np.delete(raw_data, 0, 1)
        kmeans.fit(raw_data)
        ord = kmeans.predict(raw_data)

        #print("\n******* PRINT FINAL ********")
        plot_res_3d(raw_data, ord, header, kmeans)
        plot_res_2d(raw_data, ord, header[1:], kmeans, 0, 1)
        plot_res_2d(raw_data, ord, header[1:], kmeans, 0, 2)
        plot_res_2d(raw_data, ord, header[1:], kmeans, 1, 2)

    except ValueError as err:
        print(err.args)
