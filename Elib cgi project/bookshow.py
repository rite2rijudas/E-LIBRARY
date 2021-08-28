#!C:\Python38-32\python.exe
print("content-type:text/html\r\n\r\n")
import cgi
import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",passwd="",db="elib_sdf")
cur=db.cursor()
cur.execute("select * from book")
x=cur.fetchall()
print("""
<html>
<body>
<table>
""")
for i in x:
	print("""
	<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><a href="issue.py?id=%d">issue</a></td></tr>
	"""%(i[1],i[2],i[3],i[4],i[0]))
print("""
</table>
</body>
</html>
""")