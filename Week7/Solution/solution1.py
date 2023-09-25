from csv import *

data=[]
with open('Student_Data.csv','a',newline="") as File_Append:
    file_data = writer(File_Append)
    for i in range(12):
        prod_no = input("Enter Product Number: ")
        prod_name = input("Enter Product Name: ")
        jan = int(input("Enter January Sales: "))
        feb = int(input("Enter February Sales: "))
        mar = int(input("Enter March Sales: "))
        apr = int(input("Enter April Sales: "))
        may = int(input("Enter May Sales: "))
        jun = int(input("Enter June Sales: "))
        sub_data=[prod_no,prod_name,jan,feb,mar,apr,may,jun]
        data.append(sub_data)
    file_data.writerows(data)
