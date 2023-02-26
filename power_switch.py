import optparse
import subprocess

parser = optparse.OptionParser(conflict_handler='resolve')

parser.add_option('-m', '--method', dest='method', help='+ type poweroff, reboot, or halt after you specify --method flag +')


(options, arguments) = parser.parse_args()

method = options.method

if method == 'poweroff':
    print('+ powering off your system +')
    subprocess.run(['sudo', 'systemctl', 'poweroff'])

elif method == 'reboot':
    print('+ rebooting your system +')
    subprocess.run(['sudo', 'systemctl', 'reboot'])

elif method == 'halt':
    print('+ halting your system +')
    subprocess.run(['sudo', 'systemctl', 'halt'])

else:
    print('+ irrelavent user input detected, try --help or -h for instructions +')
    parser.destroy()
    exit()
