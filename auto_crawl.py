import requests
import json
from bs4 import BeautifulSoup


def get_list(count):
	url = 'http://www.autoadsja.com/search.asp?SearchSB=5&page=' + str(count)
	response = requests.get(url)
	html = BeautifulSoup(response.content, 'html.parser')
	rows = html.find_all('a')
	for tr in rows:
		if tr.has_attr("href"):
			if "#" in tr['href'] and "http" in tr['href']:
				k =tr['href']
				response = requests.get(k)
				html = BeautifulSoup(response.content, 'html.parser')
				rows = html.find_all('b')
				for td in rows:
					if "Contact phone" in td.text.strip():
						contact_number =td.text.strip()
						number = contact_number.split(":")
						no = str(number[1])
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
											r = requests.post("http://ecms.jappclassifieds.com/pushservice.asmx/Insert_Phoneno", data={'phoneno':n,'domainname':'http://www.autoadsja.com/'})
											print(r.status_code, r.reason)
										else:
											print (n,"is not valid")
								else:
									print(n,"is valid")
									r = requests.post("http://ecms.jappclassifieds.com/pushservice.asmx/Insert_Phoneno", data={'phoneno':n,'domainname':'http://www.autoadsja.com/'})
									print(r.status_code, r.reason)
						elif len(n) >= 12:
							n = n.split(' ')
							inital = 0
							while inital < len(n):
								if len(n[inital]) >= 7 and len(n[inital]) <= 11:					
									if (n[inital].startswith('0') or n[inital].startswith('6') or n[inital].startswith('9') or n[inital].startswith('7')):
										print (n[inital],"inside is not valid")
									else:
										r = requests.post("http://ecms.jappclassifieds.com/pushservice.asmx/Insert_Phoneno", data={'phoneno':n[inital],'domainname':'http://www.autoadsja.com/'})
										print(r.status_code, r.reason)
										print (n[inital],"inside is valid")
								inital = inital +1					


if __name__ == '__main__':
	count = 0
	while (count < 160):
			get_list(count)
			count = count + 1

		


