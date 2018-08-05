import MySQLdb
db = MySQLdb.connect(host="172.20.10.3",
                     user="root",
                     passwd="raspberry",
                     db="sisunbk")
cursor = db.cursor()

# Var Data Akan Dikirim
namaSiswa = "Mutiara Alfadhilah"
noUjian = "10214122"
jawaban = "B,A,D,D,B"
idKu = ""

# Menyimpan data Siswa

sql = "INSERT INTO testdb (namaSiswa, noUjian, jawaban) VALUES ('%s', '%s', '%s')"%(namaSiswa, noUjian, jawaban)
sql2 = "SELECT id FROM testdb WHERE namaSiswa = '%s'"%(namaSiswa)
try:
    cursor.execute(sql)
    db.commit()
    print ('Data berhasil disimpan')

    cursor.execute(sql2)
    for row in cursor.fetchall():
        idSiswa = row[0]
    print ('Data ID Siswa {} : {}').format(namaSiswa, idSiswa)

    # Menyimpan Data ID ke dalam berkas
    berkas = open("dataID.txt", "w")
    berkas.write(str(idSiswa))
    print ("Data berhasil ditulis")
    berkas.close()

except:
    db.rollback()
    print('Oopss... Ada error nih')

db.close()

