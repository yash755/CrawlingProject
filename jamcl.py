import requests
import json
from bs4 import BeautifulSoup
import re


def get_list(count):
	url = 'http://jamcl.com/page/' + str(count) 
	response = requests.get(url)
	html = BeautifulSoup(response.content, 'html.parser')
	rows = html.find_all('h3',{'class':'acadp-no-margin'})
	for tr in rows:
		if tr.find('a')['href']:
		 	k =tr.find('a')['href']
			response = requests.get(k)
			html = BeautifulSoup(response.content, 'html.parser')
			rows = html.find_all('span',{'class':'acadp-phone'})
			for row in rows:
				k = row.text.strip()
				k = k.replace('(','')
				k = k.replace(')','')
				k =k.replace('-', '')
				if 'Tel:' in k:
					s = k.split(':')
					if '/' in s[1]:
						number = s[1].split('/')
						inti = 0
						while inti < len(number):
							add_db(number[inti])
							inti = inti + 1
					else:
						add_db (s[1])
				else:
					if '/' in k:
						number = k.split('/')
						inti2 = 0
						while inti2 < len(number):
							add_db(number[inti2])
							inti2 = inti2 + 1
					else:
						add_db(k)
						n = k

def add_db(n):
	n = n.lstrip()
	n =n.replace(' ','')
	if len(n) <= 11:
		if (n.startswith('0') or n.startswith('6') or n.startswith('9') or n.startswith('7')):
			print (n,"is not valid")
		else:
			if n.startswith('1'):
				if len(n) == 11:
					print (n,"is valid")
					r = requests.post("http://ecms.jappclassifieds.com/pushservice.asmx/Insert_Phoneno", data={'phoneno':n,'domainname':'http://jamcl.com/'})
					print(r.status_code, r.reason)
				else:
					print (n,"is not valid")
			else:
				print(n,"is valid")
				r = requests.post("http://ecms.jappclassifieds.com/pushservice.asmx/Insert_Phoneno", data={'phoneno':n,'domainname':'http://jamcl.com/'})
				print(r.status_code, r.reason)
	

					


if __name__ == '__main__':
	count = 0
	while (count < 150):
			get_list(count)
			count = count + 1
