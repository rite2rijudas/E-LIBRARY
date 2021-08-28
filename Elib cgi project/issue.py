#!C:\Python38-32\python.exe
print("content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
form=cgi.FieldStorage()
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="elib_sdf")
cur=db.cursor()
a=int(form.getvalue('id'))
cur.execute("select * from book where id=%d"%(a))
r=cur.fetchone()
print("""
<html>
<head>
    <title>Login And Registration Form - Easy Tutorials</title>
    <link rel="stylesheet" href="css/style2.css">
      
    
</head>
<body>
    <div class="hero">
        <div class="form-box">
            <div class="button-box">
              <div id="btn"></div>
                <button type="button" class="toggle-btn" onclick="login()">Register </button>
                
            </div>
        
        <form id="login" class="input-group" action="issue_code.py">
            <input type="text" class="input-field" placeholder="Card id" name="a1" required>
            <input type="text" class="input-field" placeholder="User Name" name="a2" required>
			<input type="text" class="input-field" placeholder="Email" name="a3" required>
			<input type="text" class="input-field" placeholder="Phone Number" name="a4" required>
			<input type="text" class="input-field" placeholder="Address" name="a5" required>
            <input type="hidden" class="input-field"  name="a6" value="%d">
            <button type="submit" class="submit-btn">Insert</button>
           
        </form>
        
    </div>
  </div>
  <script>
      var x = document.getElementById("login");
      var y = document.getElementById("register");
      var z = document.getElementById("btn");
      
      function register(){
          x.style.left = "-400px";
          y.style.left = "50px";
          z.style.left = "110px";
      }
      function login(){
          x.style.left = "50px";
          y.style.left = "450px";
          z.style.left = "0";
      }
  </script>
</body>
</html>
"""%(r[0]))