# Main Aplikasi Keseluruhan Untuk Proses Ujian

import subprocess as perintah
import check_connection

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

# Greetings Sessions
print ("Greetings Session")
for baca in arraySapaan:
    perintah.call(baca, shell=True)

# Sesi Pengisian Identitas Peserta Ujian
print ("Sesi Pengisian Identitas Ujian")
# Uncomment for debugging
print ("Playing KalID")
perintah.call(kalID, shell=True)
print ("Playing KalID2")
perintah.call(kalID2, shell=True)

# Sesi Pengisian Nama
print ("Sesi Pengisian Nama")
# Uncomment for debugging
print ("Playing KalNama")
# perintah.call(kalNama, shell=True)
print ("Playing Isi Angka Section")
perintah.call("python isiNama.py", shell=True)  # Opening Module isiNama.py

# Sesi Pengisian Nama
print ("Sesi Pengisian Nomor Ujian")
# Uncomment for debugging
print ("Playing KalNomor")
perintah.call(kalNomor, shell=True)
# Uncomment for debugging
# print ("Playing KalNomor2")
# perintah.call(kalNomor2, shell=True)
print ("Playing Isi Angka Section")
perintah.call("python isiAngka.py", shell=True) # Opening Module isiAngka.py


# Sesi Ujian
# print ("Sesi Ujian")
# perintah.call(kalUjian, shell=True)
# perintah.call(kalUjian2, shell=True)
print ("Playing Sesi Ujian")
perintah.call("python sesiUjian.py", shell=True)

print ("Selesai")
