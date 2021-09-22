import mysql.connector 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "#Lumia530",
    database="movie")
mycursor = mydb.cursor()
query ="select * from movies  where movie_name ='RACE'"
mycursor.execute(query)
k = mycursor.fetchall()
for k in k :
	print(k, '\n')




b = "select * from movies"
mycursor.execute(b)

u =mycursor.fetchall()
for u in u :
	print(u)








