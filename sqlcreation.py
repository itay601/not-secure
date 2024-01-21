import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "linoy13301",
    database="user_client"
)

mycursor=mydb.cursor()

#primary_key=True syntex check
#mycursor.execute("CREATE TABLE user (email VARCHAR(100), first_name VARCHAR(100),password VARCHAR(255))")
#mycursor.execute("CREATE TABLE client (id INTEGER(10),email VARCHAR(100), first_name VARCHAR(100),phone VARCHAR(20))")


sqlFormula = "INSERT INTO user(email,first_name,password) VALUES (%s,%s,%s)"
#validation (sql param) -corrent vunrable version -
client1=("rachel@gamil.com","Rachel", 22345436)

mycursor.execute(sqlFormula, client1)

#to commit the changes or else no changes whould be saved in the db
mydb.commit()
