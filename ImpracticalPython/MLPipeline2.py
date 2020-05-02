# ML Pipeline Process are:
# Raw Text ---> Tokenization ---> Clean Text ---> Vectorization ---> ML Algorithm
#
# The Preprocessing Pipeline Process are:
# Remove Punctuation ---> Tokenization ---> Remove Stopwords ---> Lemmatize / Stemming

import pandas as pd
import string
import re
import nltk

ps = nltk.PorterStemmer()
wn = nltk.WordNetLemmatizer
pd.set_option('display.max_colwidth', 100)

data = pd.read_csv("SMSSpamCollection.tsv", sep='\t', header=None)
data.columns = ['label', 'body_text']
stopwords = nltk.corpus.stopwords.words('english')

# Clean up Text - "Remove Punctuation", "Tokenization" & "Remove Stopwords"
def clean_text(text):
    text = "".join([word for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    text = [word for word in tokens if word not in stopwords]
    return text

data['body_text_nostop'] = data['body_text'].apply(lambda x : clean_text(x.lower()))

# Stem Text
def stemming(tokenized_text):
    text = [ps.stem(word) for word in tokenized_text]
    return text

data['body_text_stemmed'] = data['body_text_nostop'].apply(lambda x : stemming(x))

# Lemmatize Text
def lemmatizing(tokenized_text):
    text = [ps.lemmatize(word) for word in tokenized_text]
    return text

data['body_text_lemmatize'] = data['body_text_nostop'].apply(lambda x : lemmatizing(x))