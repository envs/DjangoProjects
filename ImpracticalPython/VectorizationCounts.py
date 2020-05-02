import pandas as pd
import string
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer

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

# Apply CountVectorizer
count_vect = CountVectorizer(analyzer=clean_text)
X_counts = count_vect.fit_transform(data['body_text'])
print(X_counts.shape)
print(count_vect.get_feature_names())           # prints out all unique words used in our text

# To view X_counts as a DataFrame
X_counts_df = pd.DataFrame(X_counts.toarray())
X_counts_df.columns = count_vect.get_feature_names()       # To map the Column names to the Array Number Columns
print(X_counts_df)  