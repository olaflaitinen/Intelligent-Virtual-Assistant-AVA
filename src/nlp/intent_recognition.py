from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_intent_recognition_model(corpus, labels):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    model = LogisticRegression()
    model.fit(X, labels)
    return model, vectorizer

if __name__ == "__main__":
    corpus = ["Sample text for intent recognition."]
    labels = [0]
    model, vectorizer = train_intent_recognition_model(corpus, labels)
    print("Intent recognition model trained.")
