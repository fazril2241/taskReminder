from datetime import datetime

# List untuk menyimpan semua tugas yang dimasukkan user
# Struktur data: list of dictionaries dengan keys: nama, keterangan, deadline, status
daftar_tugas = []

# Fungsi untuk memuat data tugas dari file eksternal
def muat_data():
    """
    Fungsi ini bertugas untuk:
    1. Membaca data tugas dari file 'todolist'
    2. Mem-parsing data menjadi format dictionary
    3. Menambahkan data ke daftar_tugas
    4. Membuat file baru jika belum ada
    
    Logika:
    - Coba buka file untuk dibaca
    - Jika file tidak ditemukan (FileNotFoundError), buat file baru
    - Setiap baris file dipisah dengan '|' menjadi 4 komponen
    - Komponen disimpan sebagai dictionary dalam list daftar_tugas
    """
    try:
        # Membuka file 'todolist' dalam mode read (baca)
        file = open("todolist", "r")
        # Membaca setiap baris dalam file
        for baris in file:
            # Membersihkan spasi/newline di awal/akhir baris, lalu memisah dengan delimiter '|'
            data = baris.strip().split("|")
            # Membuat dictionary tugas dari data yang sudah dipisah
            tugas = {
                "nama": data[0],           # Indeks 0: nama tugas
                "keterangan": data[1],      # Indeks 1: keterangan tugas
                "deadline": data[2],        # Indeks 2: tanggal deadline
                "status": data[3]           # Indeks 3: status (selesai/belum)
            }
            # Menambahkan dictionary tugas ke list daftar_tugas
            daftar_tugas.append(tugas)
        # Menutup file setelah selesai membaca
        file.close()
        print("Data akan dimuat!!!")
    except FileNotFoundError:
        # Jika file tidak ditemukan, buat file baru dalam mode write
        file = open("todolist", "w")
        file.close()
        print("File belum ada.Tambah tugas!!!")


# Fungsi untuk menyimpan data tugas ke file eksternal
def simpan_data():
    """
    Fungsi ini bertugas untuk:
    1. Menyimpan semua data tugas dari memory ke file
    2. Menggunakan format penyimpanan: nama|keterangan|deadline|status
    
    Logika:
    - Buka file dalam mode write (akan menghapus isi lama)
    - Iterasi setiap tugas dalam daftar_tugas
    - Tulis setiap tugas dalam format terstruktur dengan delimiter '|'
    - Tutup file setelah selesai
    """
    # Membuka file 'todolist' dalam mode write (menimpa isi lama)
    file = open("todolist", "w")
    # Iterasi setiap tugas dalam daftar
    for tugas in daftar_tugas:
        # Menulis data tugas dalam format: nama|keterangan|deadline|status + newline
        file.write(f"{tugas['nama']}|{tugas['keterangan']}|{tugas['deadline']}|{tugas['status']}\n")
    # Menutup file setelah selesai menulis
    file.close()
    print("Data berhasil disimpan!")

# Fungsi untuk menambahkan tugas baru
def tambah_tugas():
    """
    Fungsi ini bertugas untuk:
    1. Mengambil input data tugas baru dari user
    2. Memberikan konfirmasi sebelum menyimpan
    3. Menambahkan tugas ke daftar dan menyimpan ke file
    
    Logika:
    - Tampilkan header menu
    - Ambil input nama, keterangan, deadline, dan status dari user
    - Tampilkan preview tugas untuk konfirmasi
    - Jika dikonfirmasi 'yes', simpan tugas ke daftar dan file
    - Jika tidak, batalkan operasi
    """
    print("\n=== TAMBAH TUGAS BARU ===")
    # Mengambil input dari user untuk setiap field tugas
    nama = input("Nama tugas: ")
    keterangan = input("Keterangan: ")
    deadline = input("Deadline (DD-MM-YYYY): ")
    status = input("Status (selesai/belum): ")
    
    # Konfirm tugas - Menampilkan preview data yang akan disimpan
    print(f"\nTugas: {nama}")
    print(f"Deadline: {deadline}")
    konfirmasi = input("Simpan? (yes/no): ")
    
    # Jika user mengkonfirmasi dengan 'yes'
    if konfirmasi == "yes":
        # Membuat dictionary untuk tugas baru
        tugas = {
            "nama": nama,
            "keterangan": keterangan,
            "deadline": deadline,
            "status": status
        }
        # Menambahkan tugas ke daftar_tugas
        daftar_tugas.append(tugas)
        print("Tugas berhasil ditambahkan!")
        # Simpan perubahan ke file
        simpan_data()
    else:
        print("Tugas dibatalkan.")

