class Pasien:
    def __init__(self, nama, waktu_janji):
        self.nama = nama
        self.waktu_janji = waktu_janji

class Antrian:
    def __init__(self):
        self.pasien = []

    def tambah_pasien(self, pasien):
        self.pasien.append(pasien)
        print(f"Menambahkan pasien {pasien.nama} ke antrian.")

    def layani_pasien(self):
        if self.pasien:
            pasien = self.pasien.pop(0)
            print(f"Layani pasien {pasien.nama} pada {pasien.waktu_janji}.")
        else:
            print("Tidak ada pasien dalam antrian.")

    def tampilkan_antrian(self):
        if self.pasien:
            print("Antrian saat ini:")
            for i, pasien in enumerate(self.pasien, start=1):
                print(f"{i}. {pasien.nama} - {pasien.waktu_janji}")
        else:
            print("Antrian kosong.")

# Contoh penggunaan
antrian_klinik = Antrian()
antrian_klinik.tambah_pasien(Pasien("Ghina kimberly", "10:00 AM"))
antrian_klinik.tambah_pasien(Pasien("Zayn Malik", "10:30 AM"))
antrian_klinik.tampilkan_antrian()
antrian_klinik.layani_pasien()
antrian_klinik.tampilkan_antrian()
