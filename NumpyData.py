# early test scripts for Project-2018 by Colm Doherty, started on 2018-4-4
# to figure out how to manipulate the dataset to discover max, min and mean 
# values in each column. initial source for methodolgy is a
# free tutorial at https://www.youtube.com/watch?v=Tq6rCWPdXoQ


import numpy as np
import matplotlib.pyplot as plt
    # importing the numpy & matplot libraries to help manipulate the data, and giving them shorthand names

data = np.genfromtxt('Data/Iris.csv', delimiter=',')
    # importing the iris dataset, as a csv file

print (data)
    # to establish that the Iris dataset was imported ok ? hmmm

