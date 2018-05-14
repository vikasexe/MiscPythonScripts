import os
import cx_Oracle
import csv
 
SQL="select * from customer_node_type"
 
# Network drive somewhere
filename="Output.csv"
FILE=open(filename,"w");
output=csv.writer(FILE, dialect='excel')
 
# You can set these in system variables but just in case you didnt
conn_str = 'vsahu/intec09@svdbconeude02.co.csgsystems.com:1521/CB1DEV2B.co.csgsystems.com'
conn = cx_Oracle.connect(conn_str)
cursor = conn.cursor()
cursor.execute(SQL)
for row in cursor:
    output.writerow(row)
cursor.close()
connection.close()
FILE.close()