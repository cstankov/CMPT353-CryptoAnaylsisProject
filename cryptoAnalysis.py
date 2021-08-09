from dataHandler import preprocess_data
from models import runModels
from tests import run_tests

def main():
    print("Preprocesssing data...")
    eth_data, bth_data = preprocess_data()
    print("Building Models...")
    # runModels(eth_data, bth_data, with_hypertuning=True)
    runModels(eth_data, bth_data, with_hypertuning=False)
    run_tests(eth_data, bth_data)

if __name__ == '__main__':
    main()