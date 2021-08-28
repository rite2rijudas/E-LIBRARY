#!C:\Python38-32\python.exe
#print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
form=cgi.FieldStorage()
a=form.getvalue('a1')
b=form.getvalue('a2')
c=form.getvalue('a3')
d=form.getvalue('a4')

db=mysql.connector.connect(host="localhost",user="root",passwd="",db="elib_sdf")
cur=db.cursor()
cur.execute("insert into book (title,aut,cata,pub) values ('%s','%s','%s','%s')"%(a,b,c,d))
db.commit()
db.close()
print("location:adwelcome.html?msg=done\r\n\r\n")