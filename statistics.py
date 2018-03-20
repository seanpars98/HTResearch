# to use Dataframes for easy manipulation
import pandas as pd
# to tokenize and lemmatize the bodys and titles
from nltk.stem import WordNetLemmatizer
#for basic visualization during clustering
import matplotlib.pyplot as plt
#helps with visualizations in matplotlib
import seaborn as sns
# will help with standardization of data
from scipy import stats
# where we get the kmeans algorthim 
from sklearn.cluster import KMeans

# make a dataframe object from our csv dataset
data = pd.read_csv('Trafficking_Data.csv')

#make a list of each of the features so we can manipulate them
ids = data['id'].tolist()
titles = data['title'].tolist()
pub_dates = data['pub_date'].tolist()
content = data['body'].tolist()
urls = data['url'].tolist()
ages = data['poster_age'].tolist()
date_collected = data['date_collected'].tolist()

#make a copy of the data
data_copy = data

#encode categorical variables with one hot encoding
def one_hot_encoding(dataframe, columns):

	return pd.get_dummies(dataframe, columns=columns)



data = one_hot_encoding(data, ['region', 'category'])

lemmatizer = WordNetLemmatizer()

print('lemma')