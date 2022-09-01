import tweepy as tp
import PyPDF2
import unicodedata
from fpdf import FPDF
import pandas as pd
import os
from dotenv import load_dotenv
import mysql.connector
bearer_token = "AAAAAAAAAAAAAAAAAAAAAOOAfgEAAAAAvwQffXw45CQTyiGMSHrjoSpEK%2F8%3Dbdj3UQvwuYABj4vLoCIaYJl3VIcTHSnGQB6pvwOaxFWDsUSLE9"
api_key="8PK3LfQAsZE3BlAca7a74BqQP"
api_secret="4sYbygissZJaBZiMnUi2uBgvEojHG4L7KdjzobbClQo0OxQaaF"
access_token="1555469416615530496-7pV5F0ET88vaMXx6MltKPC6WdwoCsC"
access_token_secret="Y8x1D7Z8wgJ2Jr9cmbqUxzBsqzirmqTje5E9XnbqKCVBZ"

var_a=tp.OAuthHandler(api_key,api_secret)
var_a.set_access_token(access_token,access_token_secret)
var_api=tp.API(var_a,wait_on_rate_limit=True)
var_api=tp.API(var_a)
# print(type(var_api))
var_tweets=var_api.home_timeline()
print(type(var_tweets))
for i in var_tweets:
     print(i.text)

pdf=FPDF()
pdf.add_page() 
pdf.add_font('Calibri Regular', '', '/home/neosoft/Desktop/pythonassign/Calibri/Calibri.ttf', uni=True)
pdf.set_font('Calibri Regular', '', 17)

# for j in i.text:
#     print(j,end="")
#     pdf.write(8,j)
for i in var_tweets:
  for j in i.text:
    print(j,end="")
    pdf.write(8,j)
  pdf.write(8,"\n")

pdf.output("mypdf.pdf")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="p@ssw0rd",
  database="testdb")
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE Tweets (name VARCHAR(255))")
mycursor.execute("Insert into Tweets(name) VALUES ('{}')".format(i.text))
mydb.commit()


