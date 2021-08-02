import pandas as pd
tweets = pd.read_csv("raw_data/tweets.csv", sep = "\t")
print(tweets['tweet'])
