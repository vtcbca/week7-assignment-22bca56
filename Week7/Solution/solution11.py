from pandas import *

dtf = read_csv('student1_data.csv')

print(dtf[['Prod_No','Prod_Name','Jan']])
