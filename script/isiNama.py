#!/usr/bin/python

# Section for reading braille convert to alphabet
# Importing Modules and Libraries
import RPi.GPIO as GPIO
import time
import subprocess as cmd

# Database connection
import MySQLdb
db = MySQLdb.connect(host="172.20.10.3",
                     user="root",
                     passwd="raspberry",
                     db="sisunbk")
cursor = db.cursor()
print ("Database OK..")

# Defenisi Mode GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Deklarasi Variabels
pressed = "0"
nama = ""
isivalid = ""
antrian = []
pinbtnValid = 31
pinbtnNext = 5
pinbtnPrev = 29
pinbtnDelete = 32
pinbtnEnter = 3
pinbtnSatu = 36
pinbtnDua = 38
pinbtnTiga = 40
pinbtnEmpat = 37
pinbtnLima = 35
pinbtnEnam = 33

# Sounds Source
suara = 'google_speech -l id '
suaraEnter = "omxplayer -o local notif/Enter.ogg"
suaraError = "omxplayer -o local notif/Error.ogg"
suaraHapus = "omxplayer -o local notif/Hapus2.ogg"
suaraHapus2 = "omxplayer -o local notif/Hapus.ogg"
belum = "omxplayer -o local notif/belum.ogg"
belumIsiNama = "omxplayer -o local Petunjuk/belumIsiNama.mp3"
tandaStrip = 'google_speech -l id "Tanda Strip"'
sesiNama = "omxplayer -o local Petunjuk/sesiNama/sesiNama.mp3"
sesiNama2 = "omxplayer -o local Petunjuk/sesiNama/sesiNama2.mp3"
sesiNama3 = "omxplayer -o local Petunjuk/sesiNama/sesiNama3.mp3"
sesiNama4 = "omxplayer -o local Petunjuk/sesiNama/sesiNama4.mp3"
sesiNama5 = "omxplayer -o local Petunjuk/sesiNama/sesiNama5.mp3"
sesiNama6 = "omxplayer -o local Petunjuk/sesiNama/sesiNama6.mp3"
sesiNama7 = "omxplayer -o local Petunjuk/sesiNama/sesiNama7.mp3"
sesiNama8 = "omxplayer -o local Petunjuk/sesiNama/sesiNama8.mp3"
validKonfirm = "omxplayer -o local Petunjuk/validKonfirm.mp3"
validPressed = "omxplayer -o local Petunjuk/validPressed.mp3"
sapaNama = [sesiNama, sesiNama2,
            sesiNama3, sesiNama4,
            sesiNama5, sesiNama6,
            sesiNama7, sesiNama8]
pinbtn = [pinbtnValid, pinbtnNext,
          pinbtnPrev, pinbtnDelete,
          pinbtnEnter, pinbtnSatu,
          pinbtnDua, pinbtnTiga,
          pinbtnEmpat, pinbtnLima, pinbtnEnam]

