import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('bikes.csv', delimiter=';', parse_dates=True, index_col="Date")

print(df)

# maisonneuve =  df["Maisonneuve 1"]
# date = df["Date"]
# print(maisonneuve)
# plt.plot(date, maisonneuve)
df.plot(subplots=True)
plt.show()


# const ACCESS_CONTROL = 
# [ 
#     'Access-Control-Expose-Headers' => 'Access-Control-',
#     'Access-Control-Allow-Origin' => '',
#     'Access-Control-Allow-Headers' => '*',
#     'Access-Control-Allow-Methods' => 'HEAD, PUT, GET, POST, DELETE, OPTIONS',
#     'Allow' => 'HEAD, PUT, GET, POST, DELETE, OPTIONS'
# ];**