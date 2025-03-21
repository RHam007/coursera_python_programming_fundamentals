#Importing pandas
#import pandas as pd

# defining data set for the dataframe
"""
dataset1 = pd.read_csv("Iris.csv") #example data - file does not exist
dataset1

dataset2 = pd.read_csv("cars.csv")  #.read_csv("<file name>") loads the csv data into the 'dataset2' dataframe
dataset2.head()  # provides a dataframe with only the first few rows to show the values and columns
dataset2.info()  # returns the column name, a sum of the non-null field count, and the column's data type (Dtype)
dataset2.describe() # returns basic analysis dataframe for each numerical column's data (count, mean, std, min, 25%/50%/75%, and max)
"""
# Handling Duplicate Data (example)
"""
import pandas as pd

data = pd.read_csv('your_data.csv')

duplicates = data.duplicated()
print(duplicates)

duplicate_rows = data[data.duplicated()]
print(duplicate_rows)

data= data.drop_duplicates()"""

# Special handling of duplicates
"""
# Keep last instance of duplicated data
data = data.drop_duplicates(keep='last')

# Keep first instance of duplicated data (this is default)
data = data.drop_duplicates(keep='first')

# Remove all duplicated rows
data = data.drop_duplicates(keep=False)
"""

# EDA Example provided by MicroSoft via Coursera
"""
import pandas as pd
import numpy as np

# Sample DataFrame with missing values
data = {'Name': ['Alice', 'Bob', np.nan, 'David'], 
        'Age': [25, 30, np.nan, 35], 
        'City': ['New York', np.nan, 'London', 'Paris']}
df = pd.DataFrame(data)

# 1. Identifying missing values
print("Missing value counts per column:\n", df.isnull().sum())

# 2. Removing missing values (dropna)
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with any missing value:\n", df_dropped)

# 3. Imputing with mean (for numerical columns)
df_filled_mean = df.fillna(df.mean(numeric_only=True))
print("\nDataFrame after filling missing 'Age' with mean:\n", df_filled_mean)

# 3. Imputing with median (for numerical columns)
df_filled_median = df.fillna(df.median(numeric_only=True))
print("\nDataFrame after filling missing 'Age' with median:\n", df_filled_median)

# 4. Handling outliers (demonstration with 'Age')
# Assuming we identify 40 as an outlier based on domain knowledge or visualization
df['Age_capped'] = df['Age'].clip(upper=40)  # Cap values at 28
print("\nDataFrame with 'Age' capped at 40:\n", df)

# 5. Data type conversion
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # Convert to numeric, handling errors
print("\nData types after conversion:\n", df.dtypes)

# 6. Exploratory Data Analysis
print("\nDescriptive statistics:\n", df.describe())

# Group by and aggregate
grouped_data = df.groupby('City')['Age'].mean()
print("\nAverage Age by City:\n", grouped_data)
"""