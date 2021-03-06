#!/usr/bin/env python

import subprocess #module for enterig system commands
import re #filiter used to check output
import optparse #module for creating options etc
#COLORS 
TGREEN =  '\033[32m' # Green Text 
RED11 =   '\033[31m' #Red Text
YELLOW22 =  '\033[33m' #Yellow Text
PURP =  '\033[35m' #purple text
BLUE22 = '\033[34m' #blue text
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def handle_args(): 
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='example:"-i or --interface then NAME OF INTERFACE".')
    parser.add_option('-m', '--mac', dest='mac_adress', help='example:"-m or --mac 00:11:22:33:44:55".' + YELLOW22 + 
    ''' EXAMPLES:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


    00:1C:B3 	Apple Inc           00236C 	Apple, Inc                    
    00:1D:4F 	Apple Inc           0023DF 	Apple, Inc          
    00:1E:52 	Apple Inc           002436 	Apple, Inc
    00:1E:C2 	Apple Inc           002500 	Apple, Inc
    00:1F:5B 	Apple Inc           002500 	Apple, Inc
    00:1F:F3 	Apple Inc           00254B 	Apple, Inc
    00:21:E9 	Apple Inc           0025BC 	Apple, Inc
    00:22:41 	Apple Inc           002608 	Apple, Inc
    00:23:12 	Apple Inc           00264A 	Apple, Inc
    00:23:32 	Apple Inc           0026B0 	Apple, Inc              
   









    ''')
    (options, arguments) = parser.parse_args()
    if not options.interface: 
        parser.error(RED11 + '[-] PLEASE PUT A FUCKING INTERFACE or "--help" for help.')
    elif not options.mac_adress:
        parser.error(RED11 + '[-] PLEASE PUT A FUCKING MAC ADRESS')
    return options
def change_mac01(interface, mac_adress):
    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', mac_adress])  
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])
def change_mac02(interface, mac_adress): 
    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', mac_adress])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])
def get_currrent_mac(interface): 
    ifconfig_result = subprocess.check_output(['ifconfig', interface])
    mac_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
    if mac_search_result:
        return (mac_search_result.group(0))
    else:
        print('[-] ERROR COULD NOT READ MAC ADRESS')

options = handle_args() 

current_mac = get_currrent_mac(options.interface) 
print(PURP + 'Current MAC Adress = ' + str(current_mac)) 

change_mac02(options.interface, options.mac_adress) 

print(YELLOW22 + "[+] Changeing MAC Adress for " + options.interface + " to: " + options.mac_adress) 

change_mac02(options.interface, options.mac_adress)
current_mac = get_currrent_mac(options.interface)
if current_mac == options.mac_adress:
    print(TGREEN + '[+] MAC Adress was successfully changed to ' + str(current_mac))
else:
    print(RED11 + '[-] ERROR MAC Adress was not changed')

    
    



