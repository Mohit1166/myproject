import mysql.connector
import pandas as pd

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="p@ssw0rd",
    database='Info_Emp',
)
mycursor=mydb.cursor()    
var_a=pd.read_sql_query("Select *from Payroll",mydb) #used to read SQL query or database table into DataFrame
print(var_a) 
var_b=pd.DataFrame(var_a)
var_csv=var_b.to_csv(" File.csv")



