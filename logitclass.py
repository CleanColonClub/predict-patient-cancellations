import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

from sklearn.model_selection import train_test_split


def loadData():
    dataset = pd.read_csv('data/data.csv')
    feature_cols = ['Date Diff']
    target = 'No Show/LateCancel Flag'
    X = dataset[feature_cols]
    y = dataset[target]
    return(X, y)

def test():
    dataset = pd.read_csv('data/data.csv')
    feature_cols = ['Date Diff']
    target = 'No Show/LateCancel Flag'
    X = dataset[feature_cols]
    y = dataset[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    logit = SGDClassifier()
    logit.fit(X_train, y_train)
    y_pred = logit.predict(X_test)
    conf_matrix = confusion_matrix(y_test, y_pred)
    print(conf_matrix)
    print(classification_report(y_test, y_pred))

test()
