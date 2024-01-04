import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

# Menjalankan query SELECT dengan ORDER BY
# OR cukup salah satu terpenuhi maka dapat dieksekusi
kursor.execute(f"SELECT * FROM HEWAN WHERE ASAL = 'Sumatera' OR JUMLAH_SAAT_INI > '500'")
rows = kursor.fetchall()

print("Data Hewan:")
print("===================================================================================================")
print("{:<10} {:<20} {:<10} {:<10} {:<20} {:<20}".format("ID HEWAN", "NAMA HEWAN", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN TERAKHIR DITEMUKAN"))
print("---------------------------------------------------------------------------------------------------")
for row in rows:
    print("{:<10} {:<20} {:<10} {:<10} {:<20} {:<20}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
    
    
koneksi.close()