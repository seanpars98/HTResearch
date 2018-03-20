#import data processing module
import pandas as pd
#import ploting and visualization module
import matplotlib.pyplot as plt
#need regular expressions for parsing
import re
#easy counter for lists
from collections import Counter

#read the data into a Pandas dataframe for easy manipulation from the CSV file
data = pd.read_csv('Trafficking_Data.csv')

#print the first 5 rows of the dataframe/file
#print(data.head())

#clone the different columns into manipulatable lists
ids = data['id'].tolist()
titles = data['title'].tolist()
pub_dates = data['pub_date'].tolist()
content = data['body'].tolist()
urls = data['url'].tolist()
ages = data['poster_age'].tolist()
date_collected = data['date_collected'].tolist()

#test loop to print titles then content in more organized rows
#for i, j in zip(titles, content):
	#print('Title: \n', i, '\nBody: \n', j, '\n----------------------------------------')


#############################Phone Number Extraction###############################

#method that finds a phone number within title or description of ad
def find_phone(text):

	#regex testing a variety of phone number formats

	#000-000-0000
	#000 000 0000
	#000.000.0000

	#(000)000-0000
	#(000)000 0000
	#(000)000.0000
	#(000) 000-0000
	#(000) 000 0000
	#(000) 000.0000

	#000-0000
	#000 0000
	#000.0000

	#0000000
	#0000000000
	#(000)0000000

	reg = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')

	#results found stored in results
	results = reg.findall(text)

	#return the matches that we found
	return results

#initialize the results list
true_results = []
clean_results = []
dups_results = []

#iterate through the titles and call the method which finds a phone number
#for i in titles:
	#true_results += find_phone(text=i)

#iterate through the descriptions and call the method which finds the phone number
for i in content:
	true_results += find_phone(text=str(i))

#print the results on whether a number was found
print(true_results)
print('\n', len(true_results))

#sift through and return the numbers that repeat more than once
dups_results = [k for k, v in Counter(true_results).items() if v > 1]

#prints the duplicate numbers and the count of dups
print(dups_results)
print(len(dups_results))

###################################################################################





########################## Basic Word Pattern recognition ##########################





#data['poster_age'].hist(bins=10)

#plt.show()



