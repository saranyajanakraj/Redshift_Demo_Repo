import sys
#import psycopg2
import redshift_connector

conn = redshift_connector.connect(
        host="redshift-democluster.cjtsvnr1c5fa.ap-south-1.redshift.amazonaws.com",
        database="dev",
        user="awsuser",
        password="Admin123")
cur = conn.cursor()
cur.execute(open("/tmp/select.sql","r").read())
conn.commit()
rows = cur.fetchall()
print(rows)

conn.close()

