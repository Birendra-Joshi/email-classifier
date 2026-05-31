import pandas as pd
import joblib

from sklearn.model_selection import tfidfvectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

#load dataset 
df = pd.read_csv("emails.csv")

#remove missing valuees 
df = df.dropna()

#remove dublicates 
df = df.drop_duplicates()

#convert labels to numbeers 
df["label"] = df["label"].map({
    "ham": 0,
    "spam": 1
})

#feature and target 