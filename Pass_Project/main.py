print("""\nThis is a Password Management System Using Python Pandas and Mysql.
Developed by :- Vatsal Chaturvedi
\n""")
import mysql.connector as sql
import pandas as pd
from password import pass_gen
from sqlalchemy import create_engine
import stdiomask
import sys


try:
    con=sql.connect(
                    host="localhost",
                    user='khushal',
                    passwd="126444",
                    database='testdb',
                    auth_plugin="mysql_native_password"
                    )
    cursor=con.cursor()
    engine=create_engine('mysql+pymysql://khushal:126444@localhost/testdb')
    conn=engine.connect()
except:
    print("Error Connecting to Mysql.Aborting !")
    sys.exit()


try:
    dtf=pd.read_sql("SELECT * FROM PASS_LIST;",con)
except Exception as e:
    print(e)
    print("No Previus Records found create a new account instead ?\n(y/n)",end='')
    ch=input()

    if ch=='y':
        rp=stdiomask.getpass(prompt="Enter Root Password : ")
        dtf=pd.DataFrame({"field":["root"],"uname":["root"],"password":[rp]})
        dtf.to_sql(con=conn,name="pass_list",index=False) 
    else:
        sys.exit()


while True:
    print("1.Log in\n2.Save Password\n3.Generate a Password\n4.Change Root Password\n5.Exit")
    choice=int(input("Enter your Choice : "))
    dtf=pd.read_sql("SELECT * FROM PASS_LIST;",con)


    if choice==1:
        root_pass=stdiomask.getpass(prompt="Enter Root Password : ")
        if root_pass==dtf.password[0]:
            print("login successfull !!\n")
            print(dtf.loc[1:,:])
            print("\n1.Search Password by Website.\n2.Modify a Record.\n3.Exit.")
            ch2=int(input("Enter your Choice : "))
            if ch2==1:
                df=dtf
                df.index= df.feild
                feild=input("Website name : ")
                df=df.loc[feild,:]
                uname=input("User Name : ")
                df.index= df.uname
                print(df.loc[uname,:])
            elif ch2==2:
                feild=input("Website name : ")
                uname=input("User Name : ")
                password=stdiomask.getpass("New Password : ")
                df=dtf[dtf.feild==feild]
                ind=df.index[df.uname==uname]
                dtf.iloc[ind]=[feild,uname,password]
                cursor.execute("drop table pass_list;")
                dtf.to_sql(con=conn,name="pass_list",index=False)
                print("Updated Successfully.")
            elif ch2==3:
                sys.exit()
            else:
                continue
    elif choice==2:
        feild=input("Website name : ")
        uname=input("User Name : ")
        password=stdiomask.getpass("Password : ")
        record=pd.Series([feild,uname,password],index=dtf.columns)
        dtf=dtf.append(record,ignore_index=True)
        cursor.execute("drop table pass_list;")
        dtf.to_sql(con=conn,name="pass_list",index=False)
        print(dtf)
    elif choice==3:
        while True:
            password=pass_gen()
            print("\n",password)
            print("\n1.Save this password.\n2.Generate New Password.\n3.Exit")
            ch1=int(input("Enter your Choice : "))
            if ch1==1:
                feild=input("Website name : ")
                uname=input("User Name : ")
                record=pd.Series([feild,uname,password],index=dtf.columns)
                dtf=dtf.append(record,ignore_index=True)
                cursor.execute("drop table pass_list;")
                dtf.to_sql(con=conn,name="pass_list",index=False)
                break
            elif ch1==3:
                sys.exit()
            else:
                continue

    elif choice==4:
        while True:
            cur_pass=stdiomask.getpass(prompt="Enter Current Password : ")
            if cur_pass==dtf.password[0]:
                new_pass=stdiomask.getpass(prompt="Enter New Password : ")
                new_pass1=stdiomask.getpass(prompt="Confirm New Password : ")
                if new_pass1==new_pass:
                    dtf.password[0]=new_pass
                    cursor.execute("drop table pass_list;")
                    dtf.to_sql(con=conn,name="pass_list",index=False)
                    print("Password Changed Successfully!")
                    break
                else:
                    print("Password does not match,try again.")
                    continue
            else:
                print("Wrong password try again.")
                continue
    elif choice==5:
        sys.exit()
    else:
        pass
