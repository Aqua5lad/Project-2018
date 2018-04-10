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
col1mean = (np.mean(data[:,0]))
    # find the mean of the values in Column 1 (per method from Ian's video 'Numpy')
col2mean = (np.mean(data[:,1]))  
col3mean = (np.mean(data[:,2]))
col4mean = (np.mean(data[:,3]))   
    # likewise for the other 3 data columns
print("Column 1 mean is:",'{:0.3f}'.format(col1mean))
    # display the Column 1 mean to 3 decimal places (my preference)
print("Column 2 mean is:",'{:0.3f}'.format(col2mean))
print("Column 3 mean is:",'{:0.3f}'.format(col3mean))
print("Column 4 mean is:",'{:0.3f}'.format(col4mean))    

col1max = (np.max(data[:,0]))
    # find the mean of the values in Column 1 (per method from Ian's video 'Numpy')
col2max = (np.max(data[:,1]))
col3max = (np.max(data[:,2]))
col4max = (np.max(data[:,3]))  
print("Column 1 max is:",'{:0.3f}'.format(col1max))
    # display the Column 1 max to 3 decimal places 
print("Column 2 max is:",'{:0.3f}'.format(col2max))
print("Column 3 max is:",'{:0.3f}'.format(col3max))
print("Column 4 max is:",'{:0.3f}'.format(col4max))

col1min = (np.min(data[:,0]))
col2min = (np.min(data[:,1]))
col3min = (np.min(data[:,2]))
col4min = (np.min(data[:,3]))  
print("Column 1 min is:",'{:0.3f}'.format(col1min))
    # display the Column 1 max to 3 decimal places 
print("Column 2 min is:",'{:0.3f}'.format(col2min))
print("Column 3 min is:",'{:0.3f}'.format(col3min))
print("Column 4 min is:",'{:0.3f}'.format(col4min))      

    # note to self - lookup 'compartmentalising code into functions'

col1std = (np.std(data[:,0]))
    # Std.Deviation - I guessed sd first, then found 'std' function on stack overflow
col2std = (np.std(data[:,1]))
col3std = (np.std(data[:,2]))
col4std = (np.std(data[:,3]))

print("Column 1 Std Dev is:",'{:0.3f}'.format(col1std))
print("Column 2 Std Dev is:",'{:0.3f}'.format(col2std))
print("Column 3 Std Dev is:",'{:0.3f}'.format(col3std))
print("Column 4 Std Dev is:",'{:0.3f}'.format(col4std))

    # Now lets split out the 3 varieties in the dataset
    # check that I can call a value from a specific cell:
    
print("the value at row 3, column 2 is:",data[2,1])

