import pandas as pd

#Import the titanic dataset
url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df= pd.read_csv(url)

#Show first 5 rows
print("First 5 rows are:")
print(df.head())

#Show basic information
print("\nDataset info:")
print(df.info())

#Show missing values
print("\nMissing values:")
print(df.isnull().sum())

#Show summary statistics
print("\nSummary Statistics:")
print(df.describe())
