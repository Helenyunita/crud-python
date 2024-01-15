import mysql.connector 

db_config = mysql.connector.connect ( 
    host ='localhost', 
    user ='root', 
    password ='', 
    database ='mahasiswa' 
)
cursor = db_config.cursor() 

def pilih_menu(): 
    print("=== CRUD MENGGUNAKAN SQL ===") 
    print("[1] Lihat Daftar Mahasiswa") 
    print("[2] Tambah Mahasiswa") 
    print("[3] Edit Data Mahasiswa") 
    print("[4] Hapus Data Mahasiswa") 
    print("[0] Exit") 
    print("------------------------")
    pilihan = input("Pilih menu =  ") 
    
    if(pilihan == "1"): 
        daftar_mahasiswa() 
    elif(pilihan == "2"): 
        tambah_mahasiswa() 
    elif(pilihan == "3"): 
        edit_mahasiswa() 
    elif(pilihan == "4"): 
        hapus_mahasiswa() 
    elif(pilihan == "0"): 
        exit() 
    else: 
        print("Kamu memilih menu yang salah!") 
        kembali_menu()

# MEMBUAT FUNGSI UNTUK KEMBALI KE MENU UTAMA
def kembali_menu(): 
    print("\n") 
    input("Tekan Enter untuk kembali...")
    pilih_menu()

# FUNGSI UNTUK MELIHAT DATA (READ)
def daftar_mahasiswa(): 
    sql = "SELECT * FROM mhs" 
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result: 
        print(row)

def tambah_mahasiswa():  
    print("---- Tambah Data Mahasiswa ----")  
    nama = input("Masukkan Nama Mahasiswa: ") 
    nrp = input("Masukkan NRP Mahasiswa: ")
    jurusan = input("Masukkan Jurusan Mahasiswa: ") 
    sql = "INSERT INTO mhs ( nama, nrp, jurusan) VALUES (%s, %s, %s, %s)" 
    val = ( nama, nrp, jurusan)
    cursor.execute(sql, val) 
    db_config.commit() 
    print("Data mahasiswa berhasil ditambahkan") 

def edit_mahasiswa(): 
    print("---- Edit Data Mahasiswa ----")
    id_edit = input("Masukkan ID Mahasiswa yang akan diedit: ")
    nama = input("Masukkan Nama Mahasiswa: ")
    nrp = input("Masukkan NRP Mahasiswa: ") 
    jurusan = input("Masukkan Jurusan Mahasiswa: ") 
    sql = "UPDATE mhs SET nama=%s, nrp=%s, jurusan=%s WHERE id=%s" 
    val = (nama, nrp, jurusan, id_edit) 
    cursor.execute(sql, val) 
    db_config.commit() 
    print("Data mahasiswa berhasil di edit")

def hapus_mahasiswa():
    print("---- Hapus Data Mahasiswa ----")
    hapus_id = input("Masukkan ID Mahasiswa yang akan dihapus: ") 
    sql = "DELETE FROM mhs WHERE id=%s" 
    value = (hapus_id,)
    cursor.execute(sql, value) 
    db_config.commit() 
    print("Data mahasiswa berhasil dihapus") 

if __name__ == "__main__": 
    while True: 
        pilih_menu() 