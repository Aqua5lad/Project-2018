# by Colm Doherty, started on 2018-4-4. Scripting statistical analysis for Project-2018 
# to figure out how to manipulate the dataset to discover max, min and mean 
# values in each column, and more if possible. Initial source for methodolgy was a
# free tutorial at https://www.youtube.com/watch?v=Tq6rCWPdXoQ and then an 
# essay on "Functions, modules, packages and libraries" recommended by Ian McLoughlin at: 
# https://nbviewer.jupyter.org/github/ianmcloughlin/python-fundamentals-notes/blob/master/functions-modules.ipynb#

import numpy as np
import matplotlib.pyplot as plt
    # importing the numpy & matplot libraries to help manipulate the data, and giving them shorthand names
    # Alternately I could import these into iPython while testing. Remember I'm working on a multivariate dataset
data = np.genfromtxt('Data/Iris.csv', delimiter=',')
    # importing the iris dataset, as a csv file (syntax found on stack overflow)
col1 = (data[:,0])    
col2 = (data[:,1])  
col3 = (data[:,2])  
col4 = (data[:,3])  
    # name the columns, so I can call them later if required e.g. for histogram plots

    #NEW FUNCTION for column mean (prototyped in my FuncTest.py):
def colmean(colno):
    meancol = (np.mean(data[:,colno]))
    return meancol    

print("Column 1 mean is:",'{:0.3f}'.format(colmean(0)))
print("Column 2 mean is:",'{:0.3f}'.format(colmean(1)))
print("Column 3 mean is:",'{:0.3f}'.format(colmean(2)))
print("Column 4 mean is:",'{:0.3f}'.format(colmean(3)))

    # YAY! took >2hrs of trial & error to get right, w/help from Ian's "Defining functions" video 

    # NEW FUNCTIONS for column max, min, std dev:
def colmax(colno):
    maxcol = (np.max(data[:,colno]))
    return maxcol    

print("Column 1 max is:",'{:0.1f}'.format(colmax(0)))
print("Column 2 max is:",'{:0.1f}'.format(colmax(1)))
print("Column 3 max is:",'{:0.1f}'.format(colmax(2)))
print("Column 4 max is:",'{:0.1f}'.format(colmax(3)))

def colmin(colno):
    mincol = (np.min(data[:,colno]))
    return mincol    

print("Column 1 min is:",'{:0.1f}'.format(colmin(0)))
print("Column 2 min is:",'{:0.1f}'.format(colmin(1)))
print("Column 3 min is:",'{:0.1f}'.format(colmin(2)))
print("Column 4 min is:",'{:0.1f}'.format(colmin(3)))   

def colstd(colno):
    stdcol = (np.std(data[:,colno]))
    return stdcol    

print("Column 1 std dev is:",'{:0.3f}'.format(colstd(0)))
print("Column 2 std dev is:",'{:0.3f}'.format(colstd(1)))
print("Column 3 std dev is:",'{:0.3f}'.format(colstd(2)))
print("Column 4 std dev is:",'{:0.3f}'.format(colstd(3)))
   
    # Now lets split out the 3 varieties in the dataset, for closer analysis ...

print("the value at row 3, column 2 is:",data[2,1])
    # checking that I can call a value from a specific cell. Syntax is row,column

    # now I want to call a range of rows in each column ...
    # NEW CODE HERE - created a generic function:

def colmeanS(colno):
    meancolS = (np.mean(data[0:49,colno]))
    return meancolS

print("(C1) Setosa S.L. mean is:",'{:0.3f}'.format(colmeanS(0)))
print("(C2) Setosa S.W. mean is:",'{:0.3f}'.format(colmeanS(1)))
print("(C3) Setosa P.L. mean is:",'{:0.3f}'.format(colmeanS(2)))
print("(C4) Setosa P.W. mean is:",'{:0.3f}'.format(colmeanS(3)))

    # displays the mean for each Column in the Setosa sample     

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

col1Virgmean = (np.mean(data[100:149,0]))
print("Column 1 Virginica mean is:",'{:0.3f}'.format(col1Virgmean))
col2Virgmean = (np.mean(data[100:149,1]))
col3Virgmean = (np.mean(data[100:149,2]))
col4Virgmean = (np.mean(data[100:149,3]))
print("Column 2 Virginica mean is:",'{:0.3f}'.format(col2Virgmean))
print("Column 3 Virginica mean is:",'{:0.3f}'.format(col3Virgmean))
print("Column 4 Virginica mean is:",'{:0.3f}'.format(col4Virgmean))

col1Virgmax = (np.max(data[100:149,0]))
print("Column 1 Virginica max is:",'{:0.3f}'.format(col1Virgmax))
col2Virgmax = (np.max(data[100:149,1]))
col3Virgmax = (np.max(data[100:149,2]))
col4Virgmax = (np.max(data[100:149,3]))
print("Column 2 Virginica max is:",'{:0.3f}'.format(col2Virgmax))
print("Column 3 Virginica max is:",'{:0.3f}'.format(col3Virgmax))
print("Column 4 Virginica max is:",'{:0.3f}'.format(col4Virgmax))

col1Virgmin = (np.min(data[100:149,0]))
print("Column 1 Virginica min is:",'{:0.3f}'.format(col1Virgmin))
col2Virgmin = (np.min(data[100:149,1]))
col3Virgmin = (np.min(data[100:149,2]))
col4Virgmin = (np.min(data[100:149,3]))
print("Column 2 Virginica min is:",'{:0.3f}'.format(col2Virgmin))
print("Column 3 Virginica min is:",'{:0.3f}'.format(col3Virgmin))
print("Column 4 Virginica min is:",'{:0.3f}'.format(col4Virgmin))

# Std Deviations for Petal Length on 3 varieties(column3):
col3Setstd = (np.std(data[0:49,2]))
print("Petal Length Setosa std is:",'{:0.3f}'.format(col3Setstd))
col3Varstd = (np.std(data[50:99,2]))
print("Petal Length Versicolor std is:",'{:0.3f}'.format(col3Varstd))
col3Virgstd = (np.std(data[100:149,2]))
print("Petal Length Virginica std is:",'{:0.3f}'.format(col3Virgstd))


# Selecting data to plt Histograms:
plt.hist(col2)
plt.title('Histogram of Sepal Widths')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

plt.hist(col3)
plt.title('Histogram of Petal Lengths')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# learnt labeling cmds at https://matplotlib.org/gallery/pyplots/pyplot_text.html#sphx-glr-gallery-pyplots-pyplot-text-py
# also useful ref (though code used is R): http://www.lac.inpe.br/~rafael.santos/Docs/R/CAP386/IntroEDA-Iris.html

# Add the remaining two variables to plt Histograms:
plt.hist(col1)
plt.title('Histogram of Sepal Lengths')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

plt.hist(col4)
plt.title('Histogram of Petal Widths')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')
plt.show()

# now to plot the Petal Lengths by Variety:
col31 = (data[0:49,2]) 
col32 = (data[50:99,2])
col33 = (data[100:149,2])

plt.hist(col31)
plt.title('Petal Lengths of Setosa variety')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

plt.hist(col32)
plt.title('Petal Lengths of Versicolor variety')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

plt.hist(col33)
plt.title('Petal Lengths of Virginica variety')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# method for Histogram 3-way layout found on Stack overflow:
# https://stackoverflow.com/questions/24319505/how-can-one-display-images-side-by-side-in-a-github-readme-md




# Listen. Strange women lying in ponds distributing swords is no basis for a system of government.
