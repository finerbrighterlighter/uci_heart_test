#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:53:11 2020

@author: hteza
"""

import pandas as pd
import medml as ml

col_names = ["age", "sex", "cp", "trestbps", "chol", "fbs", 
             "restecg", "thalach", "exang", "oldpeak", "slope", 
             "ca", "thal", "num"]
df = pd.read_csv("/Users/hteza/Desktop/Class/RADS602/heart/processed.cleveland.data", header= None, names=col_names)

df=df[df["thal"]!="?"].reset_index(drop=True)
df=df[df["ca"]!="?"].reset_index(drop=True)

df["labels"]=df["num"].apply(lambda x:1 if x>0 else 0)

features = ["thal", "exang", "cp", "ca", "slope"]

thal = pd.get_dummies(df["thal"])
thal.columns=["normal","fixed_defect","reversible defect"]
df=pd.concat([df,thal],axis=1)

df["cp"]=df["cp"].map({1: "typical angina",
                       2: "atypical angina",
                       3: "non-anginal pain",
                       4: "asymptomatic"})
cp= pd.get_dummies(df["cp"])
df=pd.concat([df,cp],axis=1)

df["slope"]=df["slope"].map({1: "upsloping",
                             2: "flat",
                             3: "downsloping"})
slope=pd.get_dummies(df["slope"])
df=pd.concat([df,slope],axis=1)

data=df.loc[:,["normal","fixed_defect","reversible defect","typical angina",
               "atypical angina","non-anginal pain","asymptomatic",
               "upsloping","flat","downsloping","exang","ca","labels"]]

features = data.columns.tolist()
features.remove("labels")
heart = ml.ai(data=df,features=features,target="labels",test_size=0.2)

import pickle
pickle.dump(heart.model, open("logregheart.pkl","wb"))
# dump python file into pickle file
# you determine here
# pkl file appears in the same directory as this python file
 
# just recall the pickle file back into one name ( which will be model )
# you can test with myheart.coef_
# since they are in the same directory , ypu don't need to direct to it
# just call him by his name
# although you gotta figure out how to call the other directory with . or ..
myheart=pickle.load(open("logregheart.pkl","rb"))
