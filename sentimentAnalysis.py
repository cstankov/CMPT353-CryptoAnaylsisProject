import pandas
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

def sentimentAnalysis(tweet_data):
    print("Running Sentiment Analysis...")
    tweet_data['sentiment'] = tweet_data['tweet'].apply(getSentimentScore)
    return tweet_data