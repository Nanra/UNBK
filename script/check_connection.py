# Test Connection to server
from subprocess import check_output
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)


wifi_ip = check_output(['hostname', '-I'])
if wifi_ip is not None:
    print "Koneksi OK..."
    print "IP Address = {}".format(wifi_ip)
    GPIO.output(16, True)
else:
    print "Tidak terhubung dengan Server"
    GPIO.output(16, False)
