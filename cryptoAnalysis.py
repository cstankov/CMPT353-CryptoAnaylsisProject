import pandas as pd
from dataHandler import preprocess_data
from models import run_all_models
from tests import run_tests

def main():
    print("Preprocesssing data...")
    eth_data, bth_data = preprocess_data()
    print("Running Tests...")
    run_tests(eth_data, bth_data)
    print("Building Models...")
    # hypertuning for the models 
    # run_all_models(eth_data, bth_data, with_hypertuning=True)
    # Running the models regularly
    run_all_models(eth_data, bth_data, with_hypertuning=False)

if __name__ == '__main__':
    main()