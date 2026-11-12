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



# Introducing a Low Outlier

# 3. Add a low outlier (reverting to original symmetric data first)
df_low_outlier = df_symmetric.copy()
df_low_outlier.loc[len(df_low_outlier)] = 5 # Add a very low value
print("Dataset with Low Outlier (last 5 rows):\n",
df_low_outlier.tail())
print("\n--- Statistics with Low Outlier ---")
print(f"Mean: {df_low_outlier['Value'].mean():.2f}")
print(f"Median: {df_low_outlier['Value'].median():.2f}")
print(f"Skewness: {df_low_outlier['Value'].skew():.2f}")
print("Explanation")
print("The Mean decreased, pulled towards the low outlier.")
print("The Median again changed relatively little.")
print("The Skewness became negative (left-skewed), indicating the presence of alow value pulling the 'tail' to the left.")



#Q2: Describe how each measure changed and explain
#why skewness is particularly sensitive to outliers ?
# Mean went up with high outlier (from 29.14 to 32.51)
# Mean went down with the low outlier (to 27.99)
# Median stayed the same (28.80) in both cases.
#Skewness went from 0.02 to 3.96 with the high outlier ( right skewed)
#and to -1.67 with the low outlier ( left skewed).
#Skewness is sensitive because it measures how far values are from the mean.
# one outlier is very far away so it creates a long tail on one side.


# Python_ Normal Distribution :

import matplotlib.pyplot as plt
import numpy as np
mu, sigma = 0.5, 0.1
s = np.random.normal(mu, sigma, 1000)
# Create the bins and histogram
count, bins, ignored = plt.hist(s, 20, density=True)
# Plot the distribution curve
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=3,color='y')
plt.show()


import matplotlib.pyplot as plt
import numpy as np
def plot_normal_distribution(mu, sigma, num_samples=1000, bins=30, color='skyblue', label='Generated Data'):
    # Generate random samples from a normal distribution
    s = np.random.normal(mu, sigma, num_samples)
    # Create the histogram
    count, bins, ignored = plt.hist(s, bins=bins, density=True,
    color=color, alpha=0.6, label=label)
    # Plot the theoretical probability distribution curve
    # Use the 'bins' from the histogram to define the x-axis for the curve
    x = np.linspace(min(bins), max(bins), 100)
    pdf = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 /
    (2 * sigma**2) )
    plt.plot(x, pdf, linewidth=2, color='red', label=f'PDF (mu={mu}, sigma={sigma})')
    plt.title(f'Normal Distribution: mu={mu}, sigma={sigma}')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True)
# --- Task Part 1: Generate and Visualize Multiple Normal Distributions ---
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plot_normal_distribution(mu=0, sigma=1, color='lightgreen',
label='Dist 1 Data')
plt.subplot(1, 3, 2)
plot_normal_distribution(mu=5, sigma=0.5, color='salmon',
label='Dist 2 Data')
plt.subplot(1, 3, 3)
plot_normal_distribution(mu=-2, sigma=2, color='lightblue',
label='Dist 3 Data')
plt.tight_layout()
plt.show()
# --- Task Part 2: Analysis and Discussion (Students to add their text/markdown cells) ---
# --- Task Part 3: Challenge (Optional) ---
# Students can add more code cells here to demonstrate a skewed distribution


# Analysis and Discussion:
# Changing mu changes the centre of the curve, so the curve moves left or right.
# Changing sigma changes the width of the curve.
# A small sigma makes it thin and tall and a big sigma makes it wide and flat.

# Homework Task 1:
# 1.Adult height, most people are close to the average height,
# and very few are very short or very tll so it follows  a normal distribution.
# 2. Baby birth weight , most babies are close to the average weight ,
# and very few are very light or very heavy so it follows the normal distribution.


# Homework Task 2:




