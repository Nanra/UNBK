#! /usr/bin/python

## Section for testing all buttons function

import RPi.GPIO as GPIO
import time

pinbtnValid   = 31
pinbtnNext    = 5
pinbtnPrev    = 29
pinbtnDelete  = 32
pinbtnEnter   = 3
pinbtnSatu    = 36
pinbtnDua     = 38
pinbtnTiga    = 40
pinbtnEmpat   = 37
pinbtnLima    = 35
pinbtnEnam    = 33
pinbtn        = [pinbtnValid, pinbtnNext, pinbtnPrev, pinbtnDelete, pinbtnEnter, pinbtnSatu, pinbtnDua, pinbtnTiga
, pinbtnEmpat, pinbtnLima, pinbtnEnam]

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Deklarasi Button Huruf Sebagai OUTPUT
i = 0
while i < len(pinbtn):
	GPIO.setup(pinbtn[i], GPIO.IN,pull_up_down=GPIO.PUD_UP)
	i+=1

print "OK MAS BRO"

##Test Button
#while True:
#	inputValue = GPIO.input(pinbtnValid)
#	if (inputValue == False):
#		print "Tombol Ditekan"
#		time.sleep(0.3)

# Fungsi Baca Kode Braille
def braille():
	tom1 = str(GPIO.input(pinbtnSatu))
	tom2 = str(GPIO.input(pinbtnDua))
	tom3 = str(GPIO.input(pinbtnTiga))
	tom4 = str(GPIO.input(pinbtnEmpat))
	tom5 = str(GPIO.input(pinbtnLima))
	tom6 = str(GPIO.input(pinbtnEnam))
	tomvalid = str(GPIO.input(pinbtnValid))
	tomenter = str(GPIO.input(pinbtnEnter))
	tomdelete = str(GPIO.input(pinbtnDelete))
	tomnext = str(GPIO.input(pinbtnNext))
	tomback = str(GPIO.input(pinbtnPrev))
	n = tom3 + tom2 + tom1 + tom4 + tom5 + tom6 + tomvalid + tomenter + tomdelete + tomnext + tomback
	return n

def abjad(n="111111",x=""):
	if (n=="110111"):
		x = "A"
	elif (n=="100111"):
		x = "B"
	elif (n=="110011"):
		x = "C"
	elif (n=="110001"):
		x = "D"
	elif (n=="110101"):
		x = "E"
	elif (n=="100011"):
		x = "F"
	elif (n=="100001"):
		x = "G"
	elif (n=="100111"):
		x = "H"
	elif (n=="101011"):
		x = "I"
	elif (n=="101001"):
		x = "J"
	elif (n=="010111"):
		x = "K"
	elif (n=="000111"):
		x = "L"
	elif (n=="010011"):
		x = "M"
	elif (n=="010001"):
		x = "N"
	elif (n=="010101"):
		x = "O"
	elif (n=="000011"):
		x = "P"
	elif (n=="000001"):
		x = "Q"
	elif (n=="000101"):
		x = "R"
	elif (n=="001011"):
		x = "S"
	elif (n=="001001"):
		x = "T"
	elif (n=="010110"):
		x = "U"
	elif (n=="000110"):
		x = "V"
	elif (n=="101000"):
		x = "W"
	elif (n=="010010"):
		x = "X"
	elif (n=="010000"):
		x = "Y"
	elif (n=="010100"):
		x = "Z"
	elif (n=="011110"):
		x = "-"
	else:
		x = "SALAH"
		#os.system("ogg123 -q audio/wrong.ogg")
	return x


#Deklarasi Angka
def angka(n="111111",x=""):
	if (n=="110111"):
		x = "1"
	elif (n=="100111"):
		x = "2"
	elif (n=="110011"):
		x = "3"
	elif (n=="100011"):
		x = "4"
	elif (n=="110101"):
		x = "5"
	elif (n=="100011"):
		x = "6"
	elif (n=="100001"):
		x = "7"
	elif (n=="100101"):
		x = "8"
	elif (n=="101011"):
		x = "9"
	elif (n=="101001"):
		x = "0"
	else:
		x = "SALAH"
	return x

while True:
	print "Masukkan Karakter : " ,braille()
	#print braille()
	time.sleep(0.5)
