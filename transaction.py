# Imprt library yang digunakan
from tabulate import tabulate

# Buat class Transaction
class Transaction:

    # Inisiasi variabel transaction list
    def __init__(self):
        self.transaction_list = []

# ==============================================
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

                print(f"\nBerhasil menambahkan item {nama_item} sejumlah {jumlah_item} dengan harga Rp{harga_item}\n")

                return self.transaction_list
                
            except ValueError:
                print("Input invalid, input nama item tidak boleh kosong, input jumlah dan harga item harus berupa angka dan tidak boleh kurang dari 0")

# ==============================================
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

                        print(f"\nBerhasil mengubah nama item {nama_item} menjadi {nama_item_baru}\n")

                        return self.transaction_list
                    
                    else:
                        raise NameError()
            
            except ValueError:
                print("Input invalid, input nama item tidak boleh kosong")
            
            except NameError:
                print("Input invalid, nama item yang di input tidak ada di daftar transaksi")

# ==============================================
    def update_item_qty(self):
        """
        Function untuk mengubah jumlah item yang ada di transaksi
        """

        while True:
            try:
                nama_item = input("\nMasukkan nama item yang ingin diubah: ")
                jumlah_item = int(input("Masukkan jumlah item: "))

                if len(nama_item) == 0 or jumlah_item <= 0:
                    raise ValueError()

                for item in self.transaction_list:
                    if item['nama_item'] == nama_item:
                        item['jumlah_item'] = jumlah_item

                        print(f"\nBerhasil mengubah jumlah item {nama_item} menjadi {jumlah_item}\n")
                        print(self.transaction_list)

                        return self.transaction_list
                    
                    else:
                        raise NameError()
            
            except ValueError:
                print("Input invalid, input nama item tidak boleh kosong")
            
            except NameError:
                print("Input invalid, nama item yang di input tidak ada di daftar transaksi")

# ==============================================
    def update_item_price(self):
        """
        Function untuk mengubah harga item yang ada di transaksi
        """

        while True:
            try:
                nama_item = input("\nMasukkan nama item yang ingin diubah: ")
                harga_item = int(input("Masukkan harga item: "))

                if len(nama_item) == 0 or harga_item <= 0:
                    raise ValueError()

                for item in self.transaction_list:
                    if item['nama_item'] == nama_item:
                        item['harga_item'] = harga_item

                        print(f"\nBerhasil mengubah harga item {nama_item} menjadi {harga_item}\n")

                        return self.transaction_list
                    
                    else:
                        raise NameError()
            
            except ValueError:
                print("Input invalid, input nama item tidak boleh kosong")
            
            except NameError:
                print("Input invalid, nama item yang di input tidak ada di daftar transaksi")

# ==============================================
    def delete_item(self):
        """
        Function untuk menghapus item yang ada di transaksi
        """

        while True:
            try:
                nama_item = input("\nMasukkan nama item yang ingin dihapus: ")
                
                if len(nama_item) == 0:
                    raise ValueError()

                for i in range(len(self.transaction_list)-1):
                    item = self.transaction_list[i]
                    if item['nama_item'] == nama_item:
                        del self.transaction_list[item]

                        print(f"\nBerhasil menghapus item {nama_item}\n")
                        print(self.transaction_list)

                        return self.transaction_list

                    else: 
                        raise NameError()

            except ValueError:
                print("Input invalid, input nama item tidak boleh kosong")
            
            except NameError:
                print("Input invalid, nama item yang di input tidak ada di daftar transaksi")

# ==============================================
    def reset_transaction(self):
        """
        Function untuk menghapus semua item yang ada di transaksi
        """

        try:
            self.transaction_list.clear()

            print("\nBerhasil menghapus semua item dalam transaksi\n")

            return self.transaction_list

        except ValueError:
            print("Invalid input")

# ==============================================
    def calculate_sum(self):
        """
        Function untuk menghitung jumlah total transaksi
        """

        try:
            total = 0

            for item in self.transaction_list:
                jumlah_item = item['jumlah_item']
                harga_item = item['harga_item']

                total_per_item = jumlah_item * harga_item
                item['total'] = total_per_item

                total += total_per_item

            print(self.transaction_list)
            return self.transaction_list

        except ValueError:
            print("Invalid data, mohon cek kembali order anda")

# ==============================================
    def check_order(self):
        """
        Function untuk menampilkan tabel list transaksi
        """

        try:
            table = []

            for item in self.transaction_list:
                nama_item = item['nama_item']
                jumlah_item = int(item["jumlah_item"])
                harga_item = float(item["harga_item"])
                total = jumlah_item * harga_item
                table.append([nama_item, jumlah_item, harga_item, total])

            headers = ["Nama Item", "Jumlah Item", "Harga Item", "Total"]
            print("\nOrder Anda saat ini: \n")
            print(tabulate(table, headers = headers, tablefmt="grid") + "\n")

        except ValueError:
            print("Terdapat invalid data, mohon cek kembali order anda")