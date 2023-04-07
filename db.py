""""
Buat koneksi ke database
"""

# Import create_engine dan text dari sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text

# Membuat engine
# Konfigurasi koneksi ke database sqlite
engine = create_engine('sqlite:///self_service_cashier.db')

# Buat koneksi
conn = engine.connect()

# Query SQL untuk membuat table
query = text(
    """
    CREATE TABLE cashier(
        
    )
    """
)