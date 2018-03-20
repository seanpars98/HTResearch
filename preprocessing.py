import pandas as pd

from re import findall

from sklearn.utils import shuffle

data = pd.read_csv('Trafficking_Data.csv')

urls = data['url'].tolist()

regional_data = []
category_data = []

def extract_region(list_of_urls):

	for strings in list_of_urls:
		regdata = findall('http://([A-Za-z]+).', strings)[0]
		regional_data.append(regdata)

def extract_category(list_of_urls):

	for strings in list_of_urls:
		regdata = findall('http://[A-Za-z]+.backpage.com/([A-Za-z]+)', strings)[0]
		category_data.append(regdata)

extract_region(urls)
extract_category(urls)



data['region'] = regional_data
data['category'] = category_data

data = shuffle(data)

data.to_csv('updated.csv', header=True, sep=',')

