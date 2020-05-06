import nltk
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_recall_fscore_support as score
import string

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

# TF-IDF
tfidf_vect = TfidfVectorizer(analyzer=clean_text)
X_tfidf = tfidf_vect.fit_transform(data['body_text'])
X_tfidf_feat = pd.concat([data['body_len'], data['punct%'], pd.DataFrame(X_tfidf.toarray())], axis=1)

#   CountVectorizer
count_vect = CountVectorizer(analyzer=clean_text)
X_count = count_vect.fit_transform(data['body_text'])
X_count_feat = pd.concat([data['body_len'], data['punct%'], pd.DataFrame(X_count.toarray())], axis=1)

X_count_feat.head()

# Exploring Parameter Settings using GridSearchCV

# for X_tfidf_feat
gb = GradientBoostingClassifier()
param = {
    'n_estimators': [100, 150],
    'max_depth': [7, 11, 15],
    'learning_rate': [0.1]
}
gs = GridSearchCV(gb, param, cv=5, n_jobs=-1)
cv_fit_tfidf = gs.fit(X_tfidf_feat, data['label'])
pd.DataFrame(cv_fit_tfidf.cv_results_).sort_values('mean_test_score', ascending=False)[0:5]

# for X_count_feat
gb = GradientBoostingClassifier()
param = {
    'n_estimators': [100, 150],
    'max_depth': [7, 11, 15],
    'learning_rate': [0.1]
}
gs = GridSearchCV(gb, param, cv=5, n_jobs=-1)
cv_fit_count = gs.fit(X_count_feat, data['label'])
pd.DataFrame(cv_fit_count.cv_results_).sort_values('mean_test_score', ascending=False)[0:5]

