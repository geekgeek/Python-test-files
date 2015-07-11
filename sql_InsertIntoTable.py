
#http://www.tutorialspoint.com/python/python_database_access.htm

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO table1(id,name) VALUES (10, 'name10')"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
   print"success"
except:
   # Rollback in case there is any error
   db.rollback()
   print "error"

# disconnect from server
db.close()
