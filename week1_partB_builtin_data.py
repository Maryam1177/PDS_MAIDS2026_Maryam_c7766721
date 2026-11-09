import pandas as pd
import seaborn as sns

iris = sns.load_dataset("iris")
print(iris.head())

#one row represents one iris flower
#one column represents one attribute of the flower


print(iris.shape)
# The dataset has 150 rows and 5 columns

print(iris.columns)
print(iris.dtypes)
print(iris.info())
#Four columns are numbers. The species column is words.


print(iris.iloc[0])
print(iris.iloc[10:20])
print(iris[['sepal_length','petal_length']])


print(iris[iris["species"] == "setosa"])
print(iris[iris['sepal_length']> 5])
print(iris[(iris["species"] == "setosa")&(iris["sepal_length"]> 5)])


print(iris.isna().sum())
 #In real life some data might be missing so this can make our answers wrong so we always must check.


#First we must understand the data then we can find the answer.
#Selecting means choosing rows by their number while filtering means choosing rows by a rule.
#How many rows and columns are there? what does each column mean? is any data missing?