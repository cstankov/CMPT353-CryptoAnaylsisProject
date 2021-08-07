import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
import csv
import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from dataHandler import *
from dataVisualization import *
from sentimentAnalysis import *
from models import *



def main():
    print("Preprocesssing data...")
    eth_data, bth_data = preprocess_data()
    runModels(eth_data, bth_data)

if __name__ == '__main__':
    main()