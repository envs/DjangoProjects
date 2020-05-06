import nltk
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.model_selection import KFold, cross_val_score, train_test_split
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

tfidf_vect = TfidfVectorizer(analyzer=clean_text)
X_tfidf = tfidf_vect.fit_transform(data['body_text'])

X_features = pd.concat([data['body_len'], data['punct%'], pd.DataFrame(X_tfidf.toarray())], axis=1)
X_features.head()

# Explore GradientBoostingClassifier Attributes and Hyperparameters
print(dir(GradientBoostingClassifier))
print(GradientBoostingClassifier())

# Build Grid-Search
X_train, X_test, y_train, y_test = train_test_split(X_features, data['label'], test_size=0.2)

def train_GB(est, max_depth, lr):
    gb = GradientBoostingClassifier(n_estimators=n_est, max_depth=max_depth, learning_rate=lr)
    gb_model = gb.fit(X_train, y_train)
    y_pred = gb_model.predict(X_test)
    precision, recall, fscore, support = score(y_test, y_pred, pos_label='spam', average='binary')
    print('Est: {} / Depth: {} / LR: {} ----- Precision: {} / Recall: {} / Accuracy: {}'.format(
        n_est, max_depth, lr,
        round(precision, 3), 
        round(recall, 3), 
        round((y_pred==y_test).sum() / len(y_pred), 3)
    ))

for n_est in [50, 100, 150]:
    for max_depth in [3, 7, 11, 15]:
        for lr in [0.01, 0.1, 1]:
            train_GB(n_est, max_depth, lr)
