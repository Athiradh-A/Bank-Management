import mysql.connector 
connection = mysql.connector.connect(host = 'localhost',
                                    user = 'root',passwd = 'admin')     

cursor = connection.cursor()
cursor.execute("use bank")

choice = input("Enter choice\n1:Cash Withdrawal\n2:Cash Deposit\n")
more = 'Y'
while more.lower() == 'y':
    if int(choice) == 1:
        accid = input("Enter accound number:")
        cursor.execute("select Balance,Password from holder"+" where Account_Number='%s'"%(accid))
        rec = cursor.fetchall()
        print("================================")
        print("Cash Withdrawal")
        for bal in rec:
            balanc = bal[0]
            pas = bal[1]
            amt = input("Enter amount:")
            passwd = input("Enter password:")
            if passwd == pas:
                if int(balanc) - int(amt) < 0:
                    print("Sorry!! Not enough balance in account!!")
                else:
                    print("Transaction in process.............")
                    done = "update holder set Balance=Balance-%s"%(amt)+" where Account_Number='%s'"%(accid)
                    try:
                        cursor.execute(done)
                        connection.commit()
                        print("Transaction Successfull!!")                    
                    except:
                        connection.rollback()
                
    elif int(choice) == 2:
        more = 'Y'
        while more.lower() == 'y':
            print("================================")
            print("Selected to deposit money!")
            accid = input("Enter account number:")
            amt = int(input("Enter amount to deposit:"))
            confirm = input('Are you sure to deposit this money?\nYes(y)\nNo(N)\n')
            if confirm.lower() == 'y':
                print("Transaction in process.............")
                done = "update holder set Balance=Balance+%s"%(amt)+" where Account_Number='%s'"%(accid)
                try:
                    cursor.execute(done)
                    connection.commit()
                    print("Deposit Successfull!!")                    
                except:
                    connection.rollback()
            else:
                more = input("Deposit again?(y/n):")