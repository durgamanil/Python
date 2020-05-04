import pymysql

conn=pymysql.connect(host="localhost",user="root",password="",db="sslabs")
mycursor=conn.cursor()

print("\nPlease enter your choice\n")
#print
#while True:
choice=int(input("1.add\n2.show\n3.show all\n"))
if choice==1:  
    mycursor.execute("INSERT INTO `users`(`id`, `name`, `age`, `reg_date`) VALUES (null,'omkar','30',null);")
    conn.commit()
    #print(xyz)
elif choice ==2 :
    mycursor.execute("SELECT * FROM users")
   
    row = mycursor.fetchone()
    
    while row is not None:
        print(row)
        row = mycursor.fetchone()
else:
    mycursor.execute("SELECT * FROM users")
    rows = mycursor.fetchall()
    print('Total Row(s):', mycursor.rowcount)
    for row in rows:
        print(row)

#conn.commit()
conn.close()


