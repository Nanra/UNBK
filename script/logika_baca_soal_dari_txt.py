import subprocess as perintah


def main():
    bacaan = open("Sapaan_Umum.txt", "r")
    lines = bacaan.readlines()
    bacaan.close()

    for line in lines:
        print (line)
        line = str(line)
        kalimat_soal = ('"{}"'.format(line))
        isi_soal = 'google_speech -l id ' + kalimat_soal
        print isi_soal
        perintah.call(isi_soal, shell=True)


main()
