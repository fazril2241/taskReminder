 📋 TaskReminder APPLICATION

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square)
![License](http://www.apache.org/licenses/)

Aplikasi TaskReminder sederhana berbasis Python yang memungkinkan pengguna untuk mengelola tugas sehari-hari dengan mudah. Program ini menyimpan data tugas ke file eksternal sehingga data tetap tersimpan meskipun program ditutup.

🌟 Fitur Utama

- Tambah Tugas: Memasukkan tugas baru dengan nama, keterangan, deadline, dan status
- Cek Reminder: Mendapatkan notifikasi otomatis untuk tugas yang deadline-nya besok (H-1) atau hari ini (Hari H)
- Update Status: Mengubah status tugas antara "selesai" dan "belum"
- Tampilkan Daftar: Melihat semua tugas yang tersimpan dalam format terstruktur
- Hapus Tugas: Menghapus tugas yang sudah tidak diperlukan
- Data Persistence: Data tugas tersimpan otomatis ke file sehingga tidak hilang saat program ditutup

 🛠️ Persyaratan

- Python 3.7 atau lebih baru
- Tidak memerlukan library tambahan (hanya menggunakan library standar Python)

 📂 Struktur File

```
to-do-list/
├── todolist            File penyimpanan data tugas (akan dibuat otomatis)
├── program.py          File kode program utama
└── README.md           Dokumentasi ini
```

 🚀 Cara Menjalankan

1. Clone atau download repository:
   ```bash
   git clone https://github.com/fazril2241/taskReminder.git
   cd taskReminder
   ```

2. Jalankan program:
   ```bash
   python taskReminder.git
   or
   py taskReminder.git
   ```

3. Atau jika menggunakan file yang sudah ada, cukup jalankan file Python yang berisi kode program.

 🎯 Penggunaan Dasar

 Menu Utama
Setelah program dijalankan, Anda akan melihat menu utama:

```
-------------------------
     TO DO LIST      
-------------------------

--- MENU ---
1. Tambah tugas
2. Cek reminder
3. Update status
4. Tampilkan to-do list
5. Hapus tugas
6. Keluar

Pilih menu (1-6):
```

 1. Tambah Tugas (Menu 1)
```
=== TAMBAH TUGAS BARU ===
Nama tugas: Belajar Python
Keterangan: Mengerjakan latihan coding
Deadline (DD-MM-YYYY): 15-12-2024
Status (selesai/belum): belum

Tugas: Belajar Python
Deadline: 15-12-2024
Simpan? (yes/no): yes
Tugas berhasil ditambahkan!
Data berhasil disimpan!
```

 2. Cek Reminder (Menu 2)
```
=== CEK REMINDER ===
Hari ini: 14-12-2024

REMINDER H-1: Belajar Python
Deadline besok, segera kerjakan!
Deadline: 15-12-2024
```

 3. Update Status (Menu 3)
```
=== UPDATE STATUS TUGAS ===
1. Belajar Python - belum

Pilih nomor tugas: 1
Status baru (selesai/belum): selesai
Status berhasil diupdate!
Data berhasil disimpan!
```

 4. Tampilkan To-Do List (Menu 4)
```
=== TO-DO LIST ===

1. Belajar Python
   Keterangan: Mengerjakan latihan coding
   Deadline: 15-12-2024
   Status: selesai
```

 5. Hapus Tugas (Menu 5)
```
=== HAPUS TUGAS ===
1. Belajar Python

Pilih nomor tugas: 1
Hapus 'Belajar Python'? (yes/no): yes
Tugas berhasil dihapus!
Data berhasil disimpan!
```

 💡 Tips Penggunaan

- Format Deadline: Selalu gunakan format `DD-MM-YYYY` (contoh: `15-12-2024`)
- Status Tugas: Hanya gunakan `selesai` atau `belum` untuk status tugas
- Konfirmasi: Selalu periksa kembali data sebelum mengkonfirmasi penyimpanan
- File Data: File `todolist` akan dibuat otomatis saat Anda menambahkan tugas pertama

 ⚠️ Catatan Penting

- Program ini case-sensitive untuk input konfirmasi (`yes`/`no`)
- Pastikan format tanggal deadline benar untuk mendapatkan reminder yang akurat
- Data akan otomatis tersimpan setelah setiap operasi tambah, update, atau hapus tugas
- Jika file `todolist` tidak ada, program akan membuat file baru saat Anda menambahkan tugas pertama

 🤝 Kontribusi

Jika Anda ingin berkontribusi atau melaporkan bug, silakan buat issue atau pull request di repository ini.

 📄 Lisensi

Program ini dilisensikan di bawah [Apache License](LICENSE).

---

Dibuat dengan ❤️ untuk memudahkan manajemen tugas sehari-hari  
© 2024 Tim Pengembang C8
