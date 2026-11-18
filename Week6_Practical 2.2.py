import pandas as pd

#Task 1:
try:
    df = pd.read_csv("missing_file.csv")
except FileNotFoundError:
    print("File does not exist.")

try:
    df = pd.read_csv("data.csv")
except Exception as e:
    print("Something went wrong:", e)


# Task 2:
import os
print(os.getcwd())
# os.chdir("new_folder")
print(os.getcwd())


from pathlib import Path
import pandas as pd
file_path = Path("data") / "data.csv"
df = pd.read_csv(file_path)
print(df)

# Task 3:

df = pd.read_csv("data.csv")
print(df.shape)
print(df.info())
print(df.isna().sum())
print(df.dtypes)

# Task 4:

import json
data = {
"user": {
"name": "Alice",
"scores": [80, 90, 85]
}
}
print(pd.json_normalize(data))


# Task 5 :
import os
import pandas as pd
sample_data_path = "data"
files = [os.path.join(sample_data_path, f) for f in os.listdir(sample_data_path) if
f.endswith(".csv")]
dfs = [pd.read_csv(file) for file in files]
# Check if the dfs list is not empty before attempting to concatenate
if dfs:
    combined = pd.concat(dfs)
    print(combined)
else:
    print("No CSV files found in the directory to concatenate.")