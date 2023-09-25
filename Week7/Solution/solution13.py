from pandas import  *

df = read_csv('student1_data.csv')

print(df.sort_values(by="Prod_Name"))
