import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def visualize_raw_data(eth_data, btc_data, tweet_data):
    FIGURE_PATH = 'figures/'
    visualize_eth_raw_data(eth_data, FIGURE_PATH)
    visualize_btc_raw_data(btc_data, FIGURE_PATH)
    visualize_tweet_raw_data(tweet_data, FIGURE_PATH)

#########################################################
# Tweet Raw Visualization

def visualize_tweet_raw_data(tweet_data, FIGURE_PATH):
    print("Tweet dataset headers: ", tweet_data.columns.tolist())
    print_nan_values(tweet_data, "Total NAN values for Tweet dataset:\n")
    write_user_id(tweet_data, FIGURE_PATH + "user-id.csv")
    plot_likes_count_with_outliers(tweet_data, FIGURE_PATH + 'Tweet-likes-count-outliers.png')
    plot_likes_count_reduced_outliers(tweet_data, FIGURE_PATH + 'Tweet-likes-count-no-outliers.png')
    plot_number_of_users_tweets(tweet_data, FIGURE_PATH + 'Tweet-Users-tweets.png')
    plot_total_number_of_likes(tweet_data, FIGURE_PATH + 'Tweet-total-user-likes.png')
    plot_tweets_per_year(tweet_data, FIGURE_PATH + 'Tweet-tweets-per-year.png')    

def write_user_id(tweet_data, FIGURE_PATH):
    users = tweet_data.groupby('name').sum().reset_index()
    users = users.drop('likes_count', axis=1)
    users.to_csv(FIGURE_PATH)

def plot_likes_count_with_outliers(tweet_data, FIGURE_PATH):
    plt.clf()
    plt.boxplot(tweet_data['likes_count'])
    plt.title('Number of likes for the tweets')
    plt.xlabel('Like Number range')
    plt.ylabel('Count')
    plt.savefig(FIGURE_PATH)    

def plot_likes_count_reduced_outliers(tweet_data, FIGURE_PATH):
    plt.clf()
    removed_outliers = tweet_data[tweet_data['likes_count'] < 500]
    plt.boxplot(removed_outliers['likes_count'])
    plt.title('Number of likes for the tweets reduced outliers')
    plt.xlabel('Like Number range')
    plt.ylabel('Count')
    plt.savefig(FIGURE_PATH)

def plot_total_number_of_likes(tweet_data, FIGURE_PATH):
    plt.clf()
    users = tweet_data.groupby('name').sum().reset_index()
    plt.title('Total Number of likes per user')
    plt.xlabel('User Id')
    plt.ylabel('Total Likes Count')
    plt.bar(users.index.values, users['likes_count'])
    plt.savefig(FIGURE_PATH)

def plot_number_of_users_tweets(tweet_data, FIGURE_PATH):
    plt.clf()
    users = pd.DataFrame({'count' : tweet_data.groupby('name').size()}).reset_index()
    plt.bar(users.index.values, users['count'])
    plt.title('Number of tweets per user')
    plt.xlabel('User ID')
    plt.ylabel('Count')
    plt.savefig(FIGURE_PATH)

def plot_tweets_per_year(tweet_data, FIGURE_PATH):
    plt.clf()
    plt.title('Number of tweets per year')
    plt.xlabel('Year')
    plt.ylabel('Count')
    date = tweet_data.groupby(tweet_data.date.dt.year).sum().reset_index()
    plt.bar(date['date'], date['likes_count'])
    plt.savefig(FIGURE_PATH)

#########################################################
# ETH Raw Visualization

def visualize_eth_raw_data(eth_data, FIGURE_PATH):
    print("Ethereum dataset headers: ", eth_data.columns.tolist())
    print_nan_values(eth_data, "Total NAN values for ETH dataset:\n")
    plot_crypto_opening_price(eth_data, FIGURE_PATH + 'ETH-open.png', 'Opening Price of Ethereum')
    plot_crypto_closing_price(eth_data, FIGURE_PATH + 'ETH-close.png', 'Closing Price of Ethereum')
    plot_crypto_high_vs_low(eth_data, FIGURE_PATH + 'ETH-highVsLow.png', 'High Vs Low 2021 Price of Ethereum')
    plot_crypto_volume(eth_data, FIGURE_PATH + 'ETH-volume.png', 'Volume of Ethereum')

