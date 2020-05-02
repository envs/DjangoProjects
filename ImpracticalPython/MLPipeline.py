# ML Pipeline Process are:
# Raw Text ---> Tokenization ---> Clean Text ---> Vectorization ---> ML Algorithm
#
# The Preprocessing Pipeline Process are:
# Remove Punctuation ---> Tokenization ---> Remove Stopwords ---> Lemmatize / Stemming

import pandas as pd
import string
import re
import nltk

pd.set_option('display.max_colwidth', 100)

data = pd.read_csv("SMSSpamCollection.tsv", sep='\t', header=None)
data.columns = ['label', 'body_text']

# Remove punctuation
def remove_punct(text):
    text_nopunct = "".join([char for char in text if char not in string.punctuation])
    return text_nopunct

data['body_text_clean'] = data['body_text'].apply(lambda x : remove_punct(x))
print(data.head())

# Tokenization
def tokenize(text):
    tokens = re.split('\W+', text)
    return tokens

data['body_text_tokenized'] = data['body_text_clean'].apply(lambda x : tokenize(x.lower()))
print(data.head())


# Remove Stopwords
stopword = nltk.corpus.stopwords.words('english')
def remove_stopwords(tokenized_list):
    text = [word for word in tokenized_list if word not in stopword]
    return text

data['body_text_nostop'] = data['body_text_tokenized'].apply(lambda x : remove_stopwords(x))
print(data.head())