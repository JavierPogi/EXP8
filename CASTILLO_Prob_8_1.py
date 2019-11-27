import pandas as pd

cars=pd.read_csv('cars.csv')
y = (cars.head(5))
z = (cars.tail(5))  
print(y)
print(z)