import os
import pandas as pd

is_file = os.path.isfile("./database.csv")

print(is_file)

data = pd.read_csv('./database.csv')

print("\n ----- DATABASE AS DATAFRAME ----- \n")
print(data)
print("\n --------------------------------- \n")

print("\n ----- DATAFRAME COLUMNS ----- \n")
print(data.columns)
print("\n --------------------------------- \n")


print("\n ----- DATAFRAME ROW NUMBER ----- \n")
print(data.shape[0])
print("\n --------------------------------- \n")


print("\n ----- ROW WITH MORE THAN ONE VICTIM ----- \n")
print(data[data["Victim Count"] > 1])
print("\n --------------------------------- \n")


print("\n ----- ROW WITH PERPETRATOR AS MALE ----- \n")
print(len(data[data["Perpetrator Sex"] == "Male"]))
print("\n --------------------------------- \n")

print("\n ----- ROW WITH PERPETRATOR AS FEMALE ----- \n")
print(len(data[data["Perpetrator Sex"] == "Female"]))
print("\n --------------------------------- \n")


print("\n ----- NUMBER OF CRIMES AFTER THE 2000s ----- \n")
print(len(data[data["Year"] > 2000 ]))
print("\n --------------------------------- \n")


print("\n ----- CRIME COMMITTED ----- \n")
print(len(data[(data["Victim Count"] > 4) & (data["Month"] == "August")]))
print("\n --------------------------------- \n")
