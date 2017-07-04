import requests
import json
from bs4 import BeautifulSoup
import re


def get_list(count):
	url = 'http://gleanerclassifieds.com/showads/ad/searchall/keyword//start_price//end_price//title//start_rec/' + str(count) +'/page_size/10/sort/0' 
	response = requests.get(url)
	html = BeautifulSoup(response.content, 'html.parser')
	rows = html.find_all('h3')
	for tr in rows:
		if tr.find('a')['href']:
			k =tr.find('a')['href']
			response = requests.get(k)
			html = BeautifulSoup(response.content, 'html.parser')
			rows = html.find_all('b')
			for row in rows:
				n = row.text.strip()
				print (n)
				n =n.replace('-', '')
				nou=re.findall('\d+', n)
				print (nou)
				initial = 0
				while initial < len(nou):
					if len (nou[initial]) >= 7:
						no = nou[initial]
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
									r = requests.post("http://ecms.jappclassifieds.com/pushservice.asmx/Insert_Phoneno", data={'phoneno':n,'domainname':'http://gleanerclassifieds.com/'})
									print(r.status_code, r.reason)
						elif len(n) >= 12:
							n = n.split(' ')
							inital1 = 0
							while inital1 < len(n):
								if len(n[inital1]) >= 7 and len(n[inital1]) <= 11:					
									if (n[inital1].startswith('0') or n[inital1].startswith('6') or n[inital1].startswith('9') or n[inital1].startswith('7')):
										print (n[inital1],"inside is not valid")
									else:
										r = requests.post("http://ecms.jappclassifieds.com/pushservice.asmx/Insert_Phoneno", data={'phoneno':n[inital1],'domainname':'http://gleanerclassifieds.com/'})
										print(r.status_code, r.reason)
										print (n[inital1],"inside is valid")
								inital1 = inital1 +1		
					initial = initial +1

					


if __name__ == '__main__':
	count = 0
	while (count < 1600):
			get_list(count)
			count = count + 10
