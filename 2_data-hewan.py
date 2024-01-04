#2. INSERT INTO

import sqlite3
conn = sqlite3.connect('database_hewan.db')

# QUERY INSERT data ke dalam tabel PEGAWAI
conn.execute("INSERT INTO HEWAN (ID_HEWAN, NAMA_HEWAN, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN) VALUES (1, 'Orangutan', 'Mamalia', 'Sumatera', 14000, 2021)")
conn.execute("INSERT INTO HEWAN (ID_HEWAN, NAMA_HEWAN, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN) VALUES (2, 'Harimau Sumatera', 'Mamalia', 'Sumatera', 400, 2020)")
conn.execute("INSERT INTO HEWAN (ID_HEWAN, NAMA_HEWAN, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN) VALUES (3, 'Komodo', 'Reptil', 'Nusa Tenggara', 3000, 2019)")
conn.execute("INSERT INTO HEWAN (ID_HEWAN, NAMA_HEWAN, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN) VALUES (4, 'Anoa', 'Mamalia', 'Sulawesi', 5000, 2022)")
conn.execute("INSERT INTO HEWAN (ID_HEWAN, NAMA_HEWAN, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN) VALUES (5, 'Badak Jawa', 'Mamalia', 'Jawa', 72, 2021)")
conn.execute("INSERT INTO HEWAN (ID_HEWAN, NAMA_HEWAN, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN) VALUES (6, 'Kuskus', 'Mamalia', 'Papua', 50, 2020)")
conn.execute("INSERT INTO HEWAN (ID_HEWAN, NAMA_HEWAN, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN) VALUES (7, 'Trenggiling', 'Mamalia', 'Sumatera', 90, 2022)")
conn.execute("INSERT INTO HEWAN (ID_HEWAN, NAMA_HEWAN, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN) VALUES (8, 'Burung Cenderawasih', 'Burung', 'Papua', 45, 2021)")
conn.execute("INSERT INTO HEWAN (ID_HEWAN, NAMA_HEWAN, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN) VALUES (9, 'Penyu Hijau', 'Reptil', 'Nusa Tenggara Timur', 20, 2022)")
conn.execute("INSERT INTO HEWAN (ID_HEWAN, NAMA_HEWAN, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN) VALUES (10, 'Gajah Sumatera', 'Mamalia', 'Sumatera', 2500, 2023)")
conn.commit()

conn.close()