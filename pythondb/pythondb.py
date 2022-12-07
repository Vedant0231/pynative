import mysql.connector
username= input("enter your name: ")
useraddress= input("enter your address: ")
try:
    connection = mysql.connector.connect(host="localhost",database="demodb",user="vedant",password="vedant123")
    insert_data="insert into demotable values('{}','{}')".format(username,useraddress)
    cursor=connection.cursor()
    cursor.execute(insert_data)
    connection.commit()
    print("dear",'{}'" your data is saved".format(username))
except mysql.connector.Error as error:
    print("dear",'{}',"your data didn't saved".format(username))    

# """DELETE FROM demotable WHERE name='vedant,deep'"""
# """select * from  users where name='{}' and address='{}'"""


# try:
#     connection = mysql.connector.connect(host="localhost",database="demodb",user="vedant",password="vedant123")
#     insert_data="""DELETE FROM demotable WHERE name='vedant'"""
#     cursor=connection.cursor()
#     cursor.execute(insert_data)
#     connection.commit()
#     print("done")
# except mysql.connector.Error as error:
#     print(" not done")