# Fungsi untuk mengecek reminder deadline
def cek_reminder():
    """
    Fungsi ini bertugas untuk:
    1. Mengecek tugas yang deadline-nya dekat (H-1 dan Hari H)
    2. Menampilkan notifikasi reminder
    
    Logika:
    - Dapatkan tanggal hari ini
    - Iterasi semua tugas dengan status 'belum'
    - Hitung selisih hari antara deadline dan hari ini
    - Tampilkan reminder jika selisih = 1 (H-1) atau 0 (Hari H)
    - Berikan pesan tambahan motivasi untuk setiap reminder
    """
    print("\n=== CEK REMINDER ===")
    # Mendapatkan tanggal hari ini (tanpa jam, menit, detik)
    hari_ini = datetime.now().date()
    print(f"Hari ini: {hari_ini.strftime('%d-%m-%Y')}\n")
    
    # Flag untuk mengecek apakah ada reminder
    ada_reminder = False
    
    # Iterasi setiap tugas dalam daftar
    for tugas in daftar_tugas:
        # Cek hanya tugas dengan status 'belum' (case-insensitive)
        if tugas["status"].lower() == "belum":
            # Parse string tanggal menjadi objek datetime
            deadline = datetime.strptime(tugas["deadline"], "%d-%m-%Y").date()
            # Hitung selisih hari antara deadline dan hari ini
            selisih = (deadline - hari_ini).days
            
            # Cek jika deadline besok (H-1)
            if selisih == 1:
                print(f"REMINDER H-1: {tugas['nama']}")
                print("Deadline besok, segera kerjakan!")  # notif tambahan
                print(f"Deadline: {tugas['deadline']}\n")
                ada_reminder = True
            # Cek jika deadline hari ini (Hari H)
            elif selisih == 0:
                print(f"REMINDER HARI H: {tugas['nama']}")
                print("Hari ini deadline, kerjakan segera!")  # notif tambahan
                print(f"Deadline: {tugas['deadline']}\n")
                ada_reminder = True
    
    # Jika tidak ada tugas yang perlu reminder
    if not ada_reminder:
        print("Tidak ada reminder hari ini.\n")


# Fungsi untuk mengupdate status tugas
def update_status():
    """
    Fungsi ini bertugas untuk:
    1. Menampilkan daftar tugas dengan nomor urut
    2. Memungkinkan user mengubah status tugas
    3. Menyimpan perubahan ke file
    
    Logika:
    - Jika tidak ada tugas, tampilkan pesan
    - Tampilkan daftar tugas dengan format: nomor. nama - status
    - User memilih nomor tugas dan memasukkan status baru
    - Update status tugas yang dipilih
    - Simpan perubahan ke file
    """
    print("\n=== UPDATE STATUS TUGAS ===")
    
    # Cek jika daftar tugas kosong
    if len(daftar_tugas) == 0:
        print("Belum ada tugas.")
        return
    
    # Tampilkan daftar tugas dengan nomor urut
    for i in range(len(daftar_tugas)):
        print(f"{i+1}. {daftar_tugas[i]['nama']} - {daftar_tugas[i]['status']}")
    
    # Ambil input nomor tugas yang akan diupdate
    nomor = int(input("\nPilih nomor tugas: "))
    # Ambil input status baru
    status_baru = input("Status baru (selesai/belum): ")
    
    # Update status tugas pada index yang dipilih (dikurangi 1 karena index mulai dari 0)
    daftar_tugas[nomor-1]["status"] = status_baru
    print("Status berhasil diupdate!")
    # Simpan perubahan ke file
    simpan_data()


