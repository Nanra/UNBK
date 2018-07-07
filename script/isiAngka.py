#! /usr/bin/python

# Section for reading braille convert to number
import RPi.GPIO as GPIO
import time
import subprocess as cmd

pressed = "0"
nomorUjian = ""
isiValid = ""
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

# Soure Sounds
suara = 'google_speech -l id'
suaraEnter = "omxplayer -o local notif/Enter.ogg"
suaraError = "omxplayer -o local notif/Error.ogg"
suaraHapus = "omxplayer -o local notif/Hapus2.ogg"
suaraHapus2 = "omxplayer -o local notif/Hapus.ogg"
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

print "Test Pembacaan Angka\n"
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
            isiValid = bacaAngka()
            suaraAngka = suara + str(isiValid)
            cmd.call(suaraAngka, shell=True)
        print isiangka,

        if (tombolEnter is pressed) & (isiValid is ""):  # Is Arr Empty
            print("Anda Belum Mengisi Angka")
            cmd.call(suaraError, shell=True)
            cmd.call(belum, shell=True)
            continue

        if tombolEnter is pressed:  # Saving Num to Arr
            print("Angka telah disimpan ke antrian")
            antrian.append(isiValid)
            cmd.call(suaraEnter, shell=True)
            print("Antrian = ", antrian)
            isiValid = ""

        if (tombolNext is pressed) & (len(antrian == 0)):
            print ("Anda tidak bisa melanjutkan, Antrian masih kosong")
            cmd.call(suaraError, shell=True)
            cmd.call(belumIsiNim, shell=True)
            continue

        if tombolNext is pressed:
            nomorUjian = ''.join(antrian)
            kalimat = '"Nomor ujian Anda adalah : "' + nomorUjian
            suaraKalimat = suara + kalimat + '",,.. Apakah Nomor Ujian tersebut benar ?"'
            cmd.call(suaraKalimat, shell=True)
            cmd.call(validKonfirm, shell=True)
            time.sleep(3)  # Waiting for input
            tombolValidasi2 = str(GPIO.input(pinbtnValid))
            print tombolValidasi2
            if tombolValidasi2 is pressed:
                print "Y"
                cmd.call(validPressed, shell=True)
                break
            else:
                continue

        if tombolDelete is pressed:
            if len(antrian) is 0:
                print "Antrian masih Kosong"
                cmd.call(suaraError, shell=True)
                continue
            else:
                cmd.call(suaraHapus2, shell=True)
                antrian.pop()
                print (antrian)
                if len(antrian) is 0:
                    cmd.call('google_speech -l id "Antrian telah kosong. Sekarang silahkan masukkan huruf kembali !')

    time.sleep(0.3)
print("Nomor Ujian : {}".format(nomorUjian))