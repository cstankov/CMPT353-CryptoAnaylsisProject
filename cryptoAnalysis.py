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



def main():
    print("Preprocesssing data...")
    preprocess_data()

if __name__ == '__main__':
    main()