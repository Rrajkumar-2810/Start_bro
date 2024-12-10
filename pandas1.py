import pandas as pd

df = pd.read_csv("D:/PYVSCODE/Start_bro/nyc_weather.csv")
print(df)

print("Max temperature=",df['Temperature'].max()) #MAX temperature
print("Min temperature=", df['Temperature'].min()) #MIN temperature
print("df shape=", df.shape) # Rows and columns


print("Max dew point=",df['DewPoint'].max()) #MAX Dewpoint
print("Min dew point=",df['DewPoint'].min()) #MIN Dewpoint
print("Range of dew point=",df['DewPoint'].max()- df['DewPoint'].min()) #Range of Dewpoint

print("Max humidity=",df['Humidity'].max()) #Max humidity
print("Min humidity=",df['Humidity'].min()) #Min humidity
print("Range of Humidity=",df['Humidity'].max()-df['Humidity'].min()) #Range of Humidity

