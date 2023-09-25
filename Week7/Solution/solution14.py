from pandas import  *

df = read_csv('student1_data.csv')

print(df.iloc[:, 1::2])
