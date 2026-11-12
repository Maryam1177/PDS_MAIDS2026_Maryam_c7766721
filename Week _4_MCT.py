import pandas as pd


d = {
"Name": ["Tom", "James", "Ricky", "Vin", "Steve"],
"Age": [25, 26, 25, 23, 30],
"Rating": [4.23, 3.24, 3.98, 2.56, 3.20]
}
df = pd.DataFrame(d)
print(df.mean(numeric_only=True))


import pandas as pd
#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
'Lee','Chanchal','Gasper','Naviya','Andres']),
'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
#Create a DataFrame
df = pd.DataFrame(d)
print ("Mean Values in the Distribution")
# Select only numeric columns for mean calculation
print(df.mean(numeric_only=True))
print ("*******************************")
print ("Median Values in the Distribution")
# Select only numeric columns for median calculation
print(df.median(numeric_only=True))


import pandas as pd
#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
'Lee','Chanchal','Gasper','Naviya','Andres']),
'Age':pd.Series([25,26,25,23,30,25,23,34,40,30,25,46])}
#Create a DataFrame
df = pd.DataFrame(d)
print(df.mode())


#Q 1 : I choose the median because it is the middle value,
# If there are a few old people in the group, they pull up the mean.
# So the mean is not reliable.
# The mode only shows the age of the age that appears most often,
# but it is not always in the middle, so it does not describe the whole group.



# Measuring Standard Deviation:
import pandas as pd
#Create a Dictionary of series
d ={'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
'Lee','Chanchal','Gasper','Naviya','Andres']),
'Age':pd.Series([25,26,25,23,30,25,23,34,40,30,25,46]),
'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,
4.10,3.65])}
#Create a DataFrame
df = pd.DataFrame(d)
# Calculate the standard deviation
print (df.std(numeric_only =True))



# Measuring Skewness :

import pandas as pd
#Create a Dictionary of series
d ={'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
'Lee','Chanchal','Gasper','Naviya','Andres']),
'Age':pd.Series([25,26,25,23,30,25,23,34,40,30,25,46]),
'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
#Create a DataFrame
df = pd.DataFrame(d)
print(df.skew(numeric_only=True))



# Impact of outliers on Mean , Median , And Skewness

import pandas as pd
import numpy as np
# 1. Create a moderately symmetric dataset (e.g., ages of a group)
np.random.seed(42) # for reproducibility
symmetric_data = np.random.normal(loc=30, scale=5, size=20).round(1)
# Ensure values are positive, relevant for 'age'
symmetric_data = symmetric_data[symmetric_data > 0]
df_symmetric = pd.DataFrame({'Value': symmetric_data})
print("Original Symmetric Dataset (first 5 rows):\n",
df_symmetric.head())
print("\n--- Initial Statistics ---")
print(f"Mean: {df_symmetric['Value'].mean():.2f}")
print(f"Median: {df_symmetric['Value'].median():.2f}")
print(f"Skewness: {df_symmetric['Value'].skew():.2f}")



# Introducing a High Outlier:

# 2. Add a high outlier
df_high_outlier = df_symmetric.copy()
df_high_outlier.loc[len(df_high_outlier)] = 100 # Add a very high value
print("Dataset with High Outlier (last 5 rows):\n",
df_high_outlier.tail())
print("\n--- Statistics with High Outlier ---")
print(f"Mean: {df_high_outlier['Value'].mean():.2f}")
print(f"Median: {df_high_outlier['Value'].median():.2f}")
print(f"Skewness: {df_high_outlier['Value'].skew():.2f}")
print("Explanation")
print ("The Mean increased significantly, pulled towards the high outlier.")
print("The Median changed much less, as it's only affected by its position.")
print("The Skewness became strongly positive (right-skewed), indicating the presence of a high value pulling the 'tail' to the right.")





