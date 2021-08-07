from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV
import pandas as pd

def convertValue(value):
    if value == 'Increased':
        return 1
    elif value == 'Decreased':
        return -1
    else:
        return 0

def splitData(data):
    X = data.iloc[:, data.columns != 'Price_change']
    price_change = data['Price_change']
    y = price_change.apply(convertValue)

    X_train, X_valid, y_train, y_valid = train_test_split(X, y)
    return [X_train, X_valid, y_train, y_valid]

def randomForestClassifier(model_data):
    X_train, X_valid, y_train, y_valid = model_data[0], model_data[1], model_data[2], model_data[3]
    parameters = {
        'n_estimators':[50, 200, 350, 500], 
        'max_depth':[5, 7, 10, 12], 
        'min_samples_leaf':[1, 5, 10], 
        'min_samples_split':[2, 6, 10]}
    rfc = RandomForestClassifier()
    model = GridSearchCV(rfc, parameters)
    model.fit(X_train, y_train)
    print(model.score(X_train, y_train))
    print(model.score(X_valid, y_valid))
    print(model.cv_results_)
    pd.DataFrame(model.cv_results_).to_csv('btc_results_random_forest.csv')

def runModels(eth_data, btc_data):
    #eth_model_data = splitData(eth_data)
    #randomForestClassifier(eth_model_data)
    btc_model_data = splitData(btc_data)
    randomForestClassifier(btc_model_data)
    # btc - {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 50}
    #eth - {'max_depth': 10, 'min_samples_leaf': 10, 'min_samples_split': 2, 'n_estimators': 50}