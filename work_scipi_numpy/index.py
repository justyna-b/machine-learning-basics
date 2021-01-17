import pandas as pd 
import numpy as np
from scipy import linalg, sparse
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import neighbors, datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import Imputer
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.io import output_notebook, show
from bokeh.models import HoverTool
from bokeh.models import CategoricalColorMapper
from bokeh.layouts import row
from bokeh.io import output_file, show, save


# CHEAT SHEET PYTHON BASIS

# set new list 
slice_a = 'guess'
slice_c = 'will'
my_list = [slice_a, 'what', slice_c, 'happened']
my_list2 = [[4,5,6,7], [3,4,5,6]]

#list concatenation
my_list3 = my_list + my_list2
print(my_list3)

#replace in string letter with  given char
print(slice_a.replace('y' , '!!!'))

#get dimensions of an array. Parse list into array (list has no attribute shape)
print(np.array(my_list2).shape)

#count in list given string
print(my_list.count('what'))
#add an item to list
my_list.append('????')
print(my_list)
#remove an item from list
my_list.remove('????')
print(my_list)


# CHEAT SHEET NUMPY BASIS

a = np.array([1,2,3])
b =  np.array([(1.5,2,3), (4,5,6)], dtype = float)
c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]], dtype = float)

#substraction of two arrays
g = a - b   
print(g)
#create copy of array
h = a.copy()
print(h)
#print cumulation od numbers
print(b.cumsum(axis=0))
#print the maximum in rows
print(b.max(axis=0))
#reshape array but with the same data
i = g.reshape(3,-2) 
print(i)


# CHEAT SHEET SCIPY - LINEAR ALGEBRA

A = np.matrix(np.random.random((2,2)))
B = np.matrix(np.random.random((2,2)))
#print multiplication of values from array A with B
print(np.multiply(A,B))
#print transposition of A array
print(A.T)
#set matrice withh dimensions of 3x3 and set 1 in the diagonal. Parameter k set how many of them may occure
C = np.eye(3, k=0)
print(C)
#count sin value in matrice B
print(linalg.sinhm(B))
#count sqrt value of each value in matrice A
print(linalg.sqrtm(A))


# CHEAT SHEET PANDAS BASICS

s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
data = {'Country': ['Belgium', 'India', 'Brazil'], 'Capital': ['Brussels', 'New Delhi', 'Brasília'],'Population': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])

#print value of element with 'b' label
print(s['b'])
#print all values from dataframe from value with index 1
print(df[1:])
#sum value from dataframe
print(df.sum())
#print max value from dataframe
print(df.max())
#print min value from dataframe 
print(df.min())
#print statistics from dataframe for ex. mean value etc
print(df.describe())



# CHEAT SHEET SCIKIT-LEARN

X = np.random.random((10,5))
y = np.array(['M','M','F','F','M','F','M','M','F','F','F'])
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
#set model of k-means alogirthm with 3 centres
k_means = KMeans(n_clusters=3, random_state=0)
#fit given model to the set data
lr = lr.fit(X, y)
#predict labels
y_pred =svc.predict(np.random.random((2,5)))
y_pred = lr.predict(X_test)
y_pred = knn.predict_proba(X_test)
#impute missing values
imp = Imputer(missing_values=0, strategy='mean', axis=0)
imp.fit_transform(X_train)


# CHEAT SHEET MATPLOTLIB
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.cos(x)
z = np.sin(x)
plot_figure = plt.figure()
#add axis into existing plot
axes = plot_figure.add_subplot(111)
axes.plot(x, y)
#set points in coordinate system
axes.scatter([1, 2, 3], [4, 5, 6], marker='*')
plt.title('Example')
#save plot into the given file in current directory
plt.savefig('plot.png')
#show the given before plot
plt.show()



#CHEAT SHEET SEABORN
titanic = sns.load_dataset("titanic")
sns.set_style('ticks')
#firstly count the observations and show them on the plot
sns.countplot(x="deck", data=titanic)
plt.show()
#plot estimates points with scatterplot glyphs (punktowe znaki)
sns.barplot(x="sex", y="survived", hue="class", data=titanic)
plt.show()
#plot estimates points with rectangular bars
sns.pointplot(
    x="class",
    y="survived",
    hue="sex",
    data=titanic,
    palette={ "male": "g",
              "female": "m"},
    markers=["^", "o"],
    linestyles=["-", "--"]
)
plt.show()
sns.violinplot(x="age", y="sex", hue="survived", data=titanic)
plt.show()
sns.boxplot(x="alive", y="age", hue="adult_male", data=titanic)
plt.show()

#CHEAT SHEET BOKEH

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
#set figure with example dataset
p = figure(title="Example", x_axis_label='x', y_axis_label='y')
p.line(x, y, legend_label="Example", line_width=4)
#set file where later save an output
output_file("index.html")
plot_1 = figure(plot_width=300, tools='pan,box_zoom')
plot_2 = figure(plot_width=300, plot_height=300, x_range=(0, 8), y_range=(0, 8))
plot_1.legend.background_fill_color = "pink"
#create circle plot for given values
plot_1.circle(np.array([1, 2, 3]), np.array([3, 2, 1]), fill_color='cyan')
plot_1.line([1, 2, 3, 4, 1], [5, 6, 7, 8, 9], line_width=4)
#save plot into given above file
save(plot_1)