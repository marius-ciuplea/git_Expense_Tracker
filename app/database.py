import sqlite3

def connect_db(db_file='data/expenses.db'):
	conn = sqlite3.connect(db_file)
	return conn

def create_table():
	conn = connect_db()
	cursor = conn.cursor()
	cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
						(id INTEGER PRIMARY KEY, amount REAL, category TEXT, description TEXT, date TEXT )''')
	conn.commit()
	conn.close()