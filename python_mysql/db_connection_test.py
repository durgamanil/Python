import pymysql

conn=pymysql.connect(host="localhost",user="root",password="",db="my_python")
mycursor=conn.cursor()
print("\nPlease enter your choice\n")
#print
choice=int(input("1.add\n2.show\n3.show all\n"))
if choice==1:
    #id_no=int(input("enter id"))
    name1=input("entername")
    #mycursor.execute("INSERT INTO names(id,name) VALUES(4,'premsir');")
    mycursor.execute("INSERT INTO names(id,name) VALUES(5,'name1');")
    print("->data inserted")
elif choice ==2 :
    mycursor.execute("SELECT * FROM names")
    row = mycursor.fetchone()
    while row is not None:
        print(row)
        row = mycursor.fetchone()
else:
    mycursor.execute("SELECT * FROM names")
    rows = mycursor.fetchall()
    print('Total Row(s):', mycursor.rowcount)
    for row in rows:
        print(row)

conn.commit()
conn.close()


