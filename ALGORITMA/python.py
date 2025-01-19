# Daftar untuk menyimpan buku, stack, dan queue
books = []
stack = []
queue = []

def add_book():
    book_id = input("Masukkan ID Buku: ")
    title = input("Masukkan Judul Buku: ")
    author = input("Masukkan Nama Pengarang: ")
    year = input("Masukkan Tahun Terbit: ")
    book = {"ID": book_id, "Title": title, "Author": author, "Year": int(year)}
    books.append(book)  # Menambahkan buku ke dalam daftar buku
    stack.append(book)  # Menambahkan buku ke dalam stack (LIFO)
    queue.append(book)  # Menambahkan buku ke dalam queue (FIFO)
    print("Buku berhasil ditambahkan.\n")

def delete_book():
    book_id = input("Masukkan ID Buku yang ingin dihapus: ")
    global books
    for book in books:
        if book['ID'] == book_id:
            books.remove(book)  # Menghapus dari daftar buku
            if book in stack:
                stack.remove(book)  # Menghapus dari stack
            if book in queue:
                queue.remove(book)  # Menghapus dari queue
            print("Buku berhasil dihapus.\n")
            return
    print("Buku tidak ditemukan.\n")

def update_book():
    book_id = input("Masukkan ID Buku yang ingin diupdate: ")
    for book in books:
        if book['ID'] == book_id:
            new_title = input("Masukkan Judul Baru: ")
            new_author = input("Masukkan Nama Pengarang Baru: ")
            new_year = input("Masukkan Tahun Terbit Baru: ")
            book['Title'] = new_title
            book['Author'] = new_author
            book['Year'] = int(new_year)
            print("Buku berhasil diupdate.\n")
            return
    print("Buku tidak ditemukan.\n")

def recursive_search(data, target, index=0):
    if index >= len(data):
        return None
    if target.lower() in data[index]['Title'].lower():
        return data[index]
    return recursive_search(data, target, index + 1)

def search_book_recursive():
    target = input("Masukkan Judul Buku yang ingin dicari: ")
    result = recursive_search(books, target)
    if result:
        print(f"\nBuku Ditemukan: {result}\n")
    else:
        print("Buku tidak ditemukan.\n")

def display_books():
    if not books:
        print("Tidak ada buku yang tersedia.\n")
        return
    print("\nDaftar Semua Buku:")
    for book in books:
        print(f"{book['ID']} - {book['Title']} oleh {book['Author']} ({book['Year']})")
    print()

def sort_books_by_year():
    global books
    books.sort(key=lambda x: x['Year'])
    print("Buku berhasil diurutkan berdasarkan tahun.\n")

def display_stack():
    if not stack:
        print("Stack kosong.\n")
        return
    print("\nBuku dalam Stack (LIFO):")
    for book in reversed(stack):
        print(f"{book['ID']} - {book['Title']} ({book['Year']})")
    print()

def display_queue():
    if not queue:
        print("Queue kosong.\n")
        return
    print("\nBuku dalam Queue (FIFO):")
    for book in queue:
        print(f"{book['ID']} - {book['Title']} ({book['Year']})")
    print()

def main_menu():
    while True:
        print("=== Sistem Manajemen Buku ===")
        print("1. Tambah Buku")
        print("2. Tampilkan Semua Buku")
        print("3. Update Buku")
        print("4. Hapus Buku")
        print("5. Urutkan Buku Berdasarkan Tahun")
        print("6. Cari Buku (Rekursi)")
        print("7. Tampilkan Buku di Stack (LIFO)")
        print("8. Tampilkan Buku di Queue (FIFO)")
        print("9. Keluar")
        choice = input("Pilih menu (1-9): ")
        print()
        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            sort_books_by_year()
        elif choice == "6":
            search_book_recursive()
        elif choice == "7":
            display_stack()
        elif choice == "8":
            display