import nltk     #Natural Language Toolkit
from nltk.corpus import stopwords
from string import punctuation
import heapq

#Read text from file input.txt
text = open("input.txt","r").read()

#cleaning up data by removing puncutations and stopwords
clean_text = [word for word in text if word not in punctuation]
clean_text = "".join(clean_text)
clean_text = [word for word in clean_text.split() if word.lower() not in stopwords.words('english')]

#calculating frequency of each word
freq = {}
for word in clean_text:
    if word not in freq.keys():
        freq[word]=1
    else:
        freq[word] += 1

max_freq = max(freq.values())
for word in freq:
    freq[word] /=max_freq

#scoring sentence on basis of weight of words
sentence_score={}
sentences = nltk.sent_tokenize(text)
for sent in sentences:
    for word in nltk.word_tokenize(sent.lower()):
        if word in freq:
            if sent not in sentence_score:
                sentence_score[sent] = freq[word]
            else:
                sentence_score[sent] += freq[word]

#choosing roughly 35% of sentences for summary
num_sent = int(len(sentences)*0.35)

#computing summary and overwriting the content of file output.txt
summary = heapq.nlargest(num_sent,sentence_score,sentence_score.get)
summary="".join(summary)
f = open("output.txt","w")
f.write(summary)
f.close()