import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password='p@ssw0rd',
    database='testdb'
)
mycursor=mydb.cursor()           #Cursor is an object that communicates with the entire MYSQL server

# mycursor.execute("SHOW DATABASES")
# for i in mycursor:
#     print(i)

# mycursor.execute("CREATE TABLE Books( id int(10) Primary Key ,Bookname Varchar(55),Author Varchar(55) ,Category Varchar(55) )")
# mycursor.execute("CREATE TABLE CategoriesName( id int(10) Primary Key ,Bookname Varchar(55),Author Varchar(55) ,Category Varchar(55) )")

# var_a= "Insert into Books (id,Bookname,Author,Category) Values (%s,%s,%s,%s)"
# var_1=(1,"The India Story","Bimal Jalal","Action and Adventure")
# var_2=(2,"A Place Called Home","Preeti Shenoy","Classics")
# var_3=(3,"Lal Salam","Smriti Irani","Fantasy")
# var_4=(4,"Hear Yourself","Rajesh Talwar","Comics")
# var_5=(5,"Rich Dad","Stushi Portal","Finance")
# var_6=(6,"Atal Bihari Vajpayee","Shivam Shetty","Literary Fiction")
# var_7=(7,"The $10 Trillion Dream","Ruskin Bond","Classics")
# mycursor.execute(var_a,var_1)
# mycursor.execute(var_a,var_2)
# mycursor.execute(var_a,var_3)
# mycursor.execute(var_a,var_4)
# mycursor.execute(var_a,var_5)
# mycursor.execute(var_a,var_6)
# mycursor.execute(var_a,var_7)
# mydb.commit()

# var_b="Insert into CategoriesName (id,Bookname,Author,Category) Values (%s,%s,%s,%s)"
# var_1=(1,"Vahana Masterclass","Alfredo Covelli","Historical Fiction")
# var_2=(2,"Unfinished","Priyanka Chopra Jonas","Autobiography")
# var_3=(3,"ASOCA: A Sutra","Irwin Allan Sealy","Fantasy")
# var_4=(4,"Names of the Women","Jeet Thayil","Classics")
# var_5=(5,"Suparipalana","Dr. Shailendra Joshi","Comics")
# mycursor.execute(var_b,var_1)
# mycursor.execute(var_b,var_2)
# mycursor.execute(var_b,var_3)
# mycursor.execute(var_b,var_4)
# mycursor.execute(var_b,var_5)
# mydb.commit()

''' WHERE & AND '''

# var_a="Select *from CategoriesName Where Bookname= 'Unfinished'  AND  Author='Priyanka Chopra Jonas' "
# mycursor.execute(var_a)
# var_result=mycursor.fetchall()  #method fetches all rows of a query result set and returns a list of tuples. 
# for i in var_result:
#     print(i)

'''WHERE & OR '''

#var_a="Select *from CategoriesName Where Bookname= 'Names of the Women'  OR  AUTHOR= ' Jeet' "
var_a="Select *from CategoriesName Where Bookname='{}' OR AUTHOR='{}' ".format('Names of the Women',' Jeet')
mycursor.execute(var_a)
var_result=mycursor.fetchall()  #method fetches all rows of a query result set and returns a list of tuples. 
for i in var_result:
    print(i)

'''Like Operator'''


# var_a="Select *from CategoriesName Where Bookname Like 'U%' "
# mycursor.execute(var_a)
# var_result=mycursor.fetchall()  #method fetches all rows of a query result set and returns a list of tuples.  
# for i in var_result:
#     print(i)


# var_a= "Select Books.Bookname ,CategoriesName.Bookname from Books JOIN CategoriesName ON Books.id=CategoriesName.id"
# mycursor.execute(var_a)
# var_result=mycursor.fetchall()
# for i in var_result:
#     print(i)




