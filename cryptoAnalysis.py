import pandas as pd
from dataHandler import preprocess_data
from models import run_all_models
from tests import run_tests

def main():
   # print("Preprocesssing data...")
    eth_data, bth_data = preprocess_data()
    #print("Building Models...")
    # runModels(eth_data, bth_data, with_hypertuning=True)
    #run_all_models(eth_data, bth_data, with_hypertuning=False)
    run_tests(eth_data, bth_data)

if __name__ == '__main__':
    main()