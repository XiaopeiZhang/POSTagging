__author__ = 'Xiaopei'

# http://stackoverflow.com/questions/10674832/count-verbs-nouns-and-other-parts-of-speech-with-pythons-nltk
# http://stackoverflow.com/questions/11349333/when-processing-csv-data-how-do-i-ignore-the-first-line-of-data
# https://pypi.python.org/pypi/liac-arff

import nltk, csv
from string import punctuation

alltags = set([])# collect all the tags
tweetsPOS = []# collect text-tag pairs for each tweet
tagcounts = []# collect tag counts for each tweet
wslength = []# collect char per POS and word per sentence for each tweet

with open('Training_set_iteration_3.csv', 'rb') as readfile:
    csvReader = csv.reader(readfile)
    # skip the header
    firstline = True
    for row in csvReader:
        if firstline:
            firstline = False
            continue
        print row
        # concatenate text if separated
        rowtext=''
        for e in row:
            if not e.isdigit():
                if rowtext:rowtext+=','
                rowtext+=e
        print rowtext
        # calculate word per sentence
        num_pun = -2
        for k in rowtext:
            if k in punctuation:
                num_pun += 1
        num_words = len(rowtext.split())
        print num_words, num_pun
        num_pun = max(num_pun, 1)
        wslength.append([0,float(num_words)/num_pun])
        # tag POS and collect all tags and text-tag pairs
        tokens = nltk.word_tokenize(unicode(rowtext, errors='ignore'))
        oneTweet = nltk.pos_tag(tokens)
        print oneTweet
        tweetsPOS.append(oneTweet)
        for part in oneTweet:
            alltags.add(part[1])
alltags = list(alltags)
print(alltags)

# calculate tag counts for each tweet and char per POS
for i, each in enumerate(tweetsPOS):
    dic = {}
    for tag in alltags:
        dic[tag] = 0
    wlen = []
    for part in each:
        wlen.append(len(part[0]))
        dic[part[1]] += 1
    print(dic)
    counts = []
    for tag in alltags:
        counts.append(dic[tag])
    tagcounts.append(counts)
    wslength[i][0] = sum(wlen)/len(wlen)

with open('text_tag_count.csv', 'wb') as writefile:
    csvWriter = csv.writer(writefile)
    csvWriter.writerow(alltags)
    csvWriter.writerows(tagcounts)

with open('word_sentence_count.csv', 'wb') as writefile:
    csvWriter = csv.writer(writefile)
    csvWriter.writerow(['char_per_POS','word_per_sentence'])
    csvWriter.writerows(wslength)