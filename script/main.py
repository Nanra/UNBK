# Main Aplikasi Keseluruhan Untuk Proses Ujian


import sys
import subprocess as perintah

sapa1 = "omxplayer -o local notif/selamatDatang.ogg"
sapa2 = "omxplayer -o local notif/selamatDatang2.ogg"
sapa3 = "omxplayer -o local notif/selamatDatang3.ogg"
sapa4 = "omxplayer -o local notif/selamatDatang4.ogg"
sapa5 = "omxplayer -o local notif/selamatDatang5.ogg"
# Sesi Pembacaan Greetings

perintah.call(sapa1, shell=True)
perintah.call(sapa2, shell=True)
perintah.call(sapa3, shell=True)
perintah.call(sapa4, shell=True)
perintah.call(sapa5, shell=True)

##print ("Sesi Greetings")
##bacaan_sapaan = open("SapaanUtama.txt", "r")
##parsing_sapaan = bacaan_sapaan.readlines()
##for s in parsing_sapaan:
##        kalimat_sapaan = ('"{}"'.format(s))
##        isi_sapaan = 'google_speech -l id ' + kalimat_sapaan + ' -e speed 1 '
##        perintah.call(isi_sapaan, shell=True)

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
