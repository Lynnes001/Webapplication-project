import MySQLdb

def dbInsertStock(sy):
	#database connection
	db = MySQLdb.connect("localhost", "kora", "1234", "stockDB")
	cursor = db.cursor()
	#define sql
	sql = """INSERT INTO stock(symbol) VALUES(sy)"""
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()

def dbInsertRealTime(list):
	'''
	list = [rid, symbol, price, stock_date, stock_time, volume]
	'''
	#database connection
	db = MySQLdb.connect("localhost", "kora", "1234", "stockDB")
	cursor = db.cursor()
	#define sql
	sql = """INSERT INTO Real_Time_Data(rid, symbol, price, stock_date, stock_time, volume) 
			VALUES(list[0], list[1], list[2], list[3], list[4], list[5])"""
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()

def dbInsertHistoryTime(list):
	'''
	list = [hid, symbol, stock_date, open_pri, high_pri, low_pri, close_pri, adj_close, volume ]
	'''
	#database connection
	db = MySQLdb.connect("localhost", "kora", "1234", "stockDB")
	cursor = db.cursor()
	#define sql
	sql = """INSERT INTO Real_Time_Data(hid, symbol, stock_date, open_price, high_price, low_price, close_price, adj_close, volume) 
			VALUES(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8])"""
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()

def dbselect(tablename):
	#database connection
	db = MySQLdb.connect("localhost", "kora", "1234", "stockDB")
	cursor = db.cursor()
	IF tablename == 'stock':
		sql = """SELECT * FROM stock"""
	ELSE IF tablename == 'Real_Time_Data':
		sql = """SELECT * FROM Real_Time_Data"""
	ELSE IF tablename == 'History_Time_Data':
		sql = """SELECT * FROM History_Time_Data"""
	ELSE:
		return
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()


