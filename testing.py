import mysql.connector
from datetime import datetime
from datetime import datetime, timedelta

# Replace with your RDS MySQL endpoint, username, and password
host = "organise-db.cbcelvacwhjp.us-east-1.rds.amazonaws.com"
user = "root"
password = "12345678"

# Establish the connection
connection = mysql.connector.connect(host=host, user=user, password=password,database="aws_organise")

# Create a cursor object to interact with the database
cursor = connection.cursor()

#cursor.execute("delete from events;")
#connection.commit()
cursor.execute(
    f"""
    select curdate(),curtime();

               """)

a=cursor.fetchall()
for i in a:
    t_obj = datetime.strptime( str(i[1]+timedelta(hours=15.5)), '%H:%M:%S')
    print(str(t_obj.strftime("%I:%M %p")))
    print(i[0])
print(a)
connection.commit()
# Now you're connected and ready to execute SQL queries.
