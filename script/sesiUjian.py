# Section for examination
# Importing Modules and Libraries
import RPi.GPIO as GPIO
import time
import subprocess as cmd
import sys

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
arraySoal = []
arrayPilihan = []
jawaban = {}
soalSkip = []
pressed = "0"
noSoal = 0
isivalid = ""
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
sesiMasukkanJawaban = 'google_speech -l id "Silahkan Masukkan Jawaban Anda !"'
validKonfirm = "omxplayer -o local Petunjuk/validKonfirm.mp3"
validPressed = "omxplayer -o local Petunjuk/validPressed.mp3"

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

# Fungsi Cek isi Dictionary
def cek_dict(noSoal):
    if noSoal in jawaban:
        return True
    else:
        return False

# Reading Section

bacaan_sapaan = open("SapaanUtama.txt", "r")
bacaanSoal = open("Soal_Pengetahuan_Sosial_IPS.txt", "r")
bacaanPilihan = open("Jawaban_Pengetahuan_Sosial_IPS.txt", "r")
parsing_sapaan = bacaan_sapaan.readlines()
parsingSoal = bacaanSoal.readlines()
parsingPilihan = bacaanPilihan.readlines()
bacaanSoal.close()
bacaanPilihan.close()

# Membaca Petunjuk Ujian
for s in parsing_sapaan:
   kalimat_sapaan = ('"{}"'.format(s))
   isi_sapaan = 'google_speech -l id ' + kalimat_sapaan + ' -e speed 1 '
   cmd.call(isi_sapaan, shell=True)


for soal in parsingSoal:
    #print (soal)
    arraySoal.append(soal)
for pilihan in parsingPilihan:
    #print (pilihan)
    arrayPilihan.append(pilihan)

while noSoal < len(parsingSoal):
    # Proses pembacaan soal
    #print arraySoal
    bacaNomor = noSoal
    kalimatSoal = ('"Soal Nomor {} ...., {}"'.format(bacaNomor + 1, arraySoal[noSoal]))
    isiSoal = 'google_speech -l id ' + kalimatSoal + ' -e speed 1 '
    print noSoal, isiSoal
    cmd.call(isiSoal, shell=True)

    # Proses pembacaan Jawaban
    #print arrayPilihan
    kalimatPilihan = ('" Pilihannya adalah ......, {}"'.format(arrayPilihan[noSoal]))
    isiPilihan = 'google_speech -l id ' + kalimatPilihan + ' -e speed 0.9 '
    print noSoal, isiPilihan
    cmd.call(isiPilihan, shell=True)

    # Proses menerima jawaban dari Siswa

    print "\nMenunggu Jawaban dari User...."
    print ("Nomor Index Array Sekarang {}").format(noSoal)
    cmd.call(sesiMasukkanJawaban, shell=True)
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
            print "Anda Belum Mengisi Jawaban"
            cmd.call(suaraError, shell=True)
            # cmd.call(belum, shell=True)
            cmd.call('google_speech -l id "Anda belum memilih jawaban, pilih jawaban terlebih dahulu"', shell=True)
            continue

        if tombolEnter is pressed:
            print "Jawaban telah disimpan ke antrian"
            jawaban[noSoal] = isivalid # Saving Answer With Specific Index
            #if noSoal in soalSkip : # Check Apakah soal pernah dilewat
            #    soalSkip.remove(soalSkip[noSoal])
            #    print ("Soal Skip : {}").format(soalSkip)
            cmd.call(suaraEnter, shell=True)
            print "Jawaban = ", jawaban
            isivalid = ""
            continue

        if (tombolNext is pressed) & (cek_dict(noSoal) is False): # Skip Soal
            print "Tombol Next ditekan, Jawaban masih kosong"
            jawaban[noSoal] = ""
            soalSkip.insert(noSoal, noSoal) # Menyimpan Indeks Soal yang dilewat
            noSoal = noSoal + 1
            bacaNomorLewat = '"Soal Nomor {} dilewati"'.format(bacaNomor + 1)
            cmd.call('google_speech -l id ' + bacaNomorLewat + '', shell=True)
            print (jawaban)
            print (soalSkip)
            break

        if tombolNext is pressed:
            noSoal += 1
            break


        if tombolPrev is pressed:
            print "Tombol Previous Ditekan"
            time.sleep(1)
            tombolPrev2 = str(GPIO.input(pinbtnPrev))
            if tombolPrev2 is pressed: # Back to previous Soal
                if noSoal == 0:
                    print "Ini Soal nomor Satu laek "
                    cmd.call('google_speech -l id "Ini Merupakan Soal Nomor Satu, Anda tidak bisa mundur ke soal sebelumnya."', shell=True)
                    continue
                noSoal = noSoal - 1
                break
            else: # Play again soal
                break


        if tombolDelete is pressed:
            if cek_dict(noSoal) is False:
                print "Jawaban masih Kosong"
                cmd.call(suaraError, shell=True)
                cmd.call('google_speech -l id "Anda belum memasukkan Jawaban, Masukkan Jawaban terlebih dahulu"', shell=True)
                continue
            else:
                cmd.call(suaraHapus2, shell=True)
                jawaban[noSoal] = ""
                print jawaban
                cmd.call('google_speech -l id "Jawaban telah dihapus, sekarang masukkan jawaban kembali"', shell=True)

        time.sleep(0.3)
    # noSoal += 1
else:
    print ("Ujian Selesai")
    cmd.call('google_speech -l id "Sesi Ujian telah selesai, Semua soal telah dibacakan. Terimakaih dan semoga sukses "', shell=True)
    list_jawaban = list(jawaban.values())
    print (list_jawaban)
    jawabanAkhir = ''.join(list_jawaban)
    print (jawabanAkhir)

    # Menyimpan Data ID ke dalam berkas
    berkas = open("dataID.txt", "r")
    idSiswa = berkas.read()
    idSiswa = int(idSiswa)
    print ("Data ID = {}").format(idSiswa)
    berkas.close()

    sql = "UPDATE testdb SET jawaban = '%s' WHERE id = '%d' " % (jawabanAkhir, idSiswa)
    # sql2 = "SELECT id FROM testdb WHERE namaSiswa = '%s'"%(namaSiswa)
    try:
        cursor.execute(sql)
        db.commit()
        print ('Data Jawaban : {} dengan ID = {} berhasil disimpan').format(list_jawaban, idSiswa)
        print ('Data berhasil disimpan')

    except:
        db.rollback()
        print('Oopss... Ada error nih')

    db.close()

    print "Selesai"
    sys.exit()
