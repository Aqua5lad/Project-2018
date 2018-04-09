# early test scripts for Project-2018 by Colm Doherty, started on 2018-4-4
# to figure out how to manipulate the dataset to discover max, min and mean 
# values in each column. initial source for methodolgy was a
# free tutorial at https://www.youtube.com/watch?v=Tq6rCWPdXoQ and then an 
# essay on "Functions, modules, packages and libraries" recommended by Ian McLoughlin at: 
# https://nbviewer.jupyter.org/github/ianmcloughlin/python-fundamentals-notes/blob/master/functions-modules.ipynb#

import numpy as np
import matplotlib.pyplot as plt
    # importing the numpy & matplot libraries to help manipulate the data, and giving them shorthand names

data = np.genfromtxt('Data/Iris.csv', delimiter=',')
    # importing the iris dataset, as a csv file (syntax found on stack overflow)
col1 = (data[:,0]) 
    # select the first column of the dataset
col1mean = (np.mean(data[:,0]))
    # find the mean of the values in Column 1 (per method from Ian's video 'Numpy')
print("Column 1 mean is:",'{:0.3f}'.format(col1mean))
    # display the Column 1 mean to 3 decimal places (my preference)
