import sys
import subprocess as perintah

namaFile = raw_input("Masukkan Nama File : ")
file_masukan = open('"{}"'.format(namaFile), "r")
parsing_file = file_masukan.readlines()
file_masukan.close()

for line in parsing_file:
        kalimat_file = ('"{}"'.format(line))
        isi_file = 'google_speech -l id ' + kalimat_file + ' -e speed 1 '
        perintah.call(isi_file, shell=True)
sys.exit()
