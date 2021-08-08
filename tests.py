from matplotlib.pyplot import axis
from statsmodels.stats.contingency_tables import mcnemar
import pandas as pd
from scipy import stats

def getContingencyTable(eth_data, btc_data):
    eth_data['Symbol'] = 'ETH'
    eth_data = eth_data[['Price_change', 'Symbol']]
    btc_data['Symbol'] = 'BTC'
    btc_data = btc_data[['Price_change', 'Symbol']]
    frames = [eth_data, btc_data]
    data = pd.concat(frames).reset_index(drop = True)
    contingency = pd.crosstab(data['Symbol'], data['Price_change'])
    return contingency

def mcNemars(eth_data, btc_data):
    contingency = getContingencyTable(eth_data, btc_data)
    print(contingency)
    print("Pvalue for McNemar's Test:", mcnemar(contingency).pvalue)

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

def is_equal(x):
    if x['sentiment'] == x['Price_change']:
        return "Directly Proportional"
    else:
        return "Indirectly Proportional"

def is_equal(x):
    if x['Price_change_ETH'] == x['Price_change_BTC']:
        return "Directly Proportional"
    else:
        return "Indirectly Proportional"

def dayByDayTest(eth_data, btc_data):
    data = pd.concat([eth_data['Price_change'], btc_data['Price_change']], axis = 1)
    columns = ['Price_change_ETH', 'Price_change_BTC']
    data.columns = columns
    is_equal_ = data.apply(lambda x:is_equal(x), axis = 1)
    print(is_equal_.value_counts())

def is_equal2(x):
    if x['sentiment'] == x['Price_change']:
        return "Directly Proportional"
    else:
        return "Indirectly Proportional"

def convertData(data):
    data = data[['sentiment', 'Price_change']]
    data['Price_change'] = data['Price_change'].apply(convertPriceChange)
    data['sentiment'] = data['sentiment'].apply(convertSentiment)
    return data

def dayByDayTest2(data):
    data = convertData(data)
    is_equal_ = data.apply(lambda x:is_equal2(x), axis = 1)
    print(is_equal_.value_counts())
    
def getContingency(data):
    data = convertData(data)
    new1 = data[['sentiment']]
    new1 = new1.rename(columns={"sentiment": "value"})
    new1['type'] = 'sentiment'
    new2 = data[['Price_change']]
    new2 = new2.rename(columns={"Price_change": "value"})
    new2['type'] = 'Price_change'
    frames = [new1, new2]
    data = pd.concat(frames).reset_index(drop = True)
    contingency = pd.crosstab(data['type'], data['value'])
    return contingency

def chiSquareTest(data):
    contingency = getContingency(data) 
    chi2, p, dof, expected = stats.chi2_contingency(contingency)
    print("Pvalue for chi squared test: ", p)
    #print(expected)

def runTests(eth_data, btc_data):
    mcNemars(eth_data, btc_data)
    dayByDayTest(eth_data, btc_data)
    chiSquareTest(eth_data)
    chiSquareTest(btc_data)
    dayByDayTest2(eth_data)
    dayByDayTest2(btc_data)