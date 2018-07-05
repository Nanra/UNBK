# Main Aplikasi Keseluruhan Untuk Proses Ujian

import sys
import subprocess as perintah

# Source Sound
sapa1 = "omxplayer -o local Petunjuk/sapaan/sapaan.mp3"
sapa2 = "omxplayer -o local Petunjuk/sapaan/sapaan2.mp3"
sapa3 = "omxplayer -o local Petunjuk/sapaan/sapaan3.mp3"
sapa4 = "omxplayer -o local Petunjuk/sapaan/sapaan4.mp3"
sapa5 = "omxplayer -o local Petunjuk/sapaan/sapaan5.mp3"
arraySapaan = [sapa1, sapa2, sapa3, sapa4, sapa5]
kalID = "omxplayer -o local Petunjuk/sapaan/sapaanIdentitas.mp3"
kalID2 = "omxplayer -o local Petunjuk/sapaan/sapaanIdentitas2.mp3"
kalNama = "omxplayer -o local Petunjuk/sapaan/sapaanNama.mp3"
kalNomor = "omxplayer -o local Petunjuk/sapaan/sapaanNomor.mp3"
kalNomor2 = "omxplayer -o local Petunjuk/sapaan/sapaanNomor2.mp3"

### Greetings Sessions
##print ("Greetings Session")
##for baca in arraySapaan:
##    perintah.call(baca, shell=True)
##
### Sesi Pengisian Identitas Peserta Ujian
##print ("Sesi Pengisian Identitas Ujian")
##perintah.call(kalID, shell=True)
##perintah.call(kalID2, shell=True)
##
### Sesi Pengisian Nama
##print ("Sesi Pengisian Nama")
##perintah.call(kalNama, shell=True)
##perintah.call("python isiNama.py", shell=True) # Opening Module isiNama.py

# Pengisian Nama
print ("Sesi Pengisian Nomor Ujian")
perintah.call(kalNomor, shell=True)
perintah.call(kalNomor2, shell=True)
#perintah.call("python isiNama.py", shell=True)
