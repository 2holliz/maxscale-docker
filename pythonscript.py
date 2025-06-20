# Name: Mustafa Alghuraibawi
# Email: aliayad20135@gmail.com
# Date: 06/20/2025
# Class: CNE370 Intro into Virtualization
# This Python script connects to a MaxScale sharding router, runs queries on 
# sharded zipcode tables, and prints the results to the console.

import pymysql

# Connect to MaxScale
db = pymysql.connect(host="192.168.1.20", port=4000, user="maxuser", passwd="maxpwd")
cursor = db.cursor()

# 1. Largest zipcode in zipcodes_one
print("\nLargest zipcode in zipcodes_one:")
cursor.execute("SELECT MAX(Zipcode) FROM zipcodes_one.zipcodes_one;")
for result in cursor.fetchall():
    print(result)

# 2. All zipcodes where state='KY'
print("\nAll zipcodes where State='KY':")
cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE State='KY';")
for result in cursor.fetchall():
    print(result)

# 3. All zipcodes between 40000 and 41000
print("\nAll zipcodes between 40000 and 41000:")
cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE Zipcode BETWEEN 40000 AND 41000;")
for result in cursor.fetchall():
    print(result)

# 4. TotalWages where state='PA'
print("\nTotalWages where State='PA':")
cursor.execute("SELECT TotalWages FROM zipcodes_two.zipcodes_two WHERE State='PA';")
for result in cursor.fetchall():
    print(result)

# Close connection
db.close()
