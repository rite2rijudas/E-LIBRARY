#!C:\Python38-32\python.exe
print("content-type:text/html\r\n\r\n")
import cgi
import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",passwd="",db="elib_sdf")
cur=db.cursor()
cur.execute("select * from book")
x=cur.fetchall()
print("""
<!DOCTYPE html>
<html lang="en">
   <head>
      <!-- basic -->
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <!-- mobile metas -->
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta name="viewport" content="initial-scale=1, maximum-scale=1">
      <!-- site metas -->
      <title>memorial books</title>
      <meta name="keywords" content="">
      <meta name="description" content="">
      <meta name="author" content="">
      <!-- bootstrap css -->
      <link rel="stylesheet" href="css/bootstrap.min.css">
      <!-- style css -->
      <link rel="stylesheet" href="css/style.css">
      <!-- Responsive-->
      <link rel="stylesheet" href="css/responsive.css">
      <!-- fevicon -->
      <link rel="icon" href="images/fevicon.png" type="image/gif" />
      <!-- Scrollbar Custom CSS -->
      <link rel="stylesheet" href="css/jquery.mCustomScrollbar.min.css">
      <!-- Tweaks for older IEs-->
      <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script><![endif]-->
   </head>
   <style>
   .templatemo_product_box{
       display: flex;
       border: 4px solid black;
   }
   .vbookh{
       margin-left: 30px;
   }
   .text{
    margin-left: 50px;
   }
   .text2{
    margin-left: 50px;
   }
   .issue_button{
    margin-left: 50px !important;
    text-decoration: none !important;
    color: green;
   }
   </style>
   <!-- body -->
   <body class="main-layout">
      <!-- loader  -->
      <div class="loader_bg">
         <div class="loader"><img src="images/loading.gif" alt="#" /></div>
      </div>
      <!-- end loader -->
      <!-- header -->
      <header>
         <!-- header inner -->
         <div class="header">
            <div class="container">
               <div class="row">
                  <div class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col logo_section">
                     <div class="full">
                        <div class="center-desk">
                           <div class="logo"> <a href="index.html"><img src="images/logo.png" alt="#"></a> </div>
                        </div>
                     </div>
                  </div>
                  <div class="col-xl-9 col-lg-9 col-md-9 col-sm-9">
                     <div class="menu-area">
                        <div class="limit-box">
                           <nav class="main-menu">
                              <ul class="menu-area-main">
                                 <li> <a href="index.html">Home</a> </li>
                                 
                                 <li class="active"><a href="vbook.py">View Books</a></li>
                                 <li><a href="adissue.py">View Issue Book</a></li>
								 
                                 <li><a href="index.html">logout</a></li>
                              </ul>
                           </nav>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
         </div>
         </div>
         <!-- end header inner -->
      </header>
      <!-- end header -->
      <!-- about -->
      <div class="about-bg">
         <div class="container">
            <div class="row">
               <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12">
                  <div class="abouttitle">
                     <h2>View Books</h2>
                  </div>
               </div>
            </div>
         </div>
      </div>
      <div class="about">
""")
for i in x:
	print("""       
        <div class="templatemo_product_box">
        <h1 class="vbookh">book name = %s</h1>
            <p class="text">author = %s</p>
            <p class="text2">category = %s</p>
            <div class="issue_button"><a href="issue.py?id=%d">Issue</a></div>

        
        <div class="cleaner">&nbsp;</div>
    </div>
    """%(i[1],i[2],i[3],i[0]))
print("""
            
    </div>   
      <!-- end about -->
      
      <!-- end footer -->
      <!-- Javascript files-->
      <script src="js/jquery.min.js"></script>
      <script src="js/popper.min.js"></script>
      <script src="js/bootstrap.bundle.min.js"></script>
      <script src="js/jquery-3.0.0.min.js"></script>
      <script src="js/plugin.js"></script>
      <!-- sidebar -->
      <script src="js/jquery.mCustomScrollbar.concat.min.js"></script>
      <script src="js/custom.js"></script>
   </body>
</html>
""")