#Author: tritran

import requests
import os

print 20 * "-" + "Menu" + 20 * "-"
print "1. Echo public IP"
print "2. Echo random password"
print "3. CountDown Timer (5m)"
print "4. Quit"
print 20 * "-" + "----" + 20 * "-"
question = input("Vui long nhap tuy chon: ")

loop=True
while loop:
        if question == 1:
                print requests.get("http://ipecho.net/plain?").text
                loop = False
        elif question == 2:
                rand = os.system("head /dev/urandom | tr -dc A-Za-z0-9 | head -c 13 ; echo ''")
                loop = False
		elif question == 3:
				count = 300
				while count > 0:
					print count + "...\n"
					count -= 1
				print "PING PONG!!!"
        elif question == 4:
                break
        else:
                print "invalid"
                print 20 * "-" + "Menu" + 20 * "-"
                print "1. Echo public IP"
                print "2. Echo random password"
                print "3. Quit"
                print 20 * "-" + "----" + 20 * "-"
                question = input("Vui long nhap tuy chon: ")
