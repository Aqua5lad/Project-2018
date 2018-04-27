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

    #NEW FUNCTION for column mean (prototyped in my FuncTest.py in the CDs-Sample-Python-Code repository):
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
    # NEW generic functions for Mean, Max, Min of each Variety:

def colmeanS(colno):
    meancolS = (np.mean(data[0:49,colno]))
    return meancolS

print("(C1) Setosa S.L. mean is:",'{:0.3f}'.format(colmeanS(0)))
print("(C2) Setosa S.W. mean is:",'{:0.3f}'.format(colmeanS(1)))
print("(C3) Setosa P.L. mean is:",'{:0.3f}'.format(colmeanS(2)))
print("(C4) Setosa P.W. mean is:",'{:0.3f}'.format(colmeanS(3)))
    # displays the mean for each Column in the Setosa sample     

def colmaxS(colno):
    maxcolS = (np.max(data[0:49,colno]))
    return maxcolS

print("(C1) Setosa S.L. max is:",'{:0.3f}'.format(colmaxS(0)))
print("(C2) Setosa S.W. max is:",'{:0.3f}'.format(colmaxS(1)))
print("(C3) Setosa P.L. max is:",'{:0.3f}'.format(colmaxS(2)))
print("(C4) Setosa P.W. max is:",'{:0.3f}'.format(colmaxS(3)))   
    # displays the max for each Column in the Setosa sample
    
def colminS(colno):
    mincolS = (np.min(data[0:49,colno]))
    return mincolS

print("(C1) Setosa S.L. min is:",'{:0.3f}'.format(colminS(0)))
print("(C2) Setosa S.W. min is:",'{:0.3f}'.format(colminS(1)))
print("(C3) Setosa P.L. min is:",'{:0.3f}'.format(colminS(2)))
print("(C4) Setosa P.W. min is:",'{:0.3f}'.format(colminS(3)))      
  # displays the min for each Column in the Setosa sample  

def colmeanVr(colno):
    meancolVr = (np.mean(data[50:99,colno]))
    return meancolVr

print("(C1) Versicolor S.L. mean is:",'{:0.3f}'.format(colmeanVr(0)))
print("(C2) Versicolor S.W. mean is:",'{:0.3f}'.format(colmeanVr(1)))
print("(C3) Versicolor P.L. mean is:",'{:0.3f}'.format(colmeanVr(2)))
print("(C4) Versicolor P.W. mean is:",'{:0.3f}'.format(colmeanVr(3)))
    # displays the mean for each Column in the Versicolor sample     

def colmaxVr(colno):
    maxcolVr = (np.max(data[50:99,colno]))
    return maxcolVr

print("(C1) Versicolor S.L. max is:",'{:0.3f}'.format(colmaxVr(0)))
print("(C2) Versicolor S.W. max is:",'{:0.3f}'.format(colmaxVr(1)))
print("(C3) Versicolor P.L. max is:",'{:0.3f}'.format(colmaxVr(2)))
print("(C4) Versicolor P.W. max is:",'{:0.3f}'.format(colmaxVr(3)))
    # displays the max for each Column in the Versicolor sample        

def colminVr(colno):
    mincolVr = (np.min(data[50:99,colno]))
    return mincolVr

print("(C1) Versicolor S.L. min is:",'{:0.3f}'.format(colminVr(0)))
print("(C2) Versicolor S.W. min is:",'{:0.3f}'.format(colminVr(1)))
print("(C3) Versicolor P.L. min is:",'{:0.3f}'.format(colminVr(2)))
print("(C4) Versicolor P.W. min is:",'{:0.3f}'.format(colminVr(3)))
    # displays the min for each Column in the Versicolor sample     

def colmeanVg(colno):
    meancolVg = (np.mean(data[100:149,colno]))
    return meancolVg

print("(C1) Virginica S.L. mean is:",'{:0.3f}'.format(colmeanVg(0)))
print("(C2) Virginica S.W. mean is:",'{:0.3f}'.format(colmeanVg(1)))
print("(C3) Virginica P.L. mean is:",'{:0.3f}'.format(colmeanVg(2)))
print("(C4) Virginica P.W. mean is:",'{:0.3f}'.format(colmeanVg(3)))
    # displays the mean for each Column in the Virginica sample    

def colmaxVg(colno):
    maxcolVg = (np.max(data[100:149,colno]))
    return maxcolVg

print("(C1) Virginica S.L. max is:",'{:0.3f}'.format(colmaxVg(0)))
print("(C2) Virginica S.W. max is:",'{:0.3f}'.format(colmaxVg(1)))
print("(C3) Virginica P.L. max is:",'{:0.3f}'.format(colmaxVg(2)))
print("(C4) Virginica P.W. max is:",'{:0.3f}'.format(colmaxVg(3)))
    # displays the max for each Column in the Virginica sample   

def colminVg(colno):
    mincolVg = (np.min(data[100:149,colno]))
    return mincolVg

print("(C1) Virginica S.L. min is:",'{:0.3f}'.format(colminVg(0)))
print("(C2) Virginica S.W. min is:",'{:0.3f}'.format(colminVg(1)))
print("(C3) Virginica P.L. min is:",'{:0.3f}'.format(colminVg(2)))
print("(C4) Virginica P.W. min is:",'{:0.3f}'.format(colminVg(3)))
    # displays the min for each Column in the Virginica sample   

# Std Deviations for Petal Length on 3 varieties(column3):
col3Setstd = (np.std(data[0:49,2]))
print("Petal Length Setosa std is:",'{:0.3f}'.format(col3Setstd))
col3Varstd = (np.std(data[50:99,2]))
print("Petal Length Versicolor std is:",'{:0.3f}'.format(col3Varstd))
col3Virgstd = (np.std(data[100:149,2]))
print("Petal Length Virginica std is:",'{:0.3f}'.format(col3Virgstd))

# Selecting data to plot Histograms:
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

# Add the remaining two variables to plot Histograms:
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

#  FOOTNOTES
#  which data is found where?
#           	|   SL    |   SW    |   PL   |   PW   |
#	     	    -—————————————————————————————————————
#  Setosa	    | 	    	    0 - 49 			      |
#  Versicolor	|	           50 - 99		    	  |
#  Virginica	|	          100 - 149		          |
#	        	——————————————————————————————————————-



# Listen. Strange women lying in ponds distributing swords is no basis for a system of government.
