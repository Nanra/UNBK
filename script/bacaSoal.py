import sys
import subprocess as perintah

arraySoal = []
arrayPilihan = []


def main():
    # bacaan_sapaan = open("Sapaan_Umum.txt", "r")
    bacaanSoal = open("Soal_Dasar_Bahasa Indonesia.txt", "r")
    bacaanPilihan = open("Jawaban_Dasar_Bahasa Indonesia.txt", "r")
    # parsing_sapaan = bacaan_sapaan.readlines()
    parsingSoal = bacaanSoal.readlines()
    parsingPilihan = bacaanPilihan.readlines()
    bacaanSoal.close()
    bacaanPilihan.close()

    # for s in parsing_sapaan:
    #    kalimat_sapaan = ('"{}"'.format(s))
    #    isi_sapaan = 'google_speech -l id ' + kalimat_sapaan + ' -e speed 1 '
    #    perintah.call(isi_sapaan, shell=True)

    i = 0
    for soal in parsingSoal:
        print (soal)
        arraySoal.append(soal)
    for pilihan in parsingPilihan:
        print (pilihan)
        arrayPilihan.append(pilihan)

    while i < len(parsingSoal):
        print arraySoal
        kalimatSoal = ('"Soal Nomor {} ...., {}"'.format(i + 1, arraySoal[i]))
        isiSoal = 'google_speech -l id ' + kalimatSoal + ' -e speed 1 '
        print i, isiSoal
        perintah.call(isiSoal, shell=True)

        print arrayPilihan
        kalimatPilihan = ('" Pilihannya adalah ......, {}"'.format(arrayPilihan[i]))
        isiPilihan = 'google_speech -l id ' + kalimatPilihan + ' -e speed 0.9 '
        print i, isiPilihan
        perintah.call(isiPilihan, shell=True)
        i += 1
    else:
        return sys.exit()


if __name__ == "__main__":
    main()
