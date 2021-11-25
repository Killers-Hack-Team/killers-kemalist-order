import argparse
import requests, json
import sys
from sys import argv
import os

parser = argparse.ArgumentParser()

parser.add_argument ("-i", help= "IPAdres", type=str, dest='IP', required=True )

args = parser.parse_args()

red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

#banner kısmı
print (red+"""
                                                 
 ___ ___ ___ ___ 
|   Y   |   Y   |
|.  1  /|   |   |
|.  _  \|____   |
|:  |   \   |:  |
|::.| .  )  |::.|
`--- ---'   `---'     
                                                                                    
                                                      v 1.0
"""+red)
print (lgreen+bold+"         ANZ tarafından kodlandı \n"+clear)
print (yellow+bold+"   <!--BlackVision's--> \n"+clear)


ip = args.IP

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[ANZ]"
        b = cyan+bold+"[ANZ]"
        print (a, "Ip adres:", data['query'])
        print()
        print (b, "ISP:", data['isp'])
        print()
        print (b, "Şehir:", data['city'])
        print()
        print (a, "Şehir Kod/Plaka Kod:", data['region'])
        print()
        print (b, "Zaman Dilimi:", data['timezone'])
        print()
        print (a, "Zip Kod:", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Kapatıyoruz.., Bye.'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[!]"+" internet hatası!"+clear)
sys.exit(1)