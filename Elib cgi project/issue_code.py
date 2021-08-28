#!C:\Python38-32\python.exe
#print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
form=cgi.FieldStorage()
a=form.getvalue('a1')
b=form.getvalue('a2')
c=form.getvalue('a3')
d=form.getvalue('a4')
e=form.getvalue('a5')
f=form.getvalue('a6')
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="elib_sdf")
cur=db.cursor()
cur.execute("insert into applied (cid,uname,email,phno,addr,bid) values ('%s','%s','%s','%s','%s','%s')"%(a,b,c,d,e,f))
db.commit()
db.close()
print("location:welcome.html?msg=done\r\n\r\n")