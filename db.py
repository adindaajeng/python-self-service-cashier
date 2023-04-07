""""
Membuat koneksi ke database
"""

# Import create_engine dan text dari sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text

# Membuat engine
# Konfigurasi koneksi ke database sqlite
engine = create_engine('sqlite:///db_cashier.db')

# Buat koneksi ke database
conn = engine.connect()

# Query SQL untuk membuat table
query = text(
    """
    CREATE TABLE IF NOT EXISTS transaction (
        no_id INT PRIMARY KEY,
        nama_item VARCHAR(100) NOT NULL,
        jumlah_item INT NOT NULL,
        harga REAL NOT NULL,
        total_harga REAL,
        diskon REAL,
        harga_diskon REAL
    )
    """
)

# Mengeksekusi query
conn.execute(query)

# Menutup koneksi ke database
conn.close()