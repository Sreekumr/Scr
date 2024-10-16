#!C:\xampp\htdocs\PracticeFolder\venv\Scripts\python.exe

import cgi
import cgitb
import MySQLdb 

cgitb.enable()

try:
    mydb = MySQLdb.connect(host="localhost",user="root",password="",db="test" )
    myCursor = mydb.cursor()

    form = cgi.FieldStorage()
    username = form.getvalue('username')
    password = form.getvalue('password')

    sql = "INSERT INTO user (`username`,`password`) VALUES(%s,%s)"
    myCursor.execute(sql,(username,password))
    mydb.commit()
    print("Content-type:text/html")
    print()
    print(f'''<!DOCTYPE html>
                <html lang='en'>
                    <head>
                        <meta charset='UTF-8'>
                        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
                        <title>Welcome</title>
                    </head>
                    <body>
                        <center>
                            <h1>Welcome, {username}!</h1>
                            <p>Your login was successful.</p>
                            <a href='index.html'>Back to Login</a>
                        </center>
                    </body>
                </html>''')


except Exception as e:
    print(e)
finally:
    mydb.close()