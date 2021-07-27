import pandas as pd
from dataHandler import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def getSentimentScore(tweet):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(tweet)
    return score['compound']

def getSentiment(tweet):
    sentiment_score = getSentimentScore(tweet)
    if(sentiment_score == 0):
        return 'neutral'
    elif(sentiment_score < 0):
        return 'negative'
    elif(sentiment_score > 0):
        return 'positive'

def sentimentAnalysis(elon_data):
    elon_data['sentiment'] = elon_data['tweet'].apply(getSentiment)
    #elon_data['sentiment score'] = elon_data['tweet'].apply(getSentimentScore)
    #elon_data.to_csv('sentiment.csv')