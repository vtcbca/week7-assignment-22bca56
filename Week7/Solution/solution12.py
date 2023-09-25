from pandas import  *

df = read_csv('student1_data.csv')

print(df[(df["Jan"] > 5000) & (df["Feb"] > 8000)][["Prod_No", "Prod_Name"]])

