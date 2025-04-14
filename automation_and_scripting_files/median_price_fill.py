import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {'price': [100, 150, np.nan, 200, np.nan, 180, 120]}
df = pd.DataFrame(data)

# Print the DataFrame before filling missing values
print("Before filling missing values:")
print(df)

# Fill missing values with the median
median_price = df['price'].median() # calculate the median of the 'price' column and save it as the variable median_price

df['price'].fillna(median_price, inplace=True) # update the dataframe directly using the value assigned to the median_price variable
# this could have also been done directly using df['price'].fillna(.median()), but without the variable median_price being created

# Print the DataFrame after filling missing values
print("\nAfter filling missing values:")
print(df)