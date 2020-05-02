import pandas as pd
import string
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer


pd.set_option('display.max_colwidth', 100)
stopwords = nltk.corpus.stopwords.words('english')
ps = nltk.PorterStemmer()

data = pd.read_csv("SMSSpamCollection.tsv", sep='\t', header=None)
data.columns = ['label', 'body_text']


# Clean up Text - "Remove Punctuation", "Tokenization", "Remove Stopwords" & "Stem"
def clean_text(text):
    text = "".join([word.lower() for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    text = [ps.stem(word) for word in tokens if word not in stopwords]
    return text


# Apply TFIDF Vectorizer
tfidf_vect = TfidfVectorizer(analyzer=clean_text)
X_tfidf = tfidf_vect.fit_transform(data['body_text'])
print(X_tfidf.shape)
print(tfidf_vect.get_feature_names())           # prints out all unique words used in our text

# To view X_counts as a DataFrame
X_tfidf_df = pd.DataFrame(X_tfidf.toarray())
X_tfidf_df.columns = tfidf_vect.get_feature_names()       # To map the Column names to the Array Number Columns
print(X_tfidf_df)