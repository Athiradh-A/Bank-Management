import mysql.connector 
connection = mysql.connector.connect(host = 'localhost',
                                    user = 'root',passwd = 'admin')     

cursor = connection.cursor()

cursor.execute("use bank")

more = 'Y'
while more.lower() == 'y':
    print('===========================================')
    print('Select an option\n1:Add new account\n2:Modify account details\n3:Close an account')
    choice = input("Enter your choice number:")
    if int(choice) == 1:
        print("Selected to add record")
        accno = input("Enter account number: " )
        name = input("Enter name:")
        age = int(input("Enter age: "))
        balanc = int(input("Enter balance in account:"))
        passwd = input('Enter password of your account:')
        ins = 'insert into holder(Account_number,Account_Holder,Age,Balance,Password) values(%s,%s,%s,%s,%s)'
        values = (accno,name,age,balanc,passwd)
        cursor.execute(ins,values)
        print('Added')
        connection.commit()
        print('=======================================')
    elif int(choice) == 2:
        print('=======================================')
        print("Selected to modify record")
        import modify
    

    elif int(choice) == 3:
        print("=======================================")
        print("Selected to delete record")
        accid = input("Enter Account Number To Close Account:")
        confirm = input("Are you sure that you wnat to delete this account??\nY\nN\n")
        if confirm.lower() == 'y':
            dele = "delete from holder"+" where Account_Number='%s'"%(accid)
            try:
                cursor.execute(dele)
                connection.commit()            
            except:
                connection.rollback() 
            print("Record deleted! ")
        else:
            print("Selected to not delete record!")
    
    more = input("Do anything more?(Y/N):")
    