# Fungsi untuk menampilkan seluruh daftar tugas
def tampilkan_list():
    """
    Fungsi ini bertugas untuk:
    1. Menampilkan semua tugas yang tersimpan
    2. Memberikan format tampilan yang rapi dan terstruktur
    
    Logika:
    - Jika tidak ada tugas, tampilkan pesan
    - Jika ada tugas, tampilkan dengan format:
      nomor. nama_tugas
         Keterangan: ...
         Deadline: ...
         Status: ...
    """
    print("\n=== TO-DO LIST ===")
    
    # Cek jika daftar tugas kosong
    if len(daftar_tugas) == 0:
        print("Belum ada tugas.")
    else:
        # Iterasi setiap tugas dengan nomor urut
        for i in range(len(daftar_tugas)):
            tugas = daftar_tugas[i]
            print(f"\n{i+1}. {tugas['nama']}")
            print(f"   Keterangan: {tugas['keterangan']}")
            print(f"   Deadline: {tugas['deadline']}")
            print(f"   Status: {tugas['status']}")

# Fungsi untuk menghapus tugas
def hapus_tugas():
    """
    Fungsi ini bertugas untuk:
    1. Menampilkan daftar tugas untuk dipilih
    2. Memberikan konfirmasi sebelum menghapus
    3. Menghapus tugas yang dipilih
    
    Logika:
    - Jika tidak ada tugas, tampilkan pesan
    - Tampilkan daftar tugas dengan nomor urut
    - User memilih nomor tugas dan memberikan konfirmasi
    - Jika dikonfirmasi 'yes', hapus tugas dari daftar
    - Simpan perubahan ke file
    """
    print("\n=== HAPUS TUGAS ===")
    
    # Cek jika daftar tugas kosong
    if len(daftar_tugas) == 0:
        print("Belum ada tugas.Silahkan isi tugas!!")
        return
    
    # Tampilkan daftar tugas dengan nomor urut
    for i in range(len(daftar_tugas)):
        print(f"{i+1}. {daftar_tugas[i]['nama']}")
    
    # Ambil input nomor tugas yang akan dihapus
    nomor = int(input("\nPilih nomor tugas: "))
    # Tampilkan pesan konfirmasi dengan nama tugas
    konfirmasi = input(f"Hapus '{daftar_tugas[nomor-1]['nama']}'? (yes/no): ")
    
    # Jika user mengkonfirmasi dengan 'yes'
    if konfirmasi == "yes":
        # Hapus tugas dari daftar menggunakan pop() dengan index
        daftar_tugas.pop(nomor-1)
        print("Tugas berhasil dihapus!")
        # Simpan perubahan ke file
        simpan_data()
    else:
        print("Menghapus Batal.")

# Tampilan header program
print("=" * 25)
print("     TO DO LIST      ")
print("=" * 25)


# Memuat data tugas dari file saat program pertama kali dijalankan
muat_data()

# Loop utama program - Menu interaktif
while True:
    print("\n--- MENU ---")
    print("1. Tambah tugas")      # Menambah tugas baru
    print("2. Cek reminder")    # Mengecek tugas deadline dekat
    print("3. Update status")   # Mengubah status tugas
    print("4. Tampilkan to-do list")  # Menampilkan semua tugas
    print("5. Hapus tugas")     # Menghapus tugas
    print("6. Keluar")          # Keluar dari program
    
    # Ambil input pilihan menu dari user
    pilihan = input("\nPilih menu (1-6): ")
    
    # Routing berdasarkan pilihan menu
    if pilihan == "1":
        tambah_tugas()      # Panggil fungsi tambah tugas
    elif pilihan == "2":
        cek_reminder()      # Panggil fungsi cek reminder
    elif pilihan == "3":
        update_status()      # Panggil fungsi update status
    elif pilihan == "4":
        tampilkan_list()     # Panggil fungsi tampilkan list
    elif pilihan == "5":
        hapus_tugas()        # Panggil fungsi hapus tugas
    elif pilihan == "6":
        print("\nProgram selesai. Terima kasih!")
        break                # Keluar dari loop
    else:
        print("Pilihan tidak valid!")  # Pesan error untuk input tidak valid