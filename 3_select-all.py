#3. SELECT ALL
import sqlite3

conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM HEWAN")
rows = cursor.fetchall()

print("Data Hewan:")
print("=============================================================================================================")
print("{:<10} {:<20} {:<10} {:<20} {:<20} {:<20}".format("ID HEWAN", "NAMA HEWAN", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN TERAKHIR DITEMUKAN"))
print("-------------------------------------------------------------------------------------------------------------")
for row in rows:
    print("{:<10} {:<20} {:<10} {:<20} {:<20} {:<20}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
 
conn.close()