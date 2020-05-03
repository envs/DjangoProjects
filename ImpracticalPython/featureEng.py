import pandas as pd
import string
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("SMSSpamCollection.tsv", sep="\t")
data.columns = ['label', 'body_text']

# Create Feature for Text Message Length
data['body_len'] = data['body_text'].apply(lambda x: len(x) - x.count(" "))

# Create feature for % of text that is punctuation
def count_punct(text):
   count = sum([1 for char in text if char in string.punctuation])
   return round(count / (len(text) - text.count(" ")), 3) * 100

data['punct%'] = data['body_text'].apply(lambda x : count_punct(x))

# Evaluate Created Features
bins = np.linspace(0, 200, 40)
plt.hist(data[data['label'] == 'spam']['body_len'], bins=bins, alpha=0.5, normed=True, label='spam')
plt.hist(data[data['label'] == 'ham']['body_len'], bins=bins, alpha=0.5, normed=True, label='ham')
plt.legend(loc='upper left')
plt.show()

bins = np.linspace(0, 50, 40)
plt.hist(data[data['label'] == 'spam']['punct%'], bins=bins, alpha=0.5, normed=True, label='spam')
plt.hist(data[data['label'] == 'ham']['punct%'], bins=bins, alpha=0.5, normed=True, label='ham')
plt.legend(loc='upper right')
plt.show()