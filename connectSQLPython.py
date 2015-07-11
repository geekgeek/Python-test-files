
#Install mysql driver from link below:
#http://sourceforge.net/projects/mysql-python/?source=typ_redirect
#Install wampserver

import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="", # your password
                      db="test") # name of the data base


#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM table1")

# print all the first and second cell of all the rows
for row in cur.fetchall() :
    print row[0],row[1]
