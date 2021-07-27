import twint
import pandas as pd

#61 influential people who tweet about bitcoin nd crypto
users = ["elonmusk", "VitalikButerin", "VladZamfir", "ErikVoorhees", "ethereumJoseph", "gavofyork",
"naval", "tayvano_", "NickSzabo4", "simondlr", "cburniske", "AmberBaldet", "koeppelmann", "jwolpert", 
"iam_preethi", "lrettig", "lrettig", "ricburton", "ricburton", "el33th4xor", "bcrypt", "evan_van_ness",
"mikeraymcdonald", "FEhrsam", "laurashin", "AriDavidPaul", "avsa", "0xstark", "JohnLilic", 
"Disruptepreneur", "wheatpond", "leashless", "APompliano", "twobitidiot",  "trentmc0", "Melt_Dem",
"technocrypto", "brian_armstrong", "nlw", "samcassatt", "spencernoon", "mskvsk", "tyler", "cameron", "scottmelker", 
"DocumentingBTC", "CarpeNoctom", "SatoshiLite", "officialmcafee", "aantonop", "rogerkver", "justinsuntron"]

#scrape tweets
for user in users:
    c = twint.Config()
    c.Username = user
    c.Search = "btc OR bitcoin OR eth OR ethereum OR crypto OR cryptocurrency OR blockchain"
    c.Since = "2016-01-01"
    c.Until = "2021-07-14"
    c.Store_csv = True
    c.Output = "tweets" + user + ".csv"
    twint.run.Search(c)

#merge all tweets files into one csv file
tweets = pd.read_csv("tweetselonmusk.csv", header = 0)

for user in users:
    filename = "tweets" + user + ".csv"
    df = pd.read_csv(filename)
    tweets = tweets.append(df)

tweets.to_csv("raw_data/tweets.csv", sep = "\t")