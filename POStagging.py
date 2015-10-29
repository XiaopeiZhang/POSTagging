__author__ = 'Xiaopei'

# http://textminingonline.com/dive-into-nltk-part-iii-part-of-speech-tagging-and-pos-tagger
# http://stackoverflow.com/questions/14674275/python-skip-first-linefield-in-loop-using-csv-file

import nltk
import csv

text_tag = []

with open('Training_set_iteration_3.csv', 'rb') as readfile:
    csvReader = csv.reader(readfile)
    firstline = True
    for row in csvReader:
        if firstline:
            firstline = False
            continue
        print row
        rowtext=''
        for e in row:
            if not e.isdigit():
                if rowtext:rowtext+=','
                rowtext+=e
        print rowtext
        tokens = nltk.word_tokenize(unicode(rowtext, errors='ignore'))
        oneTweet = nltk.pos_tag(tokens)
        print(oneTweet)
        print(oneTweet[0][1])
        text_tag.append(oneTweet)
with open('text_tag.csv', 'wb') as writefile:
    csvWriter = csv.writer(writefile)
    csvWriter.writerows(text_tag)
