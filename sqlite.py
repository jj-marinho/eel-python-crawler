import sqlite3
from sqlite3 import Error


def create_connection(db_file):
	""" create a database connection to a SQLite database """
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
	return conn

 

#Create table
def create_table(conn):
	query = ("""
CREATE TABLE IF NOT EXISTS valores_liga (
							id INTEGER PRIMARY KEY,
							created_at TEXT DEFAULT (datetime('now', 'localtime')),
							card_name TEXT,
							store_name TEXT,
							edition TEXT,
							card_quality TEXT,
							price INTEGER);
	""")
	try:
		cur = conn.cursor()
		cur.execute(query)
	except Error as e:
		print(e)
	conn.commit()


#Insert values into table
def insert_values(conn, table):
	cur = conn.cursor()
	del_query = """ DELETE FROM valores_liga where card_name = ?"""
	query 		= """ INSERT INTO valores_liga (card_name, store_name, edition, card_quality, price)
									VALUES (?, ?, ?, ?, ?)	"""
	cur.execute(del_query, (table[0]['card_name'],))
	for row in table:
		row =  [row['card_name'], row['store_name'], row['edition'], row['card_quality'],  row['crypto_values']]
		cur.execute(query, row)
	conn.commit()


#query database
def show_data(conn):
	cur = conn.cursor()
	query = '''SELECT * FROM valores_liga'''
	cur.execute(query)
	rows = cur.fetchall()
	for row in rows:
		print(row)

def delete_table(conn):
	cur = conn.cursor()
	query = """DROP TABLE valores_liga"""
	cur.execute(query)	




conn = create_connection('valores.db')
# if conn is not None:
# 		create_table(conn)
# else:
# 		print("Error! cannot create the database connection.")
# insert_values(conn, 0)
# show_data(conn)
# delete_table(conn)


