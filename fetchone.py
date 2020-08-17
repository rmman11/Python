#!/usr/bin/python
#The fetchone() method will return the first row of the result

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  db ="python",
  password=""
)

mycursor = mydb.cursor()

#imi afiseaza din baza de date o coloana mysql cu python
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)

mydb.close()


#https://www.w3schools.com/python/python_mysql_join.asp