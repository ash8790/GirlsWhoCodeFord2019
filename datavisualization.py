import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud
from os import path

tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

subjectivity = []
polarity =[]

for tweet in tweetData:
    tweetblob = TextBlob(tweet["text"])
    polarity.append(tweetblob.polarity)
    subjectivity.append(tweetblob.subjectivity)

print(polarity)
print(subjectivity)
print(sum(polarity)/len(tweetData))
print(sum(subjectivity)/len(tweetData))

import matplotlib.pyplot as plt
import numpy as np

plt.plot(polarity, subjectivity, "ro")
plt.xlabel('Polarity Levels')
plt.ylabel('Subjectivity Levels')
plt.title('Scatterplot of Polarity vs. Subjectivity')
plt.axis(range=[-1.1,1.1])
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

plt.hist(polarity, 20, range =[-1,1])
plt.xlabel('Polarity Levels')
plt.ylabel('Frequency')
plt.title('Histogram of Polarity')
plt.axis([-0.1, 0.5,7,55])
plt.grid(True)
plt.show()

plt.hist(subjectivity, bins=[0.0,0.5, 1])
plt.xlabel('Subjectivity Levels')
plt.ylabel('Frequency')
plt.title('Histogram of Subjectivity')
plt.axis([-0.25, 1.25, 7, 70])
plt.grid(True)
plt.show()

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

text = open(path.join(d, 'tweets_small.json')).read()

totalTweets = ""
for tweet in tweetData:
    totalTweets += tweet['text']
tweets = TextBlob(totalTweets)

filteredwords = ["and","about","the","http"]
list = dict()
for word in tweets.words:
    if len(word) > 2 and word.isalpha() and word.lower() not in filteredwords:
        list[word.lower()] = tweets.word_counts[word.lower()]



wordcloud = WordCloud().generate_from_frequencies(list)
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()

filteredwords = {}

def check_viable(string):
        if check_num()

#wordcloud = WordCloud(font_path = "C:\Users\Ash\Documents",
                          # stopwords=STOPWORDS,
                          # background_color='white',
                          # width=1200,
                          # height=1000)
#generate(word_string)