#########################################################
# BTC Raw Visualization

def visualize_btc_raw_data(btc_data, FIGURE_PATH):
    print("Bitcoin dataset headers: ", btc_data.columns.tolist())
    print_nan_values(btc_data, "Total NAN values for BTC dataset:\n")
    plot_crypto_opening_price(btc_data, FIGURE_PATH + 'BTC-open.png', 'Opening Price of Bitcoin')
    plot_crypto_closing_price(btc_data, FIGURE_PATH + 'BTC-close.png', 'Closing Price of Bitcoin')
    plot_crypto_high_vs_low(btc_data, FIGURE_PATH + 'BTC-highVsLow.png', 'High Vs Low 2021 Price of Bitcoin')
    plot_crypto_volume(btc_data, FIGURE_PATH + 'BTC-volume.png', 'Volume of Bitcoin')

#########################################################
# Crypto Raw Visualization

def plot_crypto_opening_price(eth_data, FIGURE_PATH, title):
    plt.clf()
    plt.plot(eth_data['Date'], eth_data['Open'])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.savefig(FIGURE_PATH)

def plot_crypto_closing_price(eth_data, FIGURE_PATH, title):
    plt.clf()
    plt.plot(eth_data['Date'], eth_data['Close'])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.savefig(FIGURE_PATH)

def plot_crypto_high_vs_low(eth_data, FIGURE_PATH, title):
    plt.clf()
    temp_data = eth_data[eth_data['Date'] > '2021-01-01']
    plt.plot(temp_data['Date'], temp_data['High'], label = "High")
    plt.plot(temp_data['Date'], temp_data['Low'], label = "Low")
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.savefig(FIGURE_PATH)

def plot_crypto_volume(eth_data, FIGURE_PATH, title):
    plt.clf()
    plt.plot(eth_data['Date'], eth_data['Volume'])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.savefig(FIGURE_PATH)

#########################################################
# Visualize Model Results

def plot_model_results(X_test, y_test, title, save_fig):
    FIGURE_PATH = 'figures/'
    FIGURE_PATH += save_fig
    plot_data = process_model_results(X_test, y_test)
    years = mdates.YearLocator()
    fig, ax = plt.subplots(2)
    fig.suptitle(title)
    fig.tight_layout(pad=2.0)
    plt.gca().xaxis.set_major_locator(years)
    ax[0].set_xlabel('Date')
    ax[0].set_ylabel('Actual Results')
    ax[0].bar(plot_data['Date'], plot_data['Actual'])
    ax[1].set_xlabel('Date')
    ax[1].set_ylabel('Predicted Results')
    ax[1].bar(plot_data['Date'],plot_data['predictions'])
    plt.savefig(FIGURE_PATH)

def process_model_results(X_test, y_test):
    plot_data = X_test[['Date', 'predictions']]
    plot_data = pd.concat([plot_data, y_test], axis = 1)
    plot_data['Actual'] = plot_data['Price_change']
    plot_data = plot_data.drop('Price_change', axis = 1)
    plot_data = plot_data.sort_values('Date')
    plot_data['Actual'] = np.where(plot_data['Actual'] == -1, 0, plot_data['Actual'])
    plot_data['predictions'] = np.where(plot_data['predictions'] == -1, 0, plot_data['predictions'])
    return plot_data

#########################################################
# Helper Functions

def print_nan_values(data, message):
    print(message, data.isna().sum())
    is_nan = data.isnull()
    rows_have_nan = is_nan.any(axis=1)
    nan_rows = data[rows_have_nan]
    print(nan_rows)