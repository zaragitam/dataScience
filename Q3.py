# Effective Strategies for Handling Missing Values in Data Analysis
import pandas as pd
import numpy as np

# Creating a sample DataFrame with missing values
data = {
    'School ID': [101, 102, 103, np.nan, 105, 106, 107, 108],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry'],
    'Address': ['123 Main St', '456 Oak Ave', '789 Pine Ln', '101 Elm St', np.nan, '222 Maple Rd', '444 Cedar Blvd', '555 Birch Dr'],
    'City': ['Los Angeles', 'New York', 'Houston', 'Los Angeles', 'Miami', np.nan, 'Houston', 'New York'],
    'Subject': ['Math', 'English', 'Science', 'Math', 'History', 'Math', 'Science', 'English'],
    'Marks': [85, 92, 78, 89, np.nan, 95, 80, 88],
    'Rank': [2, 1, 4, 3, 8, 1, 5, 3],
    'Grade': ['B', 'A', 'C', 'B', 'D', 'A', 'C', 'B']
}

df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)

# Removing rows with missing values
df_cleaned = df.dropna()

# Displaying the DataFrame after removing missing values
print("\nDataFrame after removing rows with missing values:")
print(df_cleaned)

# Imputation Methods
# Mean, Median, and Mode Imputation
mean_imputation = df['Marks'].fillna(df['Marks'].mean())
median_imputation = df['Marks'].fillna(df['Marks'].median())
mode_imputation = df['Marks'].fillna(df['Marks'].mode().iloc[0])

print("\nImputation using Mean:")
print(mean_imputation)

print("\nImputation using Median:")
print(median_imputation)

print("\nImputation using Mode:")
print(mode_imputation)

# Forward and Backward Fill
forward_fill = df['Marks'].fillna(method='ffill')
backward_fill = df['Marks'].fillna(method='bfill')

print("\nForward Fill:")
print(forward_fill)

print("\nBackward Fill:")
print(backward_fill)

# Interpolation Techniques
linear_interpolation = df['Marks'].interpolate(method='linear')
# Quadratic interpolation requires at least 3 data points that are not NaN
quadratic_interpolation = df['Marks'].interpolate(method='quadratic')

print("\nLinear Interpolation:")
print(linear_interpolation)

print("\nQuadratic Interpolation:")
print(quadratic_interpolation)
