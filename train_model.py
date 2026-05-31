import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
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
#convert labels to numbers
df["label"] = df["label"].astype(str).str.lower().map({
    "ham": 0,
    "spam": 1
})

df = df.dropna(subset=["label"])

#feature and target 
X = df["text"]
y = df["label"]

#convert text into vectors
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(X)

#split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

#train model 
model = MultinomialNB()

model.fit(X_train, y_train)

#PREDICT 
predictions = model.predict(X_test)

#accuracy 
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, predictions))

#save model 
joblib.dump(model, "spam_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\n model saved!")