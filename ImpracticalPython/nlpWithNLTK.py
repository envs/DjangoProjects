import pandas as pd

# # Read in the raw text
# rawData = open("SMSSpamCollection.tsv").read()
# parsedData = rawData.replace("\t", "\n").split("\n")

# # Separate 'Labels' from 'Texts'
# labelList = parsedData[0::2]
# textList = parsedData[1::2]

# fullCorpus = pd.DataFrame({
#     'label': labelList[:-1],
#     'body_list': textList
# })
# print(fullCorpus[:5])

# The easiest way to read the data is
fullCorpus = pd.read_csv("SMSSpamCollection.tsv", sep="\t", header=None)
fullCorpus.columns = ['Label', 'Body_Text']

# EXPLORE THE DATASET (What is the shape of the dataset?, How many spam/ham are in the dataset?, How much missing data is there?)
print("Input data has {} rows and {} columns\n".format(len(fullCorpus), len(fullCorpus.columns)))

print("Out of {} row, {} are spam, and {} are ham\n".format(len(fullCorpus),
                                                        len(fullCorpus[fullCorpus['Label']=='spam']),
                                                        len(fullCorpus[fullCorpus['Label']=='ham'])))

print("Number of null in Label: {}".format(fullCorpus['Label'].isnull().sum()))
print("Number of null in Text: {}".format(fullCorpus['Body_Text'].isnull().sum()))