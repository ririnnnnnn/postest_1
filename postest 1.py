print (50*"=")
print ("SILAHKAN LOGIN TERLEBIH DAHULU!")
print (50*"=")
nama = input ("masukkan nama: ")
NIM = input ("masukkan NIM: ")
prodi = input ("masukkan prodi: ")
# menu 
print("----------------------------------")
print ("hai!")
print ("silahkan memilih operasi: ")
print ("1. konversi rupiah ke USD")
print ("2. konversi rupiah ke yen")
print ("3. konversi rupiah ke ringgit")
print ("4. keluar")
print("----------------------------------")

# input
USD = 15000
yen = 100
ringgit = 3000
pilihan = input("silahkan memilih operasi [1/2/3/4]: ")
if pilihan == "1": 
    rupiah = int (input ("masukkan rupiah: "))
    konversi = (rupiah)/USD 
    print ("hasil konversi adalah ", konversi, "USD")

elif pilihan == "2": 
    rupiah = int (input ("masukkan rupiah: "))
    konversi = (rupiah)/yen
    print ("hasil hitung: ", konversi, "yen")

elif pilihan == "3": 
    rupiah = int (input ("masukkan rupiah: "))
    konversi = (rupiah)/ringgit
    print ("hasil hitung: ", konversi, "ringgit")

elif pilihan == "4":
    print ("anda telah keluar")

print (50*"=")
print ("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI")
print (50*"=")
