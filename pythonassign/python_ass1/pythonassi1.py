import csv
import mysql.connector

var_a="/home/neosoft/Desktop/pythonassign/python_ass1/data.csv"

with open(var_a,"r") as f:

     var_fr=csv.reader(f,delimiter=",")
     for i in var_fr:
         print(i)

conn=mysql.connector.connect(host="localhost",user="root",password="p@ssw0rd",database="Info_Emp")
cur=conn.cursor()

# cur.execute("create table Payroll(Name Varchar(50) Primary Key,Department Varchar(50) NOT NULL ,Salary int(10) NOT NULL )")
# conn.close()
# csv_data = csv.reader(open('/home/neosoft/Desktop/pythonassign/python_ass1/data.csv'))
# for i in csv_data:
#     cur.execute("Insert into  Payroll (Name,Department,Salary) VALUES('{}','{}',{})" .format(i[0],i[1],i[2]))
# conn.commit()
# cur.close()











