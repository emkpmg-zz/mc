# -*- coding: utf-8 -*-
"""
Created on Wed May 15 19:22:57 2019

@author: PIANDT
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve
import matplotlib.pyplot as plt

mushroomData = pd.read_csv('mushrooms.csv')

#convert categorical features to numeric
mushroomData2 = pd.get_dummies(mushroomData)
inputFeatures = mushroomData2.iloc[:,2:]
outputFeatures = mushroomData2.iloc[:,1]

X_train2, X_test2, y_train2, y_test2 = train_test_split(inputFeatures, outputFeatures, random_state=0)


X_subset = X_test2
y_subset = y_test2

modelClassifier = DecisionTreeClassifier(random_state=0).fit(X_train2, y_train2)
# Sorted relevant features in descending order
relevantFeaturesSortD = modelClassifier.feature_importances_.argsort()[::-1][:5]   
top5Features = list(X_train2.columns[relevantFeaturesSortD])
print(top5Features)

#determine training and test scores for a Support Vector Classifier (SVC) 
#with varying parameter values


gammaRange = np.logspace(-4,1,6)
svcClassifier = SVC(kernel = 'rbf', C = 1, random_state=0)
    
svcScoresTrain, svcScoresTest = validation_curve(svcClassifier, X_subset, y_subset, param_name='gamma', param_range=gammaRange, cv=3, scoring="accuracy")

training_scores = np.mean(svcScoresTrain, axis=1)
testing_scores = np.mean(svcScoresTest, axis=1)
    
print(training_scores, testing_scores)
#return training_scores, testing_scores# Your answer here

#visualize the appropriate gamma vs accuracy
plt.plot(gammaRange, training_scores)
plt.plot(gammaRange, testing_scores)
plt.show()
#median polynomial degree at index 6 gives the best fit