# Deklarasi Button Huruf Sebagai OUTPUT
i = 0
while i < len(pinbtn):
    GPIO.setup(pinbtn[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    i += 1

# cmd.call('google_speech -l id "Status Semua PIN OK !"', shell=True)
print "All Pin OK\n"
# print "Test Pembacaan Huruf\n"

# Play Greetings
for baca in sapaNama:
    cmd.call(baca, shell=True)
print "Masukkan Huruf\n"


# Fungsi Baca Kode Braille
def braille():
    tom1 = str(GPIO.input(pinbtnSatu))
    tom2 = str(GPIO.input(pinbtnDua))
    tom3 = str(GPIO.input(pinbtnTiga))
    tom4 = str(GPIO.input(pinbtnEmpat))
    tom5 = str(GPIO.input(pinbtnLima))
    tom6 = str(GPIO.input(pinbtnEnam))
    n = tom3 + tom2 + tom1 + tom4 + tom5 + tom6
    if n == "111111":
        pass
    else:
        return n


def abjad(n="111111"):
    if n == "110111":
        x = "A"
    elif n == "100111":
        x = "B"
    elif n == "110011":
        x = "C"
    elif n == "110001":
        x = "D"
    elif n == "110101":
        x = "E"
    elif n == "100011":
        x = "F"
    elif n == "100001":
        x = "G"
    elif n == "100101":
        x = "H"
    elif n == "101011":
        x = "I"
    elif n == "101001":
        x = "J"
    elif n == "010111":
        x = "K"
    elif n == "000111":
        x = "L"
    elif n == "010011":
        x = "M"
    elif n == "010001":
        x = "N"
    elif n == "010101":
        x = "O"
    elif n == "000011":
        x = "P"
    elif n == "000001":
        x = "Q"
    elif n == "000101":
        x = "R"
    elif n == "001011":
        x = "S"
    elif n == "001001":
        x = "T"
    elif n == "010110":
        x = "U"
    elif n == "000110":
        x = "V"
    elif n == "101000":
        x = "W"
    elif n == "010010":
        x = "X"
    elif n == "010000":
        x = "Y"
    elif n == "010100":
        x = "Z"
    elif n == "011110":
        x = "-"
    else:
        x = "NULL"
    return x


def baca__input__huruf():
    baca = braille()
    if baca is None:
        baca
    else:
        return baca


def baca_huruf():
    isi = abjad(n=baca__input__huruf())
    return isi


while True:
    tombolValidasi = str(GPIO.input(pinbtnValid))
    tombolEnter = str(GPIO.input(pinbtnEnter))
    tombolNext = str(GPIO.input(pinbtnNext))
    tombolPrev = str(GPIO.input(pinbtnPrev))
    tombolDelete = str(GPIO.input(pinbtnDelete))
    huruf = baca_huruf()  # Baca Huruf
    if huruf == "NULL":
        baca_huruf()
    else:
        if tombolValidasi is pressed:
            isivalid = huruf
            suaraHuruf = suara + str(isivalid)

            if isivalid is "-":
                cmd.call(tandaStrip, shell=True)
                print isivalid
            cmd.call(suaraHuruf, shell=True)
            print "Isi Valid = ", isivalid
            # print suaraHuruf # Bug Checker
        print huruf,

    if (tombolEnter is pressed) & (isivalid is ""):
        print "Anda Belum Mengisi Huruf"
        cmd.call(suaraError, shell=True)
        cmd.call(belum, shell=True)
        continue

    if tombolEnter is pressed:
        print "Huruf telah disimpan ke antrian"
        antrian.append(isivalid)
        cmd.call(suaraEnter, shell=True)
        print "Antrian = ", antrian
        isivalid = ""

    if (tombolNext is pressed) & (len(antrian) == 0):
        print "Anda tidak bisa lanjutkan, Antrian masih kosong"
        cmd.call(suaraError, shell=True)
        cmd.call(belumIsiNama, shell=True)
        continue

    if tombolNext is pressed:
        print "Tombol Next Telah Ditekan"
        nama = ''.join(antrian)
        kalimat = '"Nama Anda Adalah : "' + nama
        suaraKalimat = suara + kalimat + '",,.. Apakah Nama Tersebut benar ?"'
        cmd.call(suaraKalimat, shell=True)
        cmd.call('google_speech -l id "Tekan Tombol Validasi jika benar !"', shell=True)
        cmd.call('google_speech -l id "Jika belum benar, silahkan masukkan kembali nama Anda !"', shell=True)
        # cmd.call(validKonfirm, shell=True)
        print "Menunggu Konfirmasi ...."
        time.sleep(2)  # Witing for Input Konfirmasi
        tombolValidasi2 = str(GPIO.input(pinbtnValid))
        print tombolValidasi2
        if tombolValidasi2 is pressed:
            print "Y"
            cmd.call(suaraEnter, shell=True)
            cmd.call('google_speech -l id "Anda menekan tombol validasi"', shell=True)
            # cmd.call(validPressed, shell=True)
            break
        else:
            continue

    if tombolPrev is pressed:
        cmd.call(suaraHapus, shell=True)
        antrian = []
        print "\nAntrian telah dihapus semua\n"
        cmd.call('google_speech -l id "antrian telah dihapus, sekarang masukkan huruf kembali"', shell=True)
        print "Masukkan Huruf\n"

    if tombolDelete is pressed:
        if len(antrian) is 0:
            print "Antrian Kosong Laek"
            cmd.call(suaraError, shell=True)
            continue
        else:
            cmd.call(suaraHapus2, shell=True)
            antrian.pop()
            print antrian
            if len(antrian) is 0:
                cmd.call('google_speech -l id "antrian telah kosong, sekarang masukkan huruf kembali"', shell=True)

    time.sleep(0.3)
    
# Query Simpan Data Nama ke Database Server
sql = "INSERT INTO testdb (namaSiswa) VALUES ('%s')"%(nama)
sql2 = "SELECT id FROM testdb WHERE namaSiswa = '%s'"%(nama)

try:
    cursor.execute(sql) # Eksekusi Query simpan database
    db.commit()
    print ('Data Nama : {} berhasil disimpan ke database').format(nama)

    cursor.execute(sql2) # Eksekusi Query ambil ID nama
    for row in cursor.fetchall():
        idSiswa = row[0]
    print ('Data ID Siswa {} = {}').format(nama, idSiswa)

    # Menyimpan Data ID ke dalam berkas
    berkas = open("dataID.txt", "w")
    berkas.write(str(idSiswa))
    print ("Data ID berhasil disimpan ke berkas")
    berkas.close()

except:
    db.rollback()
    print('Oopss... Ada error nih')

db.close()
