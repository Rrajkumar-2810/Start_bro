import pandas as pd
#Handling null values and creating new modified files from the original ones 
#Using methods to change null values using dictionary data type along with column names

df = pd.read_excel("D:/PYVSCODE/Start_Bro/stock_data.xlsx", "Sheet1")
print(df)

def convert_people_cell(cell):
    if cell == "n.a.":
        return "Winston Churchill"
    return cell

def convert_eps_cell(cell):
    if cell == "not available":
        return None
    return cell

def convert_price_cell(cell):
    if cell =="n.a.":
        return 0
    return cell
df = pd.read_excel("D:/PYVSCODE/Start_Bro/stock_data.xlsx", "Sheet1", converters= {
    'people': convert_people_cell, # calling function to handle n.a. values in data
    'eps': convert_eps_cell, # calling function to handle n.a. values in data 
    'price': convert_price_cell
})
print(df)

df.to_excel("D:/PYVSCODE/Start_bro/new_stock_changes1.xlsx", sheet_name= "stocks1", index= False) #Creating a new excel file with the changes
#index = False; will remove the indexing from the files
df.to_excel("D:/PYVSCODE/Start_bro/new_stock_changes2.xlsx", sheet_name= "stocks2", startrow=1, startcol=2) #Creating a new excel file with the changes
