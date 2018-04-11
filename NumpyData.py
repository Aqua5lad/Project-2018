# by Colm Doherty, started on 2018-4-4. Scripting statistical analysis for Project-2018 
# to figure out how to manipulate the dataset to discover max, min and mean 
# values in each column, and more if possible. Initial source for methodolgy was a
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

    # NB - lookup 'compartmentalising code into functions'

col1std = (np.std(data[:,0]))
    # Std.Deviation - I guessed sd first, then found 'std' function on stack overflow
col2std = (np.std(data[:,1]))
col3std = (np.std(data[:,2]))
col4std = (np.std(data[:,3]))

print("Column 1 Std Dev is:",'{:0.3f}'.format(col1std))
print("Column 2 Std Dev is:",'{:0.3f}'.format(col2std))
print("Column 3 Std Dev is:",'{:0.3f}'.format(col3std))
print("Column 4 Std Dev is:",'{:0.3f}'.format(col4std))
   
    # Now lets split out the 3 varieties in the dataset, for closer analysis ...

print("the value at row 3, column 2 is:",data[2,1])
    # checking that I can call a value from a specific cell. Syntax is row,column

    # now I want to call a range of rows in each column ...
col1Setomean = (np.mean(data[0:49,0]))
print("Column 1 Setosa mean is:",'{:0.3f}'.format(col1Setomean))
    # figured this out with help from http://cs231n.github.io/python-numpy-tutorial/#numpy-arrays
col2Setomean = (np.mean(data[0:49,1]))
col3Setomean = (np.mean(data[0:49,2]))
col4Setomean = (np.mean(data[0:49,3]))

print("Column 2 Setosa mean is:",'{:0.3f}'.format(col2Setomean))
print("Column 3 Setosa mean is:",'{:0.3f}'.format(col3Setomean))
print("Column 4 Setosa mean is:",'{:0.3f}'.format(col4Setomean))
    # display the mean for each Column in the Setosa sample

        # NB: - all calculated results are being ROUNDED.

col1Setomax = (np.max(data[0:49,0]))
print("Column 1 Setosa max is:",'{:0.3f}'.format(col1Setomax))
col2Setomax = (np.max(data[0:49,1]))
col3Setomax = (np.max(data[0:49,2]))
col4Setomax = (np.max(data[0:49,3]))

print("Column 2 Setosa max is:",'{:0.3f}'.format(col2Setomax))
print("Column 3 Setosa max is:",'{:0.3f}'.format(col3Setomax))
print("Column 4 Setosa max is:",'{:0.3f}'.format(col4Setomax))
    # display the max for each Column in the Setosa sample

col1Setomin = (np.min(data[0:49,0]))
print("Column 1 Setosa min is:",'{:0.3f}'.format(col1Setomin))
col2Setomin = (np.min(data[0:49,1]))
col3Setomin = (np.min(data[0:49,2]))
col4Setomin = (np.min(data[0:49,3]))

print("Column 2 Setosa min is:",'{:0.3f}'.format(col2Setomin))
print("Column 3 Setosa min is:",'{:0.3f}'.format(col3Setomin))
print("Column 4 Setosa min is:",'{:0.3f}'.format(col4Setomin))
    # display the min for each Column in the Setosa sample    
    
col1Setostd = (np.std(data[0:49,0]))
col2Setostd = (np.std(data[0:49,1]))
col3Setostd = (np.std(data[0:49,2]))
col4Setostd = (np.std(data[0:49,3]))

print("Column 1 Std Dev is:",'{:0.3f}'.format(col1std))
print("Column 2 Std Dev is:",'{:0.3f}'.format(col2std))
print("Column 3 Std Dev is:",'{:0.3f}'.format(col3std))
print("Column 4 Std Dev is:",'{:0.3f}'.format(col4std))    
     # display the Std Deviation for each Column in the Setosa sample   

    # NB: - these results are identical to the whole dataset. ! hmmm??

col1Versimean = (np.mean(data[50:99,0]))
print("Column 1 Versicolor mean is:",'{:0.3f}'.format(col1Versimean))
col2Versimean = (np.mean(data[50:99,1]))
col3Versimean = (np.mean(data[50:99,2]))
col4Versimean = (np.mean(data[50:99,3]))

print("Column 2 Versicolor mean is:",'{:0.3f}'.format(col2Versimean))
print("Column 3 Versicolor mean is:",'{:0.3f}'.format(col3Versimean))
print("Column 4 Versicolor mean is:",'{:0.3f}'.format(col4Versimean))

col1Versimax = (np.max(data[50:99,0]))
print("Column 1 Versicolor max is:",'{:0.3f}'.format(col1Versimax))
col2Versimax = (np.max(data[50:99,1]))
col3Versimax = (np.max(data[50:99,2]))
col4Versimax = (np.max(data[50:99,3]))
print("Column 2 Versicolor max is:",'{:0.3f}'.format(col2Versimax))
print("Column 3 Versicolor max is:",'{:0.3f}'.format(col3Versimax))
print("Column 4 Versicolor max is:",'{:0.3f}'.format(col4Versimax))

col1Versimin = (np.min(data[50:99,0]))
col2Versimin = (np.min(data[50:99,1]))
col3Versimin = (np.min(data[50:99,2]))
col4Versimin = (np.min(data[50:99,3]))
print("Column 1 Versicolor min is:",'{:0.3f}'.format(col1Versimin))
print("Column 2 Versicolor min is:",'{:0.3f}'.format(col2Versimin))
print("Column 3 Versicolor min is:",'{:0.3f}'.format(col3Versimin))
print("Column 4 Versicolor min is:",'{:0.3f}'.format(col4Versimin))


    


