#Create user and grant privileges at root admin
#user name: kora
#using localhost
#password: 1234
CREATE USER "kora"@"localhost" IDENTIFIED BY "1234"

#create a database
CREATE DATABASE stockDB;

#grant privileges to user "kora"
grant all privileges on stockDB.* to "kora"@"localhost" IDENTIFIED BY "1234";

#login as "kora"
#change database to stockDB
USE stockDB

#create tables...

CREATE TABLE Real_Time_Data(
	rid INT UNSIGNED AUTO_INCREMENT NOT NULL,
	symbol VARCHAR(4) NOT NULL,
	stock_time DATETIME,
	price FLOAT,
	volume INT,
	PRIMARY KEY(rid)
	REFERENCES stock(symbol)
		ON DELETE CASCADE
	);

CREATE TABLE History_Time_Data(
	hid INT UNSIGNED AUTO_INCREMENT NOT NULL,
	symbol VARCHAR(4) NOT NULL,
	stock_date DATE,
	open_price FLOAT,
	high_price FLOAT,
	low_price FLOAT,
	close_price FLOAT,
	adj_close FLOAT,
	volume INT,
	PRIMARY KEY(hid)
	REFERENCES stock(symbol)
		ON DELETE CASCADE
	);
