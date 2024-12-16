import pandas as pd

df = pd.read_csv("D:/PYVSCODE/Start_Bro/weather_by_cities.csv")
print(df)

g = df.groupby('city')
print(g)

for city, city_df in g:
    print(city)
    print(city_df)

print("All data will get printed related to city Mumbai:\n",g.get_group('mumbai'))

print("Max temperature in all cities:\n",g.max())
print("All statistical data:\n",g.describe())
