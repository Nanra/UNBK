import sys
import subprocess as perintah

arraysoal = []
arrayjawaban = []


def main():
    bacaan_sapaan = open("Sapaan_Umum.txt", "r")
    bacaan_soal = open("Soal_Pengetahuan_Sosial_IPS.txt", "r")
    bacaan_jawaban = open("Jawaban_Pengetahuan_Sosial_IPS.txt", "r")
    parsing_sapaan = bacaan_sapaan.readlines()
    parsing_soal = bacaan_soal.readlines()
    parsing_jawaban = bacaan_jawaban.readlines()
    bacaan_soal.close()
    bacaan_jawaban.close()

    for s in parsing_sapaan:
        kalimat_sapaan = ('"{}"'.format(s))
        isi_sapaan = 'google_speech -l id ' + kalimat_sapaan + ' -e speed 5 '
        perintah.call(isi_sapaan, shell=True)

    i = 0
    for line in parsing_soal:
        print (line)
        arraysoal.append(line)
    for lines in parsing_jawaban:
        print (lines)
        arrayjawaban.append(lines)

    while i < len(parsing_soal):
        print arraysoal
        kalimat_soal = ('"Soal Nomor {} ...., {}"'.format(i + 1, arraysoal[i]))
        isi_soal = 'google_speech -l id ' + kalimat_soal + ' -e speed 0.9 '
        print i, isi_soal
        perintah.call(isi_soal, shell=True)

        print arrayjawaban
        kalimat_jawab = ('" Pilihannya adalah ......, {}"'.format(arrayjawaban[i]))
        isi_jawaban = 'google_speech -l id ' + kalimat_jawab + ' -e speed 0.9 '
        print i, isi_jawaban
        perintah.call(isi_jawaban, shell=True)
        i += 1
    else:
        return sys.exit()

if __nama__=="__main__":
    main()
