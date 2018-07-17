# Test Connection to server
from subprocess import check_output

wifi_ip = check_output(['hostname', '-I'])
if wifi_ip is not None:
    print "Koneksi OK..."
    print "IP Address = {}".format(wifi_ip)
else:
    print "Tidak terhubung dengan Server"
