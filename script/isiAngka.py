#! /usr/bin/python

# Section for reading braille convert to number
import RPi.GPIO as GPIO
import time
import subprocess as cmd

pressed = "0"
nomorUjian = ""
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
belum = "omxplayer -o local Petunjuk/belumNomor.ogg"
belumIsiNomor = "omxplayer -o local Petunjuk/belumIsiNomor.mp3"
sesiNomor = "omxplayer -o local Petunjuk/sesiNomor/sesiNomor.mp3"
sesiNomor2 = "omxplayer -o local Petunjuk/sesiNomor/sesiNomor2.mp3"
sesiNomor3 = "omxplayer -o local Petunjuk/sesiNomor/sesiNomor3.mp3"
sesiNomor4 = "omxplayer -o local Petunjuk/sesiNomor/sesiNomor4.mp3"
sesiNomor5 = "omxplayer -o local Petunjuk/sesiNomor/sesiNomor5.mp3"
sesiNomor6 = "omxplayer -o local Petunjuk/sesiNomor/sesiNomor6.mp3"
sesiNomor7 = "omxplayer -o local Petunjuk/sesiNomor/sesiNomor7.mp3"
sesiNomor8 = "omxplayer -o local Petunjuk/sesiNomor/sesiNomor8.mp3"
validKonfirm = "omxplayer -o local Petunjuk/validKonfirm.mp3"
validPressed = "omxplayer -o local Petunjuk/validPressed.mp3"
sapaNomor = [sesiNomor, sesiNomor2,
             sesiNomor3, sesiNomor4,
             sesiNomor5, sesiNomor6,
             sesiNomor7, sesiNomor8]
pinbtn = [pinbtnValid, pinbtnNext,
          pinbtnPrev, pinbtnDelete,
          pinbtnEnter, pinbtnSatu,
          pinbtnDua, pinbtnTiga,
          pinbtnEmpat, pinbtnLima, pinbtnEnam]

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Deklarasi Button Huruf Sebagai OUTPUT
i = 0
while i < len(pinbtn):
    GPIO.setup(pinbtn[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    i += 1
print "All Pin OK\n"

# Play Greetings
#for baca in sapaNomor:
#    cmd.call(baca, shell=True)

# print "Test Pembacaan Angka\n"
print "Masukkan Angka\n"


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


# Deklarasi Angka
def angka(n="111111"):
    if n == "110111":
        x = "1"
    elif n == "100111":
        x = "2"
    elif n == "110011":
        x = "3"
    elif n == "100011":
        x = "4"
    elif n == "110101":
        x = "5"
    elif n == "100011":
        x = "6"
    elif n == "100001":
        x = "7"
    elif n == "100101":
        x = "8"
    elif n == "101011":
        x = "9"
    elif n == "101001":
        x = "0"
    else:
        x = "SALAH"
    return x


def bacaInputAngka():
    baca = braille()
    if baca is None:
        baca
    else:
        return baca


def bacaAngka():
    isi = angka(n=bacaInputAngka())
    return isi


while True:
    tombolValidasi = str(GPIO.input(pinbtnValid))
    tombolEnter = str(GPIO.input(pinbtnEnter))
    tombolNext = str(GPIO.input(pinbtnNext))
    tombolPrev = str(GPIO.input(pinbtnPrev))
    tombolDelete = str(GPIO.input(pinbtnDelete))
    isiangka = bacaAngka()  # Baca Angka
    if isiangka == "SALAH":
        bacaAngka()
    else:
        if tombolValidasi is pressed:  # Validation Button
            isivalid = bacaAngka()
            suaraAngka = suara + str(isivalid)
            cmd.call(suaraAngka, shell=True)
            print suaraAngka,
            print "Isi Valid = ", isivalid
        print isiangka,

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
        cmd.call(belumIsiNomor, shell=True)
        continue

    if tombolNext is pressed:
        nama = ''.join(antrian)
        kalimat = '"Nama Anda Adalah : "' + nama
        suaraKalimat = suara + kalimat + '",,.. Apakah Nama Tersebut benar ?"'
        cmd.call(suaraKalimat, shell=True)
        cmd.call(validKonfirm, shell=True)
        time.sleep(2)  # Witing for Input
        # Konfirmasi Nama ( Baru sampai disini besok lanjut lagi)
        tombolValidasi2 = str(GPIO.input(pinbtnValid))
        print tombolValidasi2
        if tombolValidasi2 is pressed:
            print "Y"
            cmd.call(validPressed, shell=True)
            break
        else:
            continue

    if (tombolPrev is pressed) & (len(antrian) == 0):
        print "Anda tidak bisa hapus semua, Antrian masih kosong"
        cmd.call(suaraError, shell=True)
        cmd.call(belumIsiNomor, shell=True)
        continue

    if tombolPrev is pressed:
        cmd.call(suaraHapus, shell=True)
        antrian = []
        print "\nAntrian dihapus kabeh Lur\n"
        cmd.call('google_speech -l id "antrian telah dihapus, sekarang masukkan huruf kembali"', shell=True)
        print "Masukkan Huruf\n"

    if (tombolDelete is pressed) & (len(antrian) == 0):
        print "Anda tidak bisa menghapus, Antrian masih kosong"
        cmd.call(suaraError, shell=True)
        cmd.call(belumIsiNomor, shell=True)
        continue

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
print ("Nama adalah : {}".format(nama))
