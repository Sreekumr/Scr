#!C:\xampp\htdocs\PracticeFolder\venv\Scripts\python.exe

import cgi
import cgitb
import MySQLdb

cgitb.enable()

mydb= MySQLdb.connect(host="localhost", user="root", password="", db="test")

cursor = mydb.cursor()
print("Content-type:text/html")
print()

def create_user(cursor,username,password):
    sql="INSERT INTO user(`username`,`password`) VALUES(%s,%s)"
    cursor.execute(sql,(username,password))

def Read_user(cursor,username):
    sql="SELECT * FROM user WHERE username= %s"
    cursor.execute(sql,(username,))
    return cursor.fetchall()

        
def  Updata_user(cursor,username,new_username,new_password):
    sql="UPDATE user SET username=%s, password=%s WHERE username=%s"
    cursor.execute(sql,(new_username,new_password,username))

    
def Delete_user(cursor,username):
    sql="DELETE FROM user WHERE username=%s"
    cursor.execute(sql,(username,))

try :
    form=cgi.FieldStorage()
    action= form.getvalue('action')
    if action=='Create':
        username=form.getvalue('username')
        password=form.getvalue('password')
        create_user(cursor,username,password)
        mydb.commit()
        print(f"<p><h1>User {username} Created successfully!</h1></p>")
     
    elif action=='Read':
        username=form.getvalue('username')
        user_data=Read_user(cursor,username)
        if user_data:
            for row in user_data:
                print(f"<p><h2>Username: {row[1]}, Password: {row[2]}</h2></p>")
        else:
             print(f"<p><h2>NO User found!!</h2></p>")


    elif action == 'Update':
        username=form.getvalue('old_username')
        new_username=form.getvalue('new_username')
        new_password=form.getvalue('new_password')
        Updata_user(cursor,username,new_username,new_password)
        mydb.commit()
        print(f"<p><h2>User:{username} Updated!!</h2></p>")

    elif action == 'Delete':
        username=form.getvalue('username')
        Delete_user(cursor,username)
        mydb.commit()
        print(f"<p><h2>User:{username} Deleted!!</h2></p>")


except Exception as e:
    print(e)
finally:
    mydb.close()