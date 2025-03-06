class Mahasiswa:
    def __init__(self, nama, nim, prodi, angkatan):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.angkatan = angkatan

    def praktikum(self):
        return f"{self.nama} sedang mengikuti praktikum."

    def berorganisasi(self):
        return f"{self.nama} aktif dalam kegiatan organisasi."

    def mengerjakan_tugas(self):
        return f"{self.nama} sedang mengerjakan tugas."

# Membuat dua objek Mahasiswa
mahasiswa1 = Mahasiswa("ahmad", "12345678", "Informatika", 2022)
mahasiswa2 = Mahasiswa("zaki", "87654321", "Sistem Informasi", 2021)

# Memanggil metode untuk mahasiswa1
print(mahasiswa1.praktikum())
print(mahasiswa1.berorganisasi())
print(mahasiswa1.mengerjakan_tugas())

# Memanggil metode untuk mahasiswa2
print(mahasiswa2.praktikum())
print(mahasiswa2.berorganisasi())
print(mahasiswa2.mengerjakan_tugas())