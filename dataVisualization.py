from dataHandler import *
from cryptoAnalysis import *

def visualize_raw_data(eth_data, btc_data, tweet_data):
    FIGURE_PATH = 'figures/'
    visualize_eth_raw_data(eth_data, FIGURE_PATH)
    visualize_btc_raw_data(btc_data, FIGURE_PATH)
    # visualizeElonRawData(elon_data, FIGURE_PATH)

#########################################################
# ETH Visualization

def visualize_eth_raw_data(eth_data, FIGURE_PATH):
    print("Ethereum dataset headers: ", eth_data.columns.tolist())
    print_eth_nan_values(eth_data)
    plot_crypto_opening_price(eth_data, FIGURE_PATH + 'ETH-open.png', 'Opening Price of Ethereum')
    plot_crypto_closing_price(eth_data, FIGURE_PATH + 'ETH-close.png', 'Closing Price of Ethereum')
    plot_crypto_high_vs_low(eth_data, FIGURE_PATH + 'ETH-highVsLow.png', 'High Vs Low 2021 Price of Ethereum')
    plot_crypto_volume(eth_data, FIGURE_PATH + 'ETH-volume.png', 'Volume of Ethereum')

def print_eth_nan_values(eth_data):
    print("Total NAN values for ETH dataset:\n", eth_data.isna().sum())
    is_nan = eth_data.isnull()
    rows_has_nan = is_nan.any(axis=1)
    nan_rows = eth_data[rows_has_nan]
    print(nan_rows)

#########################################################
# BTC Visualization

def visualize_btc_raw_data(btc_data, FIGURE_PATH):
    print("Bitcoin dataset headers: ", btc_data.columns.tolist())
    print_btc_nan_values(btc_data)
    plot_crypto_opening_price(btc_data, FIGURE_PATH + 'BTC-open.png', 'Opening Price of Bitcoin')
    plot_crypto_closing_price(btc_data, FIGURE_PATH + 'BTC-close.png', 'Closing Price of Bitcoin')
    plot_crypto_high_vs_low(btc_data, FIGURE_PATH + 'BTC-highVsLow.png', 'High Vs Low 2021 Price of Bitcoin')
    plot_crypto_volume(btc_data, FIGURE_PATH + 'BTC-volume.png', 'Volume of Bitcoin')

def print_btc_nan_values(btc_data):
    print("Total NAN values for BTC dataset:\n", btc_data.isna().sum())
    is_nan = btc_data.isnull()
    rows_have_nan = is_nan.any(axis=1)
    nan_rows = btc_data[rows_have_nan]
    print(nan_rows)

#########################################################
# ELON Visualization



#########################################################
# Crypto Visualization

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