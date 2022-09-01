from bs4 import BeautifulSoup
import requests
import mysql.connector

url="https://www.instagram.com/stock123_098/"
response = requests.get(url)
soup=BeautifulSoup(response.content ,"html.parser")
var_a=soup.find("link")
print(var_a.get("href"))  
conn = mysql.connector.connect(host="localhost", user="root", password='p@ssw0rd',database='insta_scrap')
cur=conn.cursor()
#cur.execute("create table for_scrap( Link Varchar(500) NOT NULL)")
cur.execute("Insert into for_scrap(Link) VALUES('{}')".format(var_a.get("href")))
conn.commit()
cur.close()



