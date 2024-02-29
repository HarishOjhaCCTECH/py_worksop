import pandas as pd

filePath = "C:/Users/Harish Ojha/Downloads/titanic.csv"
data1 = pd.read_csv(filePath)
""" survival_counts = data1.groupby('Survived').count()
# print(survival_counts)
survival_counts """
print(data1.Survived.unique())

