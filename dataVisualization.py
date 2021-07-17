from dataHandler import *
from cryptoAnalysis import *

def visualizeRawData(eth_data, btc_data, elon_data):
    FIGURE_PATH = 'figures/'
    visualizeEthRawData(eth_data, FIGURE_PATH)
    visualizeBtcRawData(btc_data, FIGURE_PATH)

#########################################################
# ETH Visualization

def visualizeEthRawData(eth_data, FIGURE_PATH):
    print("Ethereum dataset headers: ", eth_data.columns.tolist())
    plotCryptoOpeningPrice(eth_data, FIGURE_PATH + 'ETH-open.png', 'Opening Price of Ethereum')
    plotCryptoClosingPrice(eth_data, FIGURE_PATH + 'ETH-close.png', 'Closing Price of Ethereum')
    plotCryptoHighVsLow(eth_data, FIGURE_PATH + 'ETH-highVsLow.png', 'High Vs Low 2021 Price of Ethereum')
    plotCryptoVolume(eth_data, FIGURE_PATH + 'ETH-volume.png', 'Volume of Ethereum')

#########################################################
# BTC Visualization

def visualizeBtcRawData(btc_data, FIGURE_PATH):
    print("Bitcoin dataset headers: ", btc_data.columns.tolist())
    plotCryptoOpeningPrice(btc_data, FIGURE_PATH + 'BTC-open.png', 'Opening Price of Bitcoin')
    plotCryptoClosingPrice(btc_data, FIGURE_PATH + 'BTC-close.png', 'Closing Price of Bitcoin')
    plotCryptoHighVsLow(btc_data, FIGURE_PATH + 'BTC-highVsLow.png', 'High Vs Low 2021 Price of Bitcoin')
    plotCryptoVolume(btc_data, FIGURE_PATH + 'BTC-volume.png', 'Volume of Bitcoin')

#########################################################
# Crypto Visualization

def plotCryptoOpeningPrice(eth_data, FIGURE_PATH, title):
    plt.clf()
    plt.plot(eth_data['Date'], eth_data['Open'])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.savefig(FIGURE_PATH)

def plotCryptoClosingPrice(eth_data, FIGURE_PATH, title):
    plt.clf()
    plt.plot(eth_data['Date'], eth_data['Close'])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.savefig(FIGURE_PATH)

def plotCryptoHighVsLow(eth_data, FIGURE_PATH, title):
    plt.clf()
    temp_data = eth_data[eth_data['Date'] > '2021-01-01']
    plt.plot(temp_data['Date'], temp_data['High'], label = "High")
    plt.plot(temp_data['Date'], temp_data['Low'], label = "Low")
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.savefig(FIGURE_PATH)

def plotCryptoVolume(eth_data, FIGURE_PATH, title):
    plt.clf()
    plt.plot(eth_data['Date'], eth_data['Volume'])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.savefig(FIGURE_PATH)