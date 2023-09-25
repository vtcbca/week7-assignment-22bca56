from pandas import *

Column=['Product No', 'Product Name', 'January', 'February', 'March', 'April', 'May', 'June']
dtf = read_csv('student1_data.csv')
DTF = DataFrame(dtf.values.tolist(),columns=Column)
print(DTF)

