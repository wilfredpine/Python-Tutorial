# utils/classifier.py

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Sample training data
documents = [
    "Research paper about AI",
    "Proposal for funding",
    "Monthly report of activities",
]
labels = ['research', 'proposal', 'report']

def train_classifier():
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(documents)
    model = MultinomialNB()
    model.fit(X, labels)
    joblib.dump(model, 'model.joblib')
    joblib.dump(vectorizer, 'vectorizer.joblib')

def classify_document(text):
    model = joblib.load('model.joblib')
    vectorizer = joblib.load('vectorizer.joblib')
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    return prediction[0]
