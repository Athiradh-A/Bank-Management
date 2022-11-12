import mysql.connector
from texttable import *

connection = mysql.connector.connect(host = 'localhost',
                                    user = 'root',passwd = 'admin')     

cursor = connection.cursor()

cursor.execute("use bank")

paswd = 123029
passwd = input('Enter password:')
if int(passwd) == paswd:
    print("Logged in as admin")
    again = 'Y'
    while again.lower() == 'y':
        choice = input("enter choice Number\n1:Show all records\n2:Select record\n")
        if int(choice) == 1:
            print("==================================")
            print("Selected all records!")
            cursor.execute("select * from holder")
            rec = cursor.fetchall()
            for allrec in rec:
                print(list(allrec))

        elif int(choice) == 2:
            more = 'Y'
            while more.lower() == 'y':
                print("==================================")
                print("Select single record")
                accid = input("Enter Accound number:")
                cursor.execute("select * from holder"+" where Account_Number=%s"%(accid))
                rec = cursor.fetchall()
                for dat in rec:
                    print("Account holder:",dat[1])
                    print("Age:",dat[2])
                    print("Balance:",dat[3])
                    print("Password:",dat[4])
                    more = input("search more?(Y/N)")
    
        again = input("Do again?(Y/N)")