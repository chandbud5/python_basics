import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="mydatabase")  #connect to your database

mycur = mydb.cursor()   #define cursor
mycur.execute("select * from person;")  #mention your query here

result = mycur.fetchall()   #Specify how many entries you want fetchall/fetchone
for i in result:
    print(i)