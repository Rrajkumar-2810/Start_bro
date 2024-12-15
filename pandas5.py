import pandas as pd

df = pd.read_csv("D:/PYVSCODE/Start_Bro/weather_data_pandas5.csv")
print(df)
print("Data Type for changing:",type(df.day[0])) #Data Type for changing

df = pd.read_csv("D:/PYVSCODE/Start_Bro/weather_data_pandas5.csv", parse_dates= ["day"]) #Parsing dates
print(df)
print("Data type after modifying:",type(df.day[0])) #Data type after modifying

df = pd.read_csv("D:/PYVSCODE/Start_Bro/weather_data_pandas5.csv", parse_dates= ["day"]) #Parsing dates
df.set_index('day', inplace=True) #Setting Day column as index 
print(df)

new_df = df.fillna(0) #Used for filling null values with any replacement value.
print("Fill_nullvalues:", new_df) #printing the new dataset after replacing it with null values.

new_df = df.fillna({
    'temperature': 0,
    'windspeed': 0,
    'event': 'no event'
})
#Using dictionary and fillna to modify the values as required or needed using column names.
print("Dictionary_fill:", new_df) 

new_df = df.fillna(method="ffill") #ffill method is used to carry forward the previous values to the next downward row if it is empty or null.
print("Forward_fill:", new_df) 

new_df = df.fillna(method="bfill") #bfill method to carry backwards the value from the downward row values to upward row if it is empty or null.
print("Backward_fill:",new_df)

new_df = df.fillna(method="ffill", limit=1) #ffill method is used with limit=1 so that only it can carry forward the value only to 1 next row, it cannot go further from that
print("Forward_fill with limit 1:", new_df) #limit determines how far the value can be copied to the next row.

new_df = df.fillna(method="ffill", limit=1) #ffill method is used with limit=1 so that only it can carry forward the value only to 1 next row, it cannot go further from that
print("Forward_fill with limit 2:", new_df) #limit determines how far the value can be copied to the next row.

#Interpolation is a method for estimating values between known points in a data set.
new_df = df.interpolate() #default (method="linear") inside interpolate method.
print("Interpolation with linear:", new_df) 

new_df = df.interpolate(method="time")
print("Interpolation with time:", new_df)

new_df = df.dropna()
print("Drop the rows if a null value is present in any of the columns:\n", new_df)

new_df = df.dropna(how="all")
print("Drop the rows whose all rows data are null values:\n", new_df)

#Both how="all" and thresh=1 represent the same meaning while handling null values.
new_df = df.dropna(thresh=1)
print("Drop the rows which doesn't even have one single non-null value:\n", new_df)

new_df = df.dropna(thresh=2)
print("Drop the rows which doesn't have two single non-null value:\n", new_df) 

#Inserting missing date ranges which is not present in the data.
dt = pd.date_range("01-01-2017","01-11-2017") #Mentioning the date range of the dataset.
idx = pd.DatetimeIndex(dt) #Using the datetime index to insert missing date values.
df = df.reindex(idx) #Reindexing the dataset to insert the date row and its values.
print("Adding the dates which is not present in the data:\n",df) #Modified dataset

