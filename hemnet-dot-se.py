from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

class elementFromXpath():
	def __init__(self, xpath, what_attribute):
		self.xpath = xpath
		self.attribute = what_attribute

	def getElement(self):
		my_id = driver.find_element_by_xpath(self.xpath)
		output = my_id.get_attribute(self.attribute)
		return output		

driver = webdriver.Chrome()
""" Getting value of the maximum amount of pages that are available on the website.
	In order to do that we find a button by its XPATH and extract the data from the element.
"""
url = "http://www.hemnet.se/bostader?page=1" 
driver.get(url)
doc = driver.page_source
elem = driver.find_element_by_xpath('//*[@id="result"]/div[2]/div/a[3]')
print('Number of pages to parse: ' + elem.text)
max_pages = int (elem.text)

data = []

for page in range(1, 10): #range(1,max_pages) 
	url = "http://www.hemnet.se/bostader?page=" + str(page)
	driver.get(url)
	# Waiting for the browser to fully load and parse the data.
	time.sleep(60)
	print('-' * 50)
	print('Page number: ' + str(page))
	for house_page_number in range(1,11):
		offer_xpath = '//*[@id="search-results"]/li[' + str(house_page_number) + ']/div/a'
		offer_id = driver.find_element_by_xpath(offer_xpath)
		link = offer_id.get_attribute('href')

		data.append([link, house_page_number])
		"""
		print('-' * 50)
		print('Page number: ' + str(page))
		print('House id: ' + str(house_page_number) + '\n' + 'Link: ' + link)
		"""
	for house_page_number in range(12,52):
		offer_xpath = '//*[@id="search-results"]/li[' + str(house_page_number) + ']/div/a'
		offer_id = driver.find_element_by_xpath(offer_xpath)
		link = offer_id.get_attribute('href')
		# 11th element has id12 so we need to abstract 1
		data.append([link, house_page_number])
		"""	
		print('-' * 50)
		print('Page number: ' + str(page))
		print('House id: ' + str(house_page_number) + '\n' + 'Link: ' + link)
		"""


# Data in the house page - /html/head/script[14]/text()
data_new = pd.DataFrame(data)
print('-' * 50)	
#data_new.to_csv('out', sep =',')
data_new.to_excel('file.xlsx', sheet_name = '1')
print('-' * 50)
print("Exiting...")
print('-' * 50)
time.sleep(3)
driver.close()



