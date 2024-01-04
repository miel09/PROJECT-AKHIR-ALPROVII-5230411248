# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;
import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()

# Data yang ingin diubah
jml_sekrng = 900
id_hewan = 1

# Menjalankan query UPDATE
cursor.execute(f"UPDATE HEWAN SET JUMLAH_SAAT_INI = {jml_sekrng} WHERE ID_HEWAN = {id_hewan}")
conn.commit()

# Menampilkan pesan setelah update berhasil
if cursor.rowcount > 0:
    print(f"Data pegawai dengan ID {id_hewan} berhasil diupdate.")
else:
    print(f"Tidak ada data pegawai dengan ID {id_hewan}.")

# Menutup koneksi
conn.close()
