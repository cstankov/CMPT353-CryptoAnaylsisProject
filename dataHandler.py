from numpy import datetime64, string_
from cryptoAnalysis import *

def preprocess_data():
    BASE_PATH = os.path.dirname(__file__)
    RAW_PATH = '/raw_data/'
    PROCESSED_PATH = '/processed_data/'
    if data_already_preprocessed(BASE_PATH, PROCESSED_PATH):
        print("Data has already been preprocessed. Loading from existing files...")
        return load_preprocessed_data(BASE_PATH, PROCESSED_PATH)
    else:
        return process_data()

#########################################################
# PROCESS DATA

def process_data():
    eth_data, btc_data, tweet_data = loadRawData()
    # visualize_raw_data(eth_data, btc_data, tweet_data) # Display raw data
    tweet_data = process_tweet_data(tweet_data)
    eth_data = process_eth_data(eth_data)
    btc_data = process_btc_data(btc_data)
    eth_tweet_data, btc_tweet_data = merge_crypto_with_tweets(eth_data, btc_data, tweet_data)
    write_processed_data(eth_tweet_data, btc_tweet_data)
    return eth_tweet_data, btc_tweet_data
    
def process_tweet_data(tweet_data):
    # tweet_data = sentimentAnalysis(tweet_data)
    # tweet_data = tweet_data.sort_values(by='date', ascending=True).reset_index()
    tweet_data = pd.read_csv('test.csv', sep='\t')
    tweet_data = calculate_average_sentiment(tweet_data)
    tweet_data['date'] = pd.to_datetime(tweet_data['date'])
    tweet_data = tweet_data.rename({'date':'Date'}, axis=1)
    return tweet_data

def calculate_average_sentiment(tweet_data):
    tweet_data['new_sent_score'] = tweet_data['likes_count'] * tweet_data['sentiment']
    tweet_data.drop(['tweet', 'sentiment'], axis=1, inplace=True)
    tweet_data = tweet_data.groupby(['date'], as_index=False).sum()
    tweet_data['sentiment'] = tweet_data['new_sent_score'] / tweet_data['likes_count']
    tweet_data.drop(['index', 'likes_count', 'new_sent_score'], axis=1, inplace=True)
    return tweet_data 

def process_eth_data(eth_data):
    return eth_data.dropna().reset_index(drop=True)

def process_btc_data(btc_data):
    return btc_data.dropna().reset_index(drop=True)

#########################################################
# MERGE DATA

def merge_crypto_with_tweets(eth_data, btc_data, tweet_data):
    eth_tweet_data = eth_data.merge(tweet_data, on='Date', how='inner')
    btc_tweet_data = btc_data.merge(tweet_data, on='Date', how='inner')
    return eth_tweet_data, btc_tweet_data

#########################################################
# WRITE DATA

def write_processed_data(eth_tweet_data, btc_tweet_data):
    BASE_PATH = os.path.dirname(__file__)
    PROCESSED_PATH = '/processed_data/'
    eth_tweet_data.to_csv(getRelPath(BASE_PATH, PROCESSED_PATH,'ETH-USD-Processed.csv'), index=False)
    btc_tweet_data.to_csv(getRelPath(BASE_PATH, PROCESSED_PATH,'BTC-USD-Processed.csv'), index=False)

#########################################################
# LOAD DATA

def load_preprocessed_data(BASE_PATH, PROCESSED_PATH):
    eth_data = pd.read_csv(getRelPath(BASE_PATH, PROCESSED_PATH,'ETH-USD-Processed.csv'))
    btc_data = pd.read_csv(getRelPath(BASE_PATH, PROCESSED_PATH, 'BTC-USD-Processed.csv'))
    return eth_data, btc_data

def loadRawData():
    BASE_PATH = os.path.dirname(__file__)
    RAW_PATH = '/raw_data/'
    na_lst = ['#N/A', '#N/A', 'N/A', '#NA', '-1.#IND', '-1.#QNAN', '-NaN', '-nan', '1.#IND', '1.#QNAN', '<NA>', 'N/A', 'NA', 'NULL', 'NaN', 'n/a', 'nan', 'null', 'Unknown', 'unknown']
    eth_data = load_raw_eth_data(BASE_PATH, RAW_PATH, na_lst)
    btc_data = load_raw_btc_data(BASE_PATH, RAW_PATH, na_lst)
    tweet_data = load_raw_tweet_data(BASE_PATH, RAW_PATH, na_lst)
    return eth_data, btc_data, tweet_data

def load_raw_btc_data(BASE_PATH, RAW_PATH, na_lst):
    fields = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    return pd.read_csv(getRelPath(BASE_PATH, RAW_PATH, 'BTC-USD.csv'), na_values=na_lst, parse_dates=['Date'])

def load_raw_eth_data(BASE_PATH, RAW_PATH, na_lst):
    fields = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    return pd.read_csv(getRelPath(BASE_PATH, RAW_PATH,'ETH-USD.csv'), usecols=fields,  na_values=na_lst, parse_dates=['Date'])

def load_raw_tweet_data(BASE_PATH, RAW_PATH, na_lst):
    fields = ['date', 'tweet', 'likes_count']
    dtype = {'tweet':str, 'likes_count':int}
    parse_dates=['date']
    return pd.read_csv(getRelPath(BASE_PATH, RAW_PATH, 'tweets.csv'), usecols=fields, na_values=na_lst, dtype=dtype, parse_dates=parse_dates, sep ='\t')

def getRelPath(BASE_PATH, PROCESSED_PATH, SUB_PATH):
    return BASE_PATH + PROCESSED_PATH + SUB_PATH

#########################################################
# DETECTING PROCESSED DATA

def data_already_preprocessed(BASE_PATH, PROCESSED_PATH):
    return ethDatasetPreprocessed(BASE_PATH, PROCESSED_PATH) and \
        btcDatasetPreprocessed(BASE_PATH, PROCESSED_PATH)

def ethDatasetPreprocessed(BASE_PATH, PROCESSED_PATH):
    return os.path.exists(getRelPath(BASE_PATH, PROCESSED_PATH,'ETH-USD-Processed.csv'))

def btcDatasetPreprocessed(BASE_PATH, PROCESSED_PATH):
    return os.path.exists(getRelPath(BASE_PATH, PROCESSED_PATH,'BTC-USD-Processed.csv'))
