import sys
import subprocess as perintah

kumpulan_soal = []
kumpulan_jawaban = []

while True:
    try:
        soal = raw_input("Tuliskan Kalimat Soal : ")
        jawab = raw_input("Tuliskan Jawaban Dari Soal : ")
        soal = str(soal)
        jawab = str(jawab)
        kalimat_soal = ('"{}"'.format(soal))  # String Formatting New Version
        kalimat_jawab = ('"{}"'.format(jawab))  # String Formatting New Version
        isi_soal = 'google_speech -l id ' + kalimat_soal
        isi_jawab = 'google_speech -l id ' + kalimat_jawab

        # Play suara soal
        print "\nSedang Membacakan Soal..."
        perintah.call(isi_soal, shell=True)

        # Play suara Jawaban
        print "Sedang Membacakan Jawaban..."
        perintah.call(isi_jawab, shell=True)

        # print isi
        print "\nSoal yang Anda masukkan adalah " + kalimat_soal + "\n"
        print "\nPilihan jawaban yang Anda masukkan adalah " + kalimat_jawab + "\n"

        # Menyimpan Kumpulan Soal kedalam List/Array
        kumpulan_soal.append(soal.upper())
        kumpulan_jawaban.append(jawab.upper())

        # Tampilkan List/Array
        print kumpulan_soal
        print kumpulan_jawaban
        # Menghapus soal terkahir
        soal = ""
        jawab = ""

    except KeyboardInterrupt:
        pilihan = raw_input("Apakah anda ingin menyimpan soal ? (Y/N) : ")
        pilihan_user = pilihan.upper()
        if pilihan_user == "Y":
            # Menyimpan List Soal kedalam File
            nama_soal = raw_input("Masukkan Nama Soal Untuk Menyimpan : ")
            tipe_soal = raw_input("Jenis Soal : ")
            simpan_soal = open("Soal_{}_{}.txt".format(nama_soal, tipe_soal), 'w')
            simpan_jawaban = open("Jawaban_{}_{}.txt".format(nama_soal, tipe_soal), 'w')
            for i in kumpulan_soal:
                simpan_soal.write(i + '\n')
            for i in kumpulan_jawaban:
                simpan_jawaban.write(i + '\n')
            simpan_soal.close()
            simpan_jawaban.close()
            perintah.call('google_speech -l id "Terimakasih,Soal sudah tersimpan!"', shell=True)
        else:
            print "\nAnda memilih keluar , Tanpa menyimpan soal !"
            perintah.call('google_speech -l id "Terimakasih sudah mencoba,Sampai jumpa !" ', shell=True)
            # print (kumpulan_soal)
        sys.exit()
