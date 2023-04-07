# Imprt library yang digunakan
import tabulate

# Buat class Transaction
class Transaction:

    # Inisiasi variabel transaction list
    def __init__(self):
        self.transaction_list = []

    # Function Add Item
    def add_item(self):
        """
        Functon untuk menambahkan item ke transaksi
        """

        while True:
            try:
                nama_item = input("\nMasukkan nama item: ")
                jumlah_item = int(input("Masukkan jumlah item yang ingin dibeli: "))
                harga_item = float(input("Masukkan harga per item: "))

                if jumlah_item <= 0 or harga_item <= 0:
                    raise ValueError()
                
                if len(nama_item) == 0:
                    raise ValueError()

                self.transaction_list.append({
                    'nama_item': nama_item, 
                    'jumlah_item': jumlah_item, 
                    'harga_item': harga_item
                    })

                print(f"\nBerhasil menambahkan item {nama_item} sejumlah {jumlah_item} dengan harga Rp{harga_item}")

                return self.transaction_list
                
            except ValueError:
                print("Input invalid, input nama item tidak boleh kosong, input jumlah dan harga item harus berupa angka dan tidak boleh kurang dari 0")

    def update_item_name(self):
        """
        Function untuk mengubah item yang ada di transaksi
        """

        while True:
            try:
                nama_item = input("\nMasukkan nama item yang ingin diubah: ")
                nama_item_baru = input("Masukkan nama item baru: ")

                if len(nama_item) == 0 or len(nama_item_baru) == 0:
                    raise ValueError()

                for item in self.transaction_list:
                    if item['nama_item'] == nama_item:
                        item['nama_item'] = nama_item_baru

                        print(f"\nBerhasil mengubah nama item {nama_item} menjadi {nama_item_baru}")

                        return self.transaction_list
                    
                    else:
                        raise NameError()
            
            except ValueError:
                print("Input invalid, input nama item tidak boleh kosong")
            
            except NameError:
                print("Input invalid, nama item yang di input tidak ada di daftar transaksi")

    def update_item_qty(self):
        """
        Function untuk mengubah jumlah item yang ada di transaksi
        """

        while True:
            try:
                nama_item = input("\nMasukkan nama item yang ingin diubah: ")
                jumlah_item = input("Masukkan jumlah item: ")

                if len(nama_item) == 0 or jumlah_item <= 0:
                    raise ValueError()

                for item in self.transaction_list:
                    if item['nama_item'] == nama_item:
                        item['jumlah_item'] = jumlah_item

                        print(f"\nBerhasil mengubah jumlah item {nama_item} menjadi {jumlah_item}")

                        return self.transaction_list
                    
                    else:
                        raise NameError()
            
            except ValueError:
                print("Input invalid, input nama item tidak boleh kosong")
            
            except NameError:
                print("Input invalid, nama item yang di input tidak ada di daftar transaksi")










