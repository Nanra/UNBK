from subprocess import check_output

wifi_ip = check_output(['hostname', '-I'])
print wifi_ip
