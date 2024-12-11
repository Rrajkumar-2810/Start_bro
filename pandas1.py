import pandas as pd
#DataFrame is a main object in pandas. Used to represent data in the form of rows and columns

df = pd.read_csv("D:/PYVSCODE/Start_bro/nyc_weather.csv") #Using a variable to access and store the data from the CSV file.
print(df)

print("Max temperature=",df['Temperature'].max()) #Max temperature
print("Min temperature=", df['Temperature'].min()) #Min temperature
print("Mean Temperature=", df['Temperature'].mean()) #Mean temperature
print("df shape=", df.shape) # Rows and columns

print("Max dew point=",df['DewPoint'].max()) #Max Dewpoint
print("Min dew point=",df['DewPoint'].min()) #Min Dewpoint
print("Mean Dewpoint=", df['DewPoint'].mean()) #Mean Dewpoint
print("Range of dew point=",df['DewPoint'].max()- df['DewPoint'].min()) #Range of Dewpoint

print("Max humidity=",df['Humidity'].max()) #Max humidity
print("Min humidity=",df['Humidity'].min()) #Min humidity
print("Mean humidity=", df['Humidity'].mean()) #Mean humidity
print("Range of Humidity=",df['Humidity'].max()-df['Humidity'].min()) #Range of Humidity

print("Dates on which it rained:\n",df['EST'][df['Events']=='Rain'])
print("WindSpeed Mean=",df['WindSpeedMPH'].mean()) #Wind Speed Mean before filling null values with zero

print("Null values=",df.fillna(0, inplace=True))
print("WindSpeed Mean=",df['WindSpeedMPH'].mean()) #Wind Speed Mean after Filling null values with zero

