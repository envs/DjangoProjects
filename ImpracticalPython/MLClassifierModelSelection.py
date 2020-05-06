import nltk
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support as score
import string
import time

stopwords = nltk.corpus.stopwords.words('english')
ps = nltk.PorterStemmer()

data = pd.read_csv("SMSSpamCollection.tsv", sep="\t")
data.columns = ['label', 'body_text']

def count_punct(text):
   count = sum([1 for char in text if char in string.punctuation])
   return round(count / (len(text) - text.count(" ")), 3) * 100

data['body_len'] = data['body_text'].apply(lambda x: len(x) - x.count(" "))
data['punct%'] = data['body_text'].apply(lambda x : count_punct(x))

# Clean up Text - "Remove Punctuation", "Tokenization" & "Remove Stopwords"
def clean_text(text):
    text = "".join([word for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    text = [ps.stem(word) for word in tokens if word not in stopwords]
    return text

# Split into train/test set
X_train, X_test, y_train, y_test = train_test_split(data[['body_text', 'body_len', 'punct%']], data['label'], test_size=0.2)

# Vectorize Text using TF-IDF (NB: We separate the fit_transform into 'fit' and 'transform' step. This helps us transform the test set separately)
# We would then concatenate them back with 'body_len' and 'punct%' which are already numerical
tfidf_vect = TfidfVectorizer(analyzer=clean_text)
tfidf_vec_fit = tfidf_vect.fit(X_train['body_text'])

tfidf_train = tfidf_vec_fit.transform(X_train['body_text'])
tfidf_test = tfidf_vec_fit.transform(X_test['body_text'])

X_train_vect = pd.concat([X_train[['body_len', 'punct%']].reset_index(drop=True), 
            pd.DataFrame(tfidf_train.toarray())], axis = 1)

X_test_vect = pd.concat([X_test[['body_len', 'punct%']].reset_index(drop=True), 
            pd.DataFrame(tfidf_test.toarray())], axis = 1)

X_train_vect.head()
X_test_vect.head()


# FINAL Evaluation of Models
rf = RandomForestClassifier