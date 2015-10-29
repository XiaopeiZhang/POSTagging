__author__ = 'Xiaopei'

# http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('Training_set_iteration_3.csv', header=None, sep=',', names=['tweets', 'url', 'attributes'])   # columns names if no header
vect = TfidfVectorizer(decode_error='ignore')
X = vect.fit_transform(df['tweets'])
Y = df['attributes']

clf = MultinomialNB().fit(X, Y)

doc_new = ['Happy new year! Best wishes for Chicago!','Event Tomorrow 2pm.']
X_new = vect.transform(doc_new)

predicted = clf.predict(X_new)

for doc, category in zip(doc_new, predicted):
    print(doc, category)