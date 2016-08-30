import psycopg2

conn = psycopg2.connect('postgresql://cthoyt:@localhost:5432/postgres')

cur = conn.cursor()

cur.execute("select * from wk.documents")

for row in cur.fetchall():
	print(row)

cur.close()
conn.close()
