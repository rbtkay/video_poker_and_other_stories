import pandas as pd
import numpy as np

print(pd)
print(np)

print("\n--------- Partie 1 ---------\n")

liste = list(range(0, 17))
dictionary = {"A":  0, "B":1, "C":2, "D":3, "E":5}

serie = pd.Series(dictionary)

print(serie)

dictionaire = {x:np.random.randint(0,100,50) for x in "ABCDE"}

pandas_serie = pd.DataFrame.from_dict(dictionaire)
print(pandas_serie)

# print(pandas_serie.describe())

# serie_a = pandas_serie["A"].value_counts()
print("value count")
serie_b = [pandas_serie["B"].value_counts()]
# serie_c = pandas_serie["C"].value_counts()
# serie_d = pandas_serie["D"].value_counts()
# serie_e = pandas_serie["E"].value_counts()

print("superieur a 30")
serie_b = [pandas_serie["B"] > 30]

print("\n\n\n")

liste1 = list(range(0, 14))
liste2 = list(range(10, 24))

serie1 = pd.Series(liste1)
serie2 = pd.Series(liste2)

liste3 = pd.concat([serie1,serie2],axis=1)

print(liste3)