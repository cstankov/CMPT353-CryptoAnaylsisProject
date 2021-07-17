from cryptoAnalysis import *

def preprocessData():
    BASE_PATH = os.path.dirname(__file__)
    RAW_PATH = '/raw_data/'
    PROCESSED_PATH = '/processed_data/'
    if dataAlreadyPreprocessed(BASE_PATH, PROCESSED_PATH):
        print("Data has already been preprocessed.")
        return loadPreprocessedData(BASE_PATH, PROCESSED_PATH)
    else:
        print("Preprocesssing Eth Data.")



#########################################################
# LOAD DATA

def loadPreprocessedData(BASE_PATH, PROCESSED_PATH):
    eth_data = pd.read_csv(getRelPath(BASE_PATH, PROCESSED_PATH,'ETH-USD-Processed.csv'))
    btc_data = pd.read_csv(getRelPath(BASE_PATH, PROCESSED_PATH, 'BTC-USD-Processed.csv'))
    elon_data = pd.read_csv(getRelPath(BASE_PATH, PROCESSED_PATH, 'elon-Processed.csv'))
    return eth_data, btc_data, elon_data

def loadRawData():
    BASE_PATH = os.path.dirname(__file__)
    RAW_PATH = '/raw_data/'
    na_lst = ['#N/A', '#N/A', 'N/A', '#NA', '-1.#IND', '-1.#QNAN', '-NaN', '-nan', '1.#IND', '1.#QNAN', '<NA>', 'N/A', 'NA', 'NULL', 'NaN', 'n/a', 'nan', 'null', 'Unknown', 'unknown']
    eth_data = pd.read_csv(getRelPath(BASE_PATH, RAW_PATH,'ETH-USD.csv'), na_values=na_lst, parse_dates=['Date'])
    btc_data = pd.read_csv(getRelPath(BASE_PATH, RAW_PATH, 'BTC-USD.csv'), na_values=na_lst, parse_dates=['Date'])
    elon_data = pd.read_csv(getRelPath(BASE_PATH, RAW_PATH, 'elon.csv'), na_values=na_lst, sep ='\t')
    return eth_data, btc_data, elon_data

def getRelPath(BASE_PATH, PROCESSED_PATH, SUB_PATH):
    return BASE_PATH + PROCESSED_PATH + SUB_PATH

#########################################################
# DETECTING PROCESSED DATA

def dataAlreadyPreprocessed(BASE_PATH, PROCESSED_PATH):
    return ethDatasetPreprocessed(BASE_PATH, PROCESSED_PATH) and \
        btcDatasetPreprocessed(BASE_PATH, PROCESSED_PATH) and \
        elonDatasetPreprocessed(BASE_PATH, PROCESSED_PATH)

def ethDatasetPreprocessed(BASE_PATH, PROCESSED_PATH):
    return os.path.exists(getRelPath(BASE_PATH, PROCESSED_PATH,'ETH-USD-Processed.csv'))

def btcDatasetPreprocessed(BASE_PATH, PROCESSED_PATH):
    return os.path.exists(getRelPath(BASE_PATH, PROCESSED_PATH,'BTC-USD-Processed.csv'))

def elonDatasetPreprocessed(BASE_PATH, PROCESSED_PATH):
    return os.path.exists(getRelPath(BASE_PATH, PROCESSED_PATH,'elon-Processed.csv'))
