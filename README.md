# Project-2018
## Purpose of this Repository
This repository is to manage the Spring Project 2018, which draws on the python programming skills covered in the 1st semester of the GMIT Higher Diploma in Data Analytics course.

## Subject of the Project
The subject matter of the project concerns the well-known Fisher’s Iris data set<sup>[1](http://archive.ics.uci.edu/ml/datasets/Iris)</sup>. Specifically, to research the data set, then write documentation and code in the Python programming language<sup>[2](https://www.python.org)</sup> based on that research.

Fisher's Iris data set is a multivariate data set<sup>[3](https://en.wikipedia.org/wiki/Multivariate_statistics)</sup> introduced by the British statistician and biologist Ronald Fisher in his 1936 paper "The use of multiple measurements in taxonomic problems"<sup>[4](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x)</sup> as an example of linear discriminant analysis<sup>[5](https://en.wikipedia.org/wiki/Linear_discriminant_analysis)</sup>. This data set recorded the species of each Iris (3 were identified), and the measurement of 4 variables on each flower. These variables were the sepal length, sepal width, petal length and petal width (in centimetres). It was performed on 50 flowers, from each of 3 species of Iris, resulting in a total of 750 observations.

## Project Plan / Approach
The plan was to begin by describing the problem in the README, then researching it via Google searches, to gain a clear view of the tasks required. All sources were tracked and saved for later reference in the README. The python code would be developed in parallel, step by step for each task, and tested before each commit. As each function was completed & tested, the results were added to the README. The next stage would be evaluating the results and considering what further analysis could be added, based on curiousity. Once those functions were coded and the results written up in the README, some overall conclusions could be summarised. Then the focus switched back to the coding, and whether it could be improved upon, based on the "DRY" principle. Where more efficient / generic functions could be developed & tested, they would be committed to the program. Finally, the README would be edited and completed, with reference to the project requirements and the marking scheme.  

## Researching the background to the data set
The Wikipedia entry <sup>[6](https://en.wikipedia.org/wiki/Iris_flower_data_set)</sup> notes that this data set became a typical test case for many statistical classification techniques in machine learning such as support vector machines, while its use in cluster analysis is less common. Wikipedia also notes that the data set is a good example to explain the difference between supervised and unsupervised techniques in data mining. Data mining is the process of discovering patterns in large data sets involving methods at the intersection of machine learning, statistics, and database systems.
  
Searching on the term 'Fisher Iris Data Set' returns a number of research studies, of which the following two are typical examples.

1) A Thesis on Machine learning algorithms by Yu Yang<sup>[7](https://www.theseus.fi/bitstream/handle/10024/64785/yang_yu.pdf?sequence=1&isAllowed=y)</sup> sets as an objective that "the computer should have the ability to aggregate three different classifications of Iris flower to three categories, The users do not need to tell the computer which class the Iris belongs to, the computer can recognize them all by itself."  The writer achieves this by using clustering methodologies so as to allow the program to identify which datapoint belongs in each variety, based on which cluster they fall into. The employment of 3D scatterplots gave a clear visual representation, allowing the clusters to be easily identified.

2) A Statistical Analysis of the Iris Flower Dataset by Patrick S. Hoey of University of Massachusetts At Lowell<sup>[8](http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf)</sup> plotted the dataset onto scatterplots to determine patterns in the data in relation to the Iris classifications. Secondly, it developed an application in Java that will run a series of methods on the dataset to extract relevant statistical information from the dataset. The employment of 2D scatterplots gave a visual representation which assists in identifying clusters.

## Investigation of the data set with data analysis

### Project Methodology
The data set follows a multi-variate structure, with columns 1 to 4 representing, respectively, sepal length, sepal width, petal length and petal width. The values for each of the three varieties are found at rows 1-50 (Setosa), 51-100 (Versicolor) and 101-150 (Virginica). 
The data set was investigated by creating a python program called NumpyData.py, in this repository, which, when executed, performs the following tasks: 

1. Loads the iris data set as a .csv file from within the Project-2018 repository
2. Loads the NumPy and Matplotlib python libraries to enable statistical analysis and graphical representations.
3. Analyses the data set to return the min, max and mean values of each variable, and it's standard deviation.
4. Further analyses the data for each varietal subset, as to the min, max and mean values of each variable.
5. Calculates the Standard Deviations for Petal Length on each of the 3 varieties.
6. Generates the graphics used in this README to illustrate some differences in data distributions, by variable, identifying any clusters.

### 1. Statistical analysis of the data set
The python program 'NumpyData' was written to analyse the data set and identify the maximum, minimum and mean values of the iris measurements, together with their standard deviations. The results of this analysis are shown in the following table.

####            Table 1 - Statistics for the entire Iris data set                
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

* (rounded to 3 decimals)   

### 3. Observations based on the statistical analysis of the data set, and its varietal subsets.

On reviewing the previous tables, one can make the following observations. The Virginica variety has the largest measurements, except for sepal width. The Setosa variety has the smallest measurements, except for sepal width, where it's largest. The Versicolor variety falls in between largest and smallest measurements on all characteristics except for sepal width, where it's smallest.

Indeed the ranking of the varieties by variable value, as noted in Table 5 (below), may suggest the nature of this variable (sepal width) differs from the other three insofar as the variety ranking, on this variable, diverges from that based on the other variables. 

####            Table 5 - Ranking of varieties, by variable value         
|              | sepal length | sepal width  | petal length | petal width
|------------- | -------------| -------------| -------------| -------------
|Maximum       |  Virginica   |   Setosa     |  Virginica   |  Virginica   
|Medium        |  Versicolor  |  Virginica   |  Versicolor  |  Versicolor    
|Minimum       |   Setosa     |  Versicolor  |   Setosa     |   Setosa  


On closer examination of table 1, it's noticeable that the data in column 2 (Sepal Width) showed the lowest Standard Deviation (0.432) from the mean, of all the variables. This infers a clustering of values around the mean. This is explored further by plotting a histogram of these Sepal Width values, using the [matplotlib](https://matplotlib.org/) program in python. While not quite a normal distribtion ("Bell Curve"), it does show (below, left) a concentration of observations in & around the mean of 3.054 cm. So the variation of sepal widths across the 150 flowers measured was not very pronounced.
  
 Sepal Width                            |            Petal Length                 |          
:--------------------------------------:|:----------------------------------------|
![Histogram 1](https://github.com/Aqua5lad/Project-2018/blob/master/Hist%20SW.png)| ![Histogram 2](https://github.com/Aqua5lad/Project-2018/blob/master/Hist%20PL.png)|  
  
In contrast to this, with a standard deviation of 1.759, the variable for petal length suggests a widely dispersed distribution, worthy of further investigation. So the petal lengths have also been plotted in a histogram, once again using the [matplotlib](https://matplotlib.org/) program in python. The result is shown in the second histogram (above right).

While the mean value for Petal length is 3.8cm, few observations were seen at this value. The distribution was mainly found in two distinct clusters, one between 1cm and 2.2cm, and the other between 4cm and 5.7cm. This unusual distribution merited further analysis, using the NumpyData program to plot the Petal Length values by Iris variety.

####  Distributions of Petal Length, by Iris Variety

   Setosa                               |            Versicolor                 |                Virginica              |
:--------------------------------------:|:-------------------------------------:|:---------------------------------------
![](https://github.com/Aqua5lad/Project-2018/blob/master/PL%20Setosa.png)| ![](https://github.com/Aqua5lad/Project-2018/blob/master/PL%20Vers.png)                |  ![](https://github.com/Aqua5lad/Project-2018/blob/master/PL%20Virg.png)             |

This analysis reveals a significant difference in distribution between Setosa petal lengths, with a normal distribution clustered around the mean of 1.465 and a low standard deviation of just 0.173, and the far more scattered distributions of petal lengths in the Versicolor and Virginica varieties. This is illustrated in the Histograms above, together with the statistics in table 6, below.

####          Table 6 - Statistics for Petal Length, by Iris Variety             
|              |    Setosa    |  Versicolor  |   Virginica  
|------------- | -------------| -------------| -------------
|Maximum (cm)  |     1.9      |      5.1     |     6.9           
|Minimum (cm)  |     1.0      |      3.0     |     4.5            
|Mean    (cm)* |     1.465    |      4.263   |     5.561           
|Std.Deviation*|     0.173    |      0.469   |     0.548    










## Summary of Investigations

The analysis of the data set yielded the following observations:
  1. Petal Length is the variable with the most widely dispersed values, i.e. greatest deviation from the mean.
  2. Sepal Width is the variable with the least widely dispersed values, i.e. lowest deviation from the mean.
  3. By variety, Virginica has the largest measurements overall, except for sepal width. 
  4. Setosa has the smallest measurements overall, except for sepal width, where it's largest. 
  5. Versicolor falls between largest and smallest on all characteristics except for sepal width, where it's smallest.
  6. Petal Length, by Iris variety, showed a significant difference in distributions between Setosa (normal distribution) and the more scattered distributions in the Versicolor and Virginica varieties.
  
  
  
  
  














### Project References List :
1. http://archive.ics.uci.edu/ml/datasets/Iris

2. https://www.python.org

3. https://en.wikipedia.org/wiki/Multivariate_statistics

4. https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x

5. https://en.wikipedia.org/wiki/Linear_discriminant_analysis

6. https://en.wikipedia.org/wiki/Iris_flower_data_set

7. https://www.theseus.fi/bitstream/handle/10024/64785/yang_yu.pdf?sequence=1&isAllowed=y

8. http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf

### Sources of Inspiration for the coding of NumpyData.py

The initial source for methodolgy was this free tutorial: https://www.youtube.com/watch?v=Tq6rCWPdXoQ and then an essay on "Functions, modules, packages and libraries" recommended by Ian McLoughlin at: https://nbviewer.jupyter.org/github/ianmcloughlin/python-fundamentals-notes/blob/master/functions-modules.ipynb#

After creating functions for analysing the data, which were then used repeatedly, it became necessary to simplify the code with new 'generic' functions to make it more efficient. Particularly helpful in this regard was Ian's 'defining functions' video at: https://web.microsoftstream.com/video/72d3bbf9-e58d-4a19-8a2c-e784e3cb4db3

Matplotlib generated good graphics, but for best presentation, guidance on setting up labeling commands was found at: https://matplotlib.org/gallery/pyplots/pyplot_text.html#sphx-glr-gallery-pyplots-pyplot-text-py. Another useful reference (although the code used is R) was: http://www.lac.inpe.br/~rafael.santos/Docs/R/CAP386/IntroEDA-Iris.html

A method for laying out multiple Histograms, side-by-side, was found on Stack overflow:
https://stackoverflow.com/questions/24319505/how-can-one-display-images-side-by-side-in-a-github-readme-md






