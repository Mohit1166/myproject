import mysql.connector
import PyPDF2
from fpdf import FPDF
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=20)

data=(
    ("FirstName","LastName","AGE","City"),
    ("Mohit","Mohinani","24","Mumbai"),
    ("Abhishek","Sapkal","22","Pune"),
    ("Dipak","Patil","23","Airoli"),
    ("Akshay","Mewada","27","Thane"),
    ("Tanzil","Shekasol","24","Mumra"),
    ("Akash","Singh","25","Powai"),
    ("Guru","Iyer","24","Kerala"),
    ("Prashant","Reddy","24","TamilNadu"),
    ("Arun","Nair","24","Kerela"),
    )
line_height = pdf.font_size * 2.5
col_width = pdf.epw / 4
for row in data:
    for datum in row:
        pdf.multi_cell(col_width, line_height, datum, border=1,
                new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
    pdf.ln(line_height)

pdf.output('data.pdf')

conn = mysql.connector.connect(host="localhost", user="root", password='p@ssw0rd',database='Info_Emp')
cur=conn.cursor()
# pdf_data = PyPDF2.PdfFileReader(open('data.pdf'))
# for row in pdf_data:
#     print(row)
# for i in data:
#     cur.execute("INSERT INTO Emp_info (FirstName,LastName,AGE,City) VALUES ('{}','{}',{},'{}')".format(i[0],i[1],i[2],i[3]))
# conn.commit()
# cur.close()



