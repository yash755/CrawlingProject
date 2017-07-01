import requests
import json
from bs4 import BeautifulSoup


def get_list(count):
	url = 'http://www.jacars.net/?page=browse&p=' + str(count)
	response = requests.get(url)
	html = BeautifulSoup(response.content, 'html.parser')
	rows = html.find_all('a',{'class':'Tel_mobile'})
	for tr in rows:
		k = tr['href']
		k = k.split(':')
		no = k[1]
		n = no.lstrip()
		n =n.replace('-', '')
		if len(n) <= 11:
			n =n.replace(' ','')
			if (n.startswith('0') or n.startswith('6') or n.startswith('9') or n.startswith('7')):
				print (n,"is not valid")
			else:
				if n.startswith('1'):
					if len(n) == 11:
						print (n,"is valid")
						r = requests.post("http://ecms.jappclassifieds.com/pushservice.asmx/Insert_Phoneno", data={'phoneno':n,'domainname':'http://www.jacars.net/'})
						print(r.status_code, r.reason)
					else:
						print (n,"is not valid")
				else:
					print(n,"is valid")
					r = requests.post("http://ecms.jappclassifieds.com/pushservice.asmx/Insert_Phoneno", data={'phoneno':n,'domainname':'http://www.jacars.net/'})
					print(r.status_code, r.reason)
		elif len(n) >= 12:
			print (n[inital],"inside is valid")			



if __name__ == '__main__':
	count = 0
	while (count < 60):
			get_list(count)
			count = count + 1
			print (count)

