#this code is used to insert user input data and delete data
import mysql.connector
username= input("enter your name: ")
useraddress= input("enter your address: ")
userpassword = input("enter your password: ")
option= input("what you want to do:  ")
if option =="insert":
    connection = mysql.connector.connect(host="localhost",database="your database name",user="your user name",password="your password")
    insert_data="insert into userdata values('{}','{}',{})".format(username,useraddress,userpassword)
    cursor=connection.cursor()
    cursor.execute(insert_data)
    connection.commit()
    print("dear",'{}'" your data is saved".format(username))
elif option == "delete":
    connection = mysql.connector.connect(host="localhost",database="your database name",user="your user name",password="your password")
    delete_data = "delete from userdata where name='{}' and password='{}'".format(username,userpassword)
    cursor=connection.cursor()
    cursor.execute(delete_data)
    connection.commit()
    print("dear",'{}'" your data is deleted".format(username))
else:
    print("we don't have this option")

