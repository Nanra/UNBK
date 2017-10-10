import subprocess as perintah


def main():
    bacaan_soal = open("Soal_IPA_IPA.txt", "r")
    bacaan_jawaban = open("Jawaban_IPA_IPA.txt", "r")
    parsing_soal = bacaan_soal.readlines()
    parsing_jawaban = bacaan_jawaban.readlines()
    bacaan_soal.close()
    bacaan_jawaban.close()

    for line in parsing_jawaban:
        print (line)
        line = str(line)
        kalimat_soal = ('"{}"'.format(line))
        isi_soal = 'google_speech -l id ' + kalimat_soal
        print isi_soal
        perintah.call(isi_soal, shell=True)


main()
