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
    text = " ".join([ps.stem(word) for word in tokens if word not in stopwords])            # Recreating a string again from our tokens
    return text

data['cleaned_text'] = data['body_text'].apply(lambda x : clean_text(x))
print(data.head())


# Apply CountVectorizer (w/N-Gram)
ngram_vect = CountVectorizer(ngram_range=(2,2))
X_counts = ngram_vect.fit_transform(data['cleaned_text'])
print(X_counts.shape)
print(ngram_vect.get_feature_names())           # prints out all unique words used in our text

# To view X_counts as a DataFrame
X_counts_df = pd.DataFrame(X_counts.toarray())
X_counts_df.columns = ngram_vect.get_feature_names()       # To map the Column names to the Array Number Columns
print(X_counts_df)