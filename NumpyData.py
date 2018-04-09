# early test scripting for Project-2018 by Colm Doherty, started on 2018-4-4 to learn how to manipulate the dataset to 
# discover the max, min and mean values in each column. My initial source for methodolgy was a free tutorial at
# https://www.youtube.com/watch?v=Tq6rCWPdXoQ, then I referred to an essay on "Functions, modules, packages and libraries"
# recommended by Ian McLoughlin at: 
# https://nbviewer.jupyter.org/github/ianmcloughlin/python-fundamentals-notes/blob/master/functions-modules.ipynb#

import numpy as np
import matplotlib.pyplot as plt
    # importing the numpy & matplot libraries to help manipulate the data, and giving them shorthand names

data = np.genfromtxt('Data/Iris.csv', delimiter=',')
    # importing the iris dataset, as a csv file
print (data[:,0]) 
    # show the first column of the dataset



    

