#1.Create Database dan Tabel

import sqlite3

# buat connection db
cursor = sqlite3.connect('database_hewan.db')

# create table baru
cursor.execute('''
                CREATE TABLE HEWAN(
                  ID_HEWAN INT AUTO_INCREMENT PRIMARY KEY,
                  NAMA_HEWAN VARCHAR(50),
                  JENIS VARCHAR(50),
                  ASAL VARCHAR(50),
                  JUMLAH_SAAT_INI INTEGER(10),
                  TAHUN_TERAKHIR_DITEMUKAN INTEGER(10)
                )
                ''')

#break
cursor.close()