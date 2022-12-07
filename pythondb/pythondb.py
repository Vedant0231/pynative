#By this program we can save user input data in mysql database
import mysql.connector
username= input("enter your name: ")
useraddress= input("enter your address: ")
try:
    connection = mysql.connector.connect(host="localhost",database="your database name",user="your user name",password="your password")
    insert_data="insert into demotable values('{}','{}')".format(username,useraddress)
    cursor=connection.cursor()
    cursor.execute(insert_data)
    connection.commit()
    print("dear",'{}'" your data is saved".format(username))
except mysql.connector.Error as error:
    print("dear",'{}',"your data didn't saved".format(username))    


