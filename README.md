# CMPT353-CryptoAnaylsisProject

An exploratory data analysis on the effects that influential people on twitter such as Elon Musk have on the cryptocurrency market. With Sklearn neural network, random forest and naïve bayes classifiers we hope to see if we are able to predict the price change based on the sentiment analysis of the tweets.

## Usage

Command to run the project: python cryptoAnalysis.py (main program)
Command to run the twitter scraper: python scrapetweets.py


The follow are the libraries that we used: 
vaderSentiment\
sklearn\
matplotlib\
pandas\
numpy\
twint (Do not need to run the main program above)\


Raw datasets are contained in the raw_data folder 
Processed datasets are contained in the processed_data folder
Model hypertuning data is kept in the model_data folder
All plots and visualizations are kept in the figures folder


Once the program is run it will look to see if the processed_data folders contained the processed data. If it does not it will begin processing the data within the raw_data folder. This was done because the sentiment anaylsis does take a long time due to the 160,000 lines of data. Within the processing the raw data is also visualized and certain figures are then saved. After the processed data is loaded the statistical tests on the data are then conducted and output in the terminal. Lastly the models are then run a certain amount of times depending on what value the OVERFITTING_ITERATIONS constant (found in models.py) is set to. When each model is run the evaluation metrics are output after all OVERFITTING_ITERATIONS occur the accuracy is then plotted and stored in the firgures folder.

uncomment the line located in the crptoanalysis.py folder to conduct hypertuning for the models. It is left commented due to the amount of time it takes. 
