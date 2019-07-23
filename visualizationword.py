import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud
from os import path

tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

text = open(path.join(d, 'tweets_small.json')).read()

totalTweets = ""
for tweet in tweetData:
    totalTweets += tweet['text']
tweets = TextBlob(totalTweets)

filteredwords = ["and","about","the","http"]
list = dict()
for word in tweets.words:
    if len(word) > 2:
        continue
    if word.lower() in filteredwords:
        continue
    if not word.isalpha():
        continue
    list[word.lower()] = tweets.word_counts[word.lower()]
wordcloud = WordCloud().generate_from_frequencies(list)
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
view()
