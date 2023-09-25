from pandas import *

Column=['Product No', 'Product Name', 'January', 'February', 'March', 'April', 'May', 'June']
dtf = read_csv('student1_data.csv')
dtf.loc[len(dtf)+1]=[114,'Harddisk',89,78,90,89,99,67]
dtf.loc[len(dtf)+2]=[115,'CD Drive',89,67,34,33,23,10]
print(dtf)
