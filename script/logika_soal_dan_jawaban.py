print "*" * 50

# Bagian Deklarasi
kunci = ["A", "B", "C", "D"]
urut = ["PERTAMA", "KEDUA", "KETIGA", "KEEMPAT"]
soal = ["""Apa nama Ibukota Indonesia ? \n A. Jakarta \n B. Bandung \n C. Medan \n D. Batam""",
        """Apa nama Ibukota Provinsi Jawa Barat ? \n A. Jakarta \n B. Bandung \n C. Medan \n D. Batam""",
        """Apa nama Ibukota Provinsi Sumatera Utara ? \n A. Jakarta \n B. Bandung \n C. Medan \n D. Batam""",
        """Siapa nama Presiden Republik Indonesia ke-4 ? \n A. Ir. Soekarno \n B. Megawati Soekarnoputri \n C. Joko 
        Widodo \n D. Abdurrahman Wahid"""]
benar = 0
salah = 0
catatan = ""
i = 0
jwb = []

# Bagian Input Jawaban
while i < len(soal):
    print soal[i]
    jawaban = raw_input(" \nMasukkan Jawaban : ")
    i += 1
    jwb.append(jawaban.upper())
    print "\n"
    print "*" * 50
    print "\n"

print " \nJawaban anda adalah : "
print jwb

n = 0
# Uji Jawaban
for n in range(i):
    if jwb[n] == kunci[n]:
        print "Jawaban ", urut[n], " BENAR"
        benar += 1
    else:
        print "Jawaban ", urut[n], " SALAH"
        salah += 1

if benar >= 3:
    catatan = "Anda Luar Biasa"
elif benar == 2:
    catatan = "Cukup"
elif benar == 1:
    catatan = "Buruk"
else:
    catatan = "Anda belum Lulus"

# Hasil Akhir
print "\nHasil Keseluruhan :"
print "Jumlah Jawaban Benar = ", benar
print "Jumlah Jawaban Salah = ", salah
print "Catatan Pencapaian : ", catatan
print "*" * 50
raw_input("Tekan ENTER untuk keluar ....")
