#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:40:02 2020

@author: hteza
"""
# object oriented programming style (oo style, more efficient)
# it makes it easier to replicate
# call your function from every place
# the same code for every place

from sklearn.model_selection  import train_test_split
from sklearn.linear_model import LogisticRegression

# name the class
class ai:
    
    # __init__ is necessary
    # inititate the class
    # what attributes does this have
    # and get this
    # like pd.Dataframe()
    def __init__(self,data,features,target,test_size):
        self.X=data.loc[:,features].values
        self.y=data[target].values.ravel()
        self.model=self.learn(self.X,self.y,test_size)
    
    # other methods class ai can do
    # like pd.read_csv or pd.tosql and stuff
    def learn(self,X,y,test_size):
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=test_size,stratify=y)
        clf=LogisticRegression(max_iter=10000,penalty="l2")
        clf.fit(X_train,y_train)
        return clf
    
    

    