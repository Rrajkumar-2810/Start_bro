import pandas as pd

df = pd.read_csv("D:/PYVSCODE/Start_bro/nyc_weather.csv")
#print(df)

print("Max temperature=",df['Temperature'].max())
print("df shape=", df.shape)
