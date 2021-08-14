from matplotlib.pyplot import axis
from statsmodels.stats.contingency_tables import mcnemar
import pandas as pd
from scipy import stats

def run_tests(eth_data, btc_data):
    mc_nemars(eth_data, btc_data)
    compare_price_change_btc_eth(eth_data, btc_data)
    chi_square_test(eth_data)
    chi_square_test(btc_data)
    compare_sentiment_with_price_change(eth_data)
    compare_sentiment_with_price_change(btc_data)

#########################################################
# Mc Nemars Test
# - Mc Nemars test ran on BTC and ETH if it incresed and decreased
#   the same amount. Low PValue shows that it BTC and ETH increase and decrease 
#   at a similar rate.

def mc_nemars(eth_data, btc_data):
    contingency = get_contingency_table_for_mcnemar(eth_data, btc_data)
    print("-------------------------------------------------")
    print(contingency)
    print("Pvalue for McNemar's Test:", mcnemar(contingency).pvalue)
    print("-------------------------------------------------\n\n")

def get_contingency_table_for_mcnemar(eth_data, btc_data):
    eth_data['Symbol'] = 'ETH'
    eth_data = eth_data[['Price_change', 'Symbol']]
    btc_data['Symbol'] = 'BTC'
    btc_data = btc_data[['Price_change', 'Symbol']]
    data = pd.concat([eth_data, btc_data]).reset_index(drop = True)
    # print("Covariance for price change for crypto: ", data.cov())
    return pd.crosstab(data['Symbol'], data['Price_change'])

#########################################################
# BTC and ETH day by day comparing the Price_change Test
# - Percentage of days where both BTC and ETH had a net increase or decrease

def compare_price_change_btc_eth(eth_data, btc_data):
    data = pd.concat([eth_data['Price_change'], btc_data['Price_change']], axis = 1)
    columns = ['Price_change_ETH', 'Price_change_BTC']
    data.columns = columns
    equal_count = data.apply(lambda x:is_equal(x), axis = 1)
    calculate_btc_eth_cov(data)
    print("-------------------------------------------------")
    print("Comparison of the price change between BTC and ETH test (%): ", equal_count.value_counts()/ len(equal_count))
    print("-------------------------------------------------\n\n")

def calculate_btc_eth_cov(data):
    temp = data.copy()
    temp['Price_change_ETH'] = data['Price_change_ETH'].apply(convertPriceChange)
    temp['Price_change_BTC'] = data['Price_change_BTC'].apply(convertPriceChange)
    print("-------------------------------------------------")
    print("Covariance for crypto price change: ", temp.cov())
    print("-------------------------------------------------\n\n")

def is_equal(x):
    if x['Price_change_ETH'] == x['Price_change_BTC']:
        return "Directly Proportional"
    else:
        return "Indirectly Proportional"

#########################################################
# Chi Square Test
# - Comparing sentiment score with price change. If PValue is 
#   small there is a correlation between the number of sentiment scores
#   to price change  

def chi_square_test(data):
    contingency = get_contingency(data) 
    chi2, p, dof, expected = stats.chi2_contingency(contingency)
    print("-------------------------------------------------")
    print("Pvalue for chi squared test: ", p)
    print("-------------------------------------------------\n\n")

def get_contingency(data):
    data = convert_data(data)
    new1 = data[['sentiment']]
    new1 = new1.rename(columns={"sentiment": "value"})
    new1['type'] = 'sentiment'
    new2 = data[['Price_change']]
    new2 = new2.rename(columns={"Price_change": "value"})
    new2['type'] = 'Price_change'
    data = pd.concat([new1, new2]).reset_index(drop = True)
    print("-------------------------------------------------")
    print("Covariance for sentiment and price change: ", data.cov())
    print("-------------------------------------------------\n\n")
    return pd.crosstab(data['type'], data['value'])

#########################################################
#  Comparing sentiment score with price increase per day Test

def compare_sentiment_with_price_change(data):
    data = convert_data(data)
    temp = data.copy()
    temp['is_equal'] = data.apply(lambda x: is_equal2(x), axis = 1)
    print("-------------------------------------------------")
    print("Comparison of the price change between sentiment score and Price_change test (%): ", temp['is_equal'].value_counts()/ len(temp))
    print("-------------------------------------------------\n\n")

#########################################################
#  Helper Functions

def convert_data(data):
    data = data[['sentiment', 'Price_change']]
    temp = data.copy()
    temp['Price_change'] = data['Price_change'].apply(convertPriceChange)
    temp['sentiment'] = data['sentiment'].apply(convertSentiment)
    return temp

def convertPriceChange(value):
    if value == 'Increased':
        return 1
    elif value == 'Decreased':
        return -1
    else:
        return 0

def convertSentiment(value):
    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0

def is_equal2(x):
    if x['sentiment'] == x['Price_change']:
        return "Directly Proportional"
    else:
        return "Indirectly Proportional"