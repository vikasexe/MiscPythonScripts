import cx_Oracle
#from prettytable import from_db_cursor
import HTML

conn_str = 'vsahu/intec09@svdbconeude02.co.csgsystems.com:1521/CB1DEV2B.co.csgsystems.com'
conn = cx_Oracle.connect(conn_str)
c = conn.cursor()
c.execute('select * from customer_node_type')

x = from_db_cursor(c) 
    
#print(x)
#print(x.get_html_string())
#for row in c:
#    print(row[0], "-", row[1])
htmlcode = HTML.table(c)
print (htmlcode)
conn.close()