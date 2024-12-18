import pandas as pd

india_weather = pd.DataFrame({
    'city': ['bengaluru', 'delhi', 'mumbai'],
    'temperature': [34,76,27],
    'humidity': [67,96,80]
})
print("India Weather:\n",india_weather)

us_weather = pd.DataFrame({
    'city': ['texas', 'chicago', 'amsterdam'],
    'temperature': [45,84,97],
    'humidity': [42,76,84]
})
print("US Weather:\n",us_weather)

df = pd.concat([india_weather, us_weather]) #Combines the datasets(Datasets can be 2 or more than one)
print("One Weather Table:\n",df) 

df = pd.concat([india_weather, us_weather], ignore_index=True) #Combines the datasets and Writes index in a semantic manner
print("One Weather Table:\n",df) 

df = pd.concat([india_weather,us_weather], keys=['india','us'])
print("Creates keys and divides the data sectionally to view them:\n",df) 

print("India:\n", df.loc['india'])
print("US:\n",df.loc['us'])


#Using indexing to present the data sequentially to allow easy interpretation of data(Indexing is important)
temperature_df = pd.DataFrame({
    'city': ['bengaluru', 'delhi', 'mumbai'],
    'temperature': [34,76,27]
},index= [0,1,2])

humidity_df = pd.DataFrame({
    'city': [ 'delhi', 'mumbai', 'bengaluru'],
    'humidity': [42,76,84]
}, index=[1,2,0])

temp_humi_df = pd.concat([temperature_df, humidity_df])
print("Combining tables with different columns:\n",temp_humi_df)

temp_humi_df_axis = pd.concat([temperature_df, humidity_df], axis=1)
print("Combining tables with different columns but now with easier interpretation:\n",temp_humi_df_axis)

print("Temperature dataset:\n", temperature_df)

#Creating a new Series of data to add in a dataset
s = pd.Series(['rain', 'hot', 'humidity'], name='event')

#Without axis 
temp_s = pd.concat([temperature_df, s])
print("Adding a new Column to temperature dataset without using axis:\n",temp_s)

#Using Axis for efficient data interpretation
temp_s = pd.concat([temperature_df, s], axis=1)
print("Adding a new Column to temperature dataset:\n",temp_s)
