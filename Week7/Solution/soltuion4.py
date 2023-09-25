from pandas import *

Column=['Product No', 'Product Name', 'January', 'February', 'March', 'April', 'May', 'June']
dtf = read_csv('student1_data.csv
               ')
data = dtf.values.tolist()
total=[sum(i[2::]) for i in data]
average=[int(sum(i[2::])/6) for i in data]

dataframe = DataFrame(data,columns=Column)
dataframe['Total']=total
dataframe['Average']=average

print(dataframe)
