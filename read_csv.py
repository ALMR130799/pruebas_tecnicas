import pandas as pd


dataframe = pd.read_csv("organizations-1000.csv")

first1 = dataframe[dataframe['Founded'] >= 2000]

print(first1)

