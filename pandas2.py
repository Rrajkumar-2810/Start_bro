import pandas as pd

df = pd.read_csv("D:/PYVSCODE/Start_Bro/weather_data.csv")
print(df)
print('Shape:', df.shape)
rows, columns = df.shape
print('Columns:', columns)
print('Describe:', df.describe())
print('Rainy days:\n', df['day'][df['event']=='Rain'])
print('Sunny days:\n', df['day'][df['event']=='Sunny'])
print('Snowy days:\n', df['day'][df['event']=='Snow'])

print('Max temperature:', df['temperature'].max()) #Max temperature
print('Min temperature:', df['temperature'].min()) #Min temperature

print('Max wind speed:', df['windspeed'].max()) #Max wind speed
print('Min wind speed:', df['windspeed'].min()) #Min wind speed

print("Head:\n", df.head(2)) #prints all the data records from heading to the count of record number mentioned.
print("Tail:\n", df.tail(2)) #prints all the data records from last record to the count of record number mentioned

print(df.columns) # Prints all the columns name 
print(df['event'])
print("Event with date:\n",df[['event','day']])
print("Event with date and temperature:\n",df[['event','day','temperature']])
print("Temperature greater than 32:\n",df[df.temperature >= 32]) #df[df['temperature']]
print("Max Temperature record:\n",df[df.temperature == df['temperature'].max()])
print("The day on which temperature was maximum:\n", df[['day','temperature']][df.temperature == df['temperature'].max()])

#Indexing
print("Setting index as day",df.set_index('day', inplace=True)) #Setted day as index
print(df)
print("Resetting index:",df.reset_index(inplace=True)) #Resetting index
print(df)

print("Setting index as event",df.set_index('event', inplace=True)) #Setted event as index
print(df)
print(df.loc['Snow'])
print("Resetting index:", df.reset_index(inplace=True)) #Resetting index back to original
print(df)
