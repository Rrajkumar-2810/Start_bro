import numpy as np
import pandas as pd

df = pd.read_csv("D:/PYVSCODE/Start_Bro/weather_data_pandas6.csv")
print(df) #Printing the CSV File

new_df = df.replace(-99999, np.nan) #Replacing one type of values with NaN   
print(new_df) #df.replace(df['windspeed']=-99999, np.nan)

df =df.replace([-99999, -88888], np.nan) #Replacing two type of values with NaN
print(df)

df = pd.read_csv("D:/PYVSCODE/Start_Bro/weather_data_pandas6.csv")
print(df) #Printing the CSV File

df = df.replace({
    'temperature': -99999,
    'windspeed': -99999,
    'event': '0'
}, np.nan)
print(df)

reg_df = pd.read_excel("D:/PYVSCODE/Start_Bro/regex_weather_data.xlsx")
print(reg_df) #Printing the xlsx file

reg_df = reg_df.replace('[A-Za-z]', '', regex=True)
print(reg_df) #Printing without the dataset after removing the units from the columns 

reg_df = pd.read_excel("D:/PYVSCODE/Start_Bro/regex_weather_data.xlsx")
print(reg_df)

reg_df = reg_df.replace({
    'temperature': '[A-Za-z]',
    'windspeed': '[A-Za-z]',
}, '', regex=True)
print(reg_df) #Printing only the numbers after removing the units from the columns and making the event column unaffected by the changes

student_df = pd.DataFrame({
    'score' : ['good','excellent','average','poor','average','good','poor'],
    'names': ['raj','vikas','dharm','james','sarah','leah','ben']
})
print(student_df)

new_student_df = student_df.replace(['poor','average','good','excellent'], [1,2,3,4])
print(new_student_df)
