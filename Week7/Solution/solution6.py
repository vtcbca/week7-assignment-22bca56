from pandas import *

Column=['Product No', 'Product Name', 'January', 'February', 'March', 'April', 'May', 'June']
dtf = read_csv('student1_data.csv
               ')

dtf.loc[2.5] = [116, 'Portable Hardisk',90,78,76,45,34,22]
dtf = dtf.sort_index().reset_index(drop=True)
dtf.loc[3.5] = [117, 'Power Cable',40,48,60,45,56,21]
dtf = dtf.sort_index().reset_index(drop=True)

print(dtf)
