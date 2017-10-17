email = input("Geef uw howest email op: ")

import re

addressToVerify = email
match = re.match('^[a-z]+\.[a-z]*@student.howest.be$', email)

if match == None:
	print('Dit is geen geldig email adres.')
else:
    print('Dit is een geldig email adres.')
