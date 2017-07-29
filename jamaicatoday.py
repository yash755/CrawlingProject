import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unicodedata
import re


def get_list(count):
	url = 'https://www.jamaicatoday.com/advert-category/auto/page/' + str(count) + '/'
	response = requests.get(url)
	html = BeautifulSoup(response.content, 'html.parser')
	rows = html.find_all('div',{'class':'stylish-button'})
	for row in rows:
		links = row.find_all('a')
		for link in links:
			try:
				print link['href']
				if link.has_attr("href"):
					k =link['href']
					driver = webdriver.PhantomJS(service_args=['--ssl-protocol=any'])
					driver.maximize_window()
					driver.get(k)
					time.sleep(5)
					driver.find_element_by_class_name('adverts-icon-down-open').click();
					time.sleep(5)
					driver.save_screenshot('ame.png')
					html2 = driver.page_source
					soup = BeautifulSoup(html2, "lxml", from_encoding="utf-8")
					rows = soup.find_all('a')
					for row in rows:
						if row.has_attr("href"):
							if "tel" in row['href']:
									n = row.text.strip()
									n =n.replace('-', '')
									nou=re.findall('\d+', n)
									initial = 0
									while initial < len(nou):
										print(nou[initial])
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
															r = requests.post("http://ecms.jappclassifieds.com/pushservice.asmx/Insert_Phoneno", data={'phoneno':n,'domainname':'https://www.jamaicatoday.com'})
															print(r.status_code, r.reason)
														else:
															print (n,"is not valid")
													else:
														print(n,"is valid")
														r = requests.post("http://ecms.jappclassifieds.com/pushservice.asmx/Insert_Phoneno", data={'phoneno':n,'domainname':'https://www.jamaicatoday.com'})
														print(r.status_code, r.reason)
											elif len(n) >= 12:
												n = n.split(' ')
												inital1 = 0
												while inital1 < len(n):
													if len(n[inital1]) >= 7 and len(n[inital1]) <= 11:					
														if (n[inital1].startswith('0') or n[inital1].startswith('6') or n[inital1].startswith('9') or n[inital1].startswith('7')):
															print (n[inital1],"inside is not valid")
														else:
															r = requests.post("http://ecms.jappclassifieds.com/pushservice.asmx/Insert_Phoneno", data={'phoneno':n[inital1],'domainname':'https://www.jamaicatoday.com'})
															print(r.status_code, r.reason)
															print (n[inital1],"inside is valid")
													inital1 = inital1 +1		
										initial = initial +1
			except:
				print ("Invalid number")

				


if __name__ == '__main__':
	count = 1
	while (count < 30:
			get_list(count)
			count = count + 1