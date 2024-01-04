import sqlite3

koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()
kursor.execute("SELECT * FROM HEWAN WHERE JUMLAH_SAAT_INI <= '1000'")
rows = kursor.fetchall()

print("Data Hewan:")
print("===================================================================================================")
print("{:<10} {:<20} {:<10} {:<10} {:<20} {:<20}".format("ID HEWAN", "NAMA HEWAN", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN TERAKHIR DITEMUKAN"))
print("---------------------------------------------------------------------------------------------------")
for row in rows:
    print("{:<10} {:<20} {:<10} {:<10} {:<20} {:<20}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
    
koneksi.close()
