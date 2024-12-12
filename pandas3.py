import pandas as pd

df = pd.read_csv("D:/PYVSCODE/Start_Bro/stock_data.csv") 
print(df)

df = pd.read_csv("D:/PYVSCODE/Start_Bro/stock_data.csv", na_values=['not available','n.a.']) #Null values as represented as NaN
print(df)

df = pd.read_csv("D:/PYVSCODE/Start_Bro/stock_data.csv", na_values={
    'eps': {'not available', 'n.a.'},
    'revenue': {'not available','n.a.','-1'},
    'price': {'not available','n.a.'}
})
print(df)

print(df.to_csv("D:/PYVSCODE/Start_Bro/new_stock_data.csv", index=False)) #Printing new CSV file after modifying the values in the original file
