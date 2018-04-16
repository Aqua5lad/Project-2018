# Project-2018
## Purpose of this Repository
This repository is to manage the Spring Project 2018, which draws on the python programming skills covered in the 1st semester of the GMIT Higher Diploma in Data Analytics course.

## Subject of the Project
The subject matter of the project concerns the well-known [Fisher’s Iris data set](http://archive.ics.uci.edu/ml/datasets/Iris). Specifically, to research the data set, then write documentation and code in the [Python programming language](https://www.python.org) based on that research.

Fisher's Iris data set is a multivariate data set<sup>[1](https://en.wikipedia.org/wiki/Multivariate_statistics)</sup> introduced by the British statistician and biologist Ronald Fisher in his 1936 paper "The use of multiple measurements in taxonomic problems"<sup>[2](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x)</sup> as an example of linear discriminant analysis<sup>[3](https://en.wikipedia.org/wiki/Linear_discriminant_analysis)</sup>.

This data set recorded the species of each Iris (3 were identified), and the measurement of 4 variables on each flower. These variables were the sepal length, sepal width, petal length and petal width (in centimetres). It was performed on 50 flowers, from each of 3 species of Iris, resulting in a total of 750 observations.

## Investigation of the Problem

### Project Methodology
The dataset is investigated by creating a python program called NumpyData.py which will do the following: 

1. Load the iris dataset as a .csv file from within the Project-2018 repository
2. Load the NumPy and Matplotlib python libraries to enable statistical analysis and graphical representations.
3. Analyse the dataset to find the min, max and mean values of each variable
4. Further analyse the data for each variety subset, as to the min, max and mean values of each variable
5. generate graphics to illustrate some differences in data distributions, by variable.


### 1. Statistical analysis of the dataset
The python program 'NumpyData' was written to analyse the dataset and identify the maximum, minimum and mean values of the iris measurements, together with their standard deviations. The results of this analysis are shown in the following table.

####            Table 1 - Statistics for the entire Iris dataset                
|              | sepal length | sepal width  | petal length | petal width
|------------- | -------------| -------------| -------------| -------------
|Maximum (cm)  |     7.9      |      4.4     |     6.9      |      2.5    
|Minimum (cm)  |     4.3      |      2.0     |     1.0      |      0.1   
|Mean    (cm)* |     5.843    |      3.054   |     3.759    |      1.199    
|Std.Deviation*|     0.825    |      0.432   |     1.759    |      0.761

### 2. Statistical analysis of the data subsets for each variety

A similar statistical analysis, by Iris variety, was carried out, using the NumpyData program. The results of this analysis are shown in the following three tables.

#### Table 2 - Statistics for the Iris-Setosa subset
|              | sepal length | sepal width  | petal length | petal width
|------------- | -------------| -------------| -------------| -------------
|Maximum (cm)  |     5.8      |      4.4     |     1.9      |      0.6    
|Minimum (cm)  |     4.3      |      2.3     |     1.0      |      0.1   
|Mean    (cm)* |     5.006    |      3.420   |     1.465    |      0.245    
  

#### Table 3 - Statistics for the Iris-Versicolor subset
|              | sepal length | sepal width  | petal length | petal width
|------------- | -------------| -------------| -------------| -------------
|Maximum (cm)  |     7.0      |      3.4     |     5.1      |      1.8  
|Minimum (cm)  |     4.9      |      2.0     |     3.0      |      1.0   
|Mean    (cm)* |     5.941    |      2.769   |     4.263    |      1.327
  

#### Table 4 - Statistics for the Iris-Virginica subset
|              | sepal length | sepal width  | petal length | petal width
|------------- | -------------| -------------| -------------| -------------
|Maximum (cm)  |     7.9      |      3.8     |     6.9      |      2.5    
|Minimum (cm)  |     4.9      |      2.2     |     4.5      |      1.4  
|Mean    (cm)* |     6.602    |      2.973   |     5.561    |      2.031   

* all rounded to 3 decimals   

### 3. Some Observations based on the statistical analysis of the dataset, and its varietal subsets.

On reviewing the previous tables, we can make the following observations. The Virginica variety has the largest measurements, except for sepal width. The Setosa variety has the smallest measurements, except for sepal width, where it's largest. The Versicolor variety falls in between largest and smallest measurements on all characteristics except for sepal width, where it's smallest.

Indeed the ranking of the varieties by variable value, as noted in Table 5 (below), may suggest the nature of this variable (sepal width) differs from the other three insofar as the variety ranking, on this variable, diverges from that based on the other variables. 

####            Table 5 - Ranking of varieties, by variable value         
|              | sepal length | sepal width  | petal length | petal width
|------------- | -------------| -------------| -------------| -------------
|Maximum       |  Virginica   |   Setosa     |  Virginica   |  Virginica   
|Medium        |  Versicolor  |  Virginica   |  Versicolor  |  Versicolor    
|Minimum       |   Setosa     |  Versicolor  |   Setosa     |   Setosa  


On closer examination of table 1, it's noticeable that the data in column 2 (Sepal Width) showed the lowest Standard Deviation (0.432) from the mean, of all the variables. This infers a clustering of values around the mean. This is explored further by plotting a histogram of these Sepal Width values, using the [matplotlib](https://matplotlib.org/) program in python. The result is as follows:
  
![Histogram 1](https://github.com/Aqua5lad/Project-2018/blob/master/Hist%20SW.png)

While not quite a normal distribtion ("Bell Curve"), it does show a concentration of observations in & around the mean of 3.054 cm. So the variation of sepal widths across the 150 flowers measured was not very pronounced.

In contrast to this, with a standard deviation of 1.759, the variable for petal length suggests a widely dispersed distribution, worthy of further investigation. So the petal lengths have been plotted in a histogram, once again using the [matplotlib](https://matplotlib.org/) program in python. The result is as follows:

![Histogram 2](https://github.com/Aqua5lad/Project-2018/blob/master/Hist%20PL.png)

While the mean value for Petal length is 3.8cm, few observations were seen at or near this value. The distribution was mainly found in two distinct clusters, one between 1cm and 2.2cm, and the other between 4cm and 5.7cm. This unusual distribution merited further a  investigation, using the NumpyData program to plot the Petal Length values by Iris variety.

####  Distributions of Petal Length, by Iris Variety

   Setosa                               |            Versicolor                 |                Virginica                |
:--------------------------------------:|:-------------------------------------:|:---------------------------------------:|:
![](https://github.com/Aqua5lad/Project-2018/blob/master/PL%20Virg.png)| ![](https://github.com/Aqua5lad/Project-2018/blob/master/PL%20Versi.png)                |  ![](https://github.com/Aqua5lad/Project-2018/blob/master/PL%20Virg.png)             |


























### Project References List :

1: https://en.wikipedia.org/wiki/Multivariate_statistics

2: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x

3: https://en.wikipedia.org/wiki/Linear_discriminant_analysis

