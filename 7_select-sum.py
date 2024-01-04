import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()

# Menjalankan query SUM
cursor.execute("SELECT SUM(JUMLAH_SAAT_INI) FROM HEWAN")
total_jumlah = cursor.fetchone()[0]

print(f"Total populasi hewan langka saat ini: {total_jumlah}")

# Menutup koneksi
conn.close()
