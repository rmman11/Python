#!/usr/bin/python

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  db ="python",
  password=""
)

mycursor = mydb.cursor()

#imi afiseaza din baza de date mysql cu python
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)