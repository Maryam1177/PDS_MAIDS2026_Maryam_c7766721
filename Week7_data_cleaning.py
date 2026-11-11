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
