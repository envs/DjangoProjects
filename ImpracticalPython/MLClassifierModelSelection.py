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

# Clean up Text - "Remove Punctuation", "Tokenization" and "Remove Stopwords"
def clean_text(text):
    text = "".join([word for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    text = [ps.stem(word) for word in tokens if word not in stopwords]
    return text

# Split into train/testset
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
# For RandomForestClassifier
rf = RandomForestClassifier(n_estimators=150, max_depth=None, n_jobs=-1)

start = time.time()
rf_model = rf.fit(X_train_vect, y_train)
end = time.time()
fit_time = (end - start)

start = time.time()
y_pred = rf_model.predict(X_test_vect)
end = time.time()
pred_time = (end - start)

precision, recall, fscore, train_support = score(y_test, y_pred, pos_label='spam', average='binary')
print('Fit time: {} / Predict time: {} ------ Precision: {} / Recall: {} / Accuracy: {}'.format(
    round(fit_time, 3), round(pred_time, 3),
    round(precision, 3), round(recall, 3),
    round((y_pred==y_test).sum() / len(y_pred), 3)))

# For GradientBoostingClassifier
gb = GradientBoostingClassifier(n_estimators=150, max_depth=11)

start = time.time()
gb_model = gb.fit(X_train_vect, y_train)
end = time.time()
fit_time = (end - start)

start = time.time()
y_pred = gb_model.predict(X_test_vect)
end = time.time()
pred_time = (end - start)

precision, recall, fscore, train_support = score(y_test, y_pred, pos_label='spam', average='binary')
print('Fit time: {} / Predict time: {} ------ Precision: {} / Recall: {} / Accuracy: {}'.format(
    round(fit_time, 3), round(pred_time, 3),
    round(precision, 3), round(recall, 3),
    round((y_pred==y_test).sum() / len(y_pred), 3)))