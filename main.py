from transaction import Transaction

# Display semua list menu
def menu():
    """
    Functon untuk menampilkan semua list menu dari self-service cashier
    """

    transaction = Transaction()

    while True:
        try:
            print("======= Selamat datang di Self-Service Cashier =======")
            print("Menu: ")
            print("1. Tambahkan item untuk dibeli")
            print("2. Update item yang akan dibeli")
            print("3. Hapus item yang akan dibeli")
            print("4. Check item yang akan dibeli")
            print("5. Checkout")

            menu = int(input("Silakan pilih dari menu di atas: "))

            if menu == 1:
                transaction.add_item()

            elif menu == 2:
                print("\nSubmenu update item: ")
                print("1. Update nama item")
                print("2. Update jumlah item")
                print("3. Update harga item")

                submenu = int(input("Silakan pilih dari submenu di atas: "))

                if submenu == 1:
                    transaction.update_item_name()
                
                else:
                    raise ValueError()

            
            else:
                raise ValueError()

        except ValueError:
            print("\nMenu invalid, silakan masukkan nomor menu sesuai dengan list\n")

menu()

