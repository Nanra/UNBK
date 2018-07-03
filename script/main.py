# Main Aplikasi Keseluruhan Untuk Proses Ujian


import sys
import subprocess as perintah

# Sesi Pembacaan Greetings
print ("Sesi Greetings")
bacaan_sapaan = open("SapaanUtama.txt", "r")
parsing_sapaan = bacaan_sapaan.readlines()
for s in parsing_sapaan:
        kalimat_sapaan = ('"{}"'.format(s))
        isi_sapaan = 'google_speech -l id ' + kalimat_sapaan + ' -e speed 1 '
        perintah.call(isi_sapaan, shell=True)

# Sesi Pengisian Identitas Peserta Ujian
print ("Sesi Pengisian Identitas Ujian")
kalID = '"Anda memasuki sesi pengisian identitas peserta ujian."'
kalID2 = '"Mohon isikan dengan baik dan benar identitas diri anda !"'
perintah.call('google_speech -l id ' + kalID + ' -e speed 1 ', shell=True)
perintah.call('google_speech -l id ' + kalID2 + ' -e speed 1 ', shell=True)

# Pengisian Nama
print ("Sesi Pengisian Nama")
kalNama = '"Sekarang silahkan isikan nama lengkap Anda !"'
perintah.call('google_speech -l id ' + kalNama + ' -e speed 1 ', shell=True)
perintah.call("python isiNama.py", shell=True) # Opening Module isiNama.py

# Pengisian Nama
print ("Sesi Pengisian Nomor Ujian")
kalNama = '"Sekarang silahkan isikan nomor ujian Anda !"'
perintah.call('google_speech -l id ' + kalNama + ' -e speed 1 ', shell=True)
#perintah.call("python isiNama.py", shell=True)
