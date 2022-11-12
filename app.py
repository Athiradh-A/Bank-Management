print("Welcome to ")

more = 'Y'
while more.lower() == 'y':
    sel = input("select your choice\n1:|Transactions|\n2:|Account details and modifications|\n3:|Admin|\n")
    if int(sel) == 1:
        print("=====================================")
        print("Selected transactions")
        from subfiles import transaction
    elif int(sel) == 2:
        print("=====================================")
        print("Selected Account details and modifications ")
        from subfiles import account
    elif int(sel) == 3:
        print("=====================================")
        print("selected Admin controls")
        from subfiles import admin

    more = input("Want ot run program once more?(Y/N):")
