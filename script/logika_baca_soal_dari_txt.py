import subprocess as perintah


arraysoal = []
arrayjawaban = []

def main():
    bacaan_soal = open("Soal_IPA_IPA.txt", "r")
    bacaan_jawaban = open("Jawaban_IPA_IPA.txt", "r")
    parsing_soal = bacaan_soal.readlines()
    parsing_jawaban = bacaan_jawaban.readlines()
    bacaan_soal.close()
    bacaan_jawaban.close()

    i = 0

    for line in parsing_soal:
        print (line)
        arraysoal.append(line)
    for lines in parsing_jawaban:
        print (lines)
        arrayjawaban.append(lines)

    while i < len(parsing_soal):
        print arraysoal
        kalimat_soal = ('"Soal Nomor {} {}"'.format(i+1,arraysoal[i]))
        isi_soal = 'google_speech -l id ' + kalimat_soal
        print i, isi_soal
        perintah.call(isi_soal, shell=True)

        print arrayjawaban
        kalimat_jawab = ('"{}"'.format(arrayjawaban[i]))
        isi_jawaban = 'google_speech -l id ' + kalimat_jawab
        print i, isi_jawaban
        perintah.call(isi_jawaban, shell=True)
        i +=1
main()
