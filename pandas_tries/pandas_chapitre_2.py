import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("./311-service-requests.csv", encoding='latin1')

print("\n------- 2.1 -------\n")
print(df.info())
print(df.head())
print(df.describe())

print("\n------- 2.2 --------\n")
print(df["Complaint Type"])

print("\n------- 2.3 --------\n")
print(df.columns.values)

print("\n------- 2.4 --------\n")
print(df["Complaint Type"].value_counts().head(10))

print([df['Complaint Type'].value_counts() > 1000])

serie = [df['Complaint Type'].value_counts() > 1000]

print("\n------- 2.5 --------\n")
# serie.plot.bar()
# df["Complaint Type"].value_counts().plot.bar()
plt.show()

