import requests
import json
from bs4 import BeautifulSoup


def get_list(count):
	url = 'http://jamaicaclassifiedonline.com/' + str(count)
	response = requests.get(url)
	html = BeautifulSoup(response.content, 'html.parser')
	rows = html.find_all('div',{'class':'card-image'})
	for row in rows:
		k = row.find('a')['href']
		response = requests.get(k)
		html = BeautifulSoup(response.content, 'html.parser')
		# try:
		if html.find("a", {"class": "btn waves-effect waves-light amber black-text"}) is not None:
			rows = html.find("a", {"class": "btn waves-effect waves-light amber black-text"})
			h = rows['href']
			m = h.split(":")
			n = m[1]
			n = n.lstrip()
			n =n.replace('-', '')
			if len(n) <= 11:
				n =n.replace(' ','')
				if (n.startswith('0') or n.startswith('6') or n.startswith('9') or n.startswith('7')):
					print (n,"is not valid")
				else:
					if n.startswith('1'):
							if len(n) == 11:
								print (n,"is valid")
								r = requests.post("http://ecms.jappclassifieds.com/pushservice.asmx/Insert_Phoneno", data={'phoneno':n,'domainname':'http://jamaicaclassifiedonline.com/'})
								print(r.status_code, r.reason)
							else:
								print (n,"is not valid")
					else:
						print(n,"is valid")
						r = requests.post("http://ecms.jappclassifieds.com/pushservice.asmx/Insert_Phoneno", data={'phoneno':n,'domainname':'http://jamaicaclassifiedonline.com/'})
						print(r.status_code, r.reason)
			elif len(n) >= 12:
				n = n.split(' ')
				inital = 0
				while inital < len(n):
						if len(n[inital]) >= 7 and len(n[inital]) <= 11:					
							if (n[inital].startswith('0') or n[inital].startswith('6') or n[inital].startswith('9') or n[inital].startswith('7')):
								print (n[inital],"inside is not valid")
							else:
								r = requests.post("http://ecms.jappclassifieds.com/pushservice.asmx/Insert_Phoneno", data={'phoneno':n[inital],'domainname':'http://jamaicaclassifiedonline.com/'})
								print(r.status_code, r.reason)
								print (n[inital],"inside is valid")
						inital = inital +1	



if __name__ == '__main__':
	count = 0
	while (count < 150):
			get_list(count)
			count = count + 1


		