import mysql.connector
from texttable import *

connection = mysql.connector.connect(host = 'localhost',
                                    user = 'root',passwd = 'admin')     

cursor = connection.cursor()

cursor.execute("use bank")
accid = input("Enter account number to modify:")
print("Enter choice to modify\n1:Account number\n2:Account Holder name")
choice = int(input("Enter choice:"))
if int(choice) == 1:
    print("=================================")
    print('Selected to modify account number')
    
    cursor.execute("select * from holder"+" where Account_Number=%s"%(accid))
    commnd = cursor.fetchall()
    for row in commnd:
        print("Account number:",row[0])
        print("Account holder:",row[1])
        print("Age:",row[2])
        print("Balance:",row[3])

    newac = input("Enter new account number:")
    updat = "update holder set Account_Number='%s'"%(newac)+" where Account_Number='%s'"%(accid)
    try:
        cursor.execute(updat)
        connection.commit()
    except:
        connection.rollback()
    
elif int(choice) == 2:
    print('=================================')
    print("selected to modify name")
    cursor.execute("select * from holder"+" where Account_Number=%s"%(accid))
    commnd = cursor.fetchone()
    for row in commnd:
        print(row)
        print("Account number:",row[0])
        print("Account holder:",row[1])
        print("Age:",row[2])
        print("Balance:",row[3])
    accname = input("Enter New Name:")
    updat = "update holder set Account_Holder='%s'"%(accname) + " where Account_Number='%s'"%(accid)
    try:
        cursor.execute(updat)
        connection.commit()
    except:
        connection.rollback()

    
print("Updated!")