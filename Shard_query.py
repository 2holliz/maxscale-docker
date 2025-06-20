# shard_query.py
# Name: Mustafa Alghuraibawi
# Email: aliayad20135@gmail.com
# Date: 06/20/2025
# Class: Database Sharding Project
# Description: Connects to MaxScale ReadWriteSplit router and runs sample queries on the sharded database.

import pymysql

# Connect to MaxScale router (ReadWriteSplit-router on port 4006)
db = pymysql.connect(
    host="127.0.0.1",  # localhost
    port=4006,         # MaxScale router port
    user="maxuser",
    passwd="maxpwd",
    database="zipcodes_one"  # You can choose one logical DB or omit to query fully qualified names
)

cursor = db.cursor()

print("Largest zipcode in zipcodes_one:")
cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1;")
print(cursor.fetchone())

print("\nAll zipcodes where state=KY:")
cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE State='KY';")
for row in cursor.fetchall():
    print(row)

print("\nAll zipcodes between 40000 and 41000:")
cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE Zipcode BETWEEN 40000 AND 41000;")
for row in cursor.fetchall():
    print(row)

print("\nTotalWages where state=PA:")
cursor.execute("SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE State='PA';")
for row in cursor.fetchall():
    print(row)

db.close()
