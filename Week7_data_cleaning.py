import pandas as pd
import numpy as np

# using list
product_data=[['e-book', 2000], ['plants', 6000], ['Pencil', 3000]]
#2d list, similar to 2d array
indexes=[1,2,3]
columns_name=['product', 'unit_sold']
product_df = pd.DataFrame(data=product_data, index=indexes,
columns=columns_name)
print(product_df)

# using dictionaries
product_data={'product': ['e-book', 'plants', 'Pencil'], 'unit_sold':
[2000, 5000, 3000]}
product_df = pd.DataFrame(data=product_data)
print(product_df)
<<<<<<< HEAD

# using numpy array
products = np.array([['','product','unit_sold'], [1, 'E-book',2000],
[2, 'Plants', 6000], [3, 'Pencil', 3000]])
product_pf = pd.DataFrame(data=products[1:,1:],index=products[1:,0 ],
columns=products[0,1:])
print(product_pf)
# output is same as of first case


df = pd.read_csv('data/dirtydata (2).csv')
print(df.head(10))

#Print information about the data:
print(df.info())
print(df.isna().sum())
print(df.duplicated())

import pandas as pd
df = pd.read_csv('data/data.csv')
new_df = df.dropna()
print(new_df.to_string())


import pandas as pd
df = pd.read_csv('data/dirtydata (2).csv')
df_new = df['Calories'].fillna(130)

print(df_new)



=======
>>>>>>> bdf48676d9e25590f223820fc992a86324cf7c96
