import unittest
from src.nlp.tokenization import tokenize
from src.nlp.embedding import word2vec_embedding, bert_embedding
from src.nlp.intent_recognition import train_intent_recognition_model
from src.nlp.entity_extraction import extract_entities
from src.nlp.sentiment_analysis import analyze_sentiment

class TestNLP(unittest.TestCase):
    def test_tokenize(self):
        text = "This is a sample text for tokenization."
        tokens = tokenize(text)
        self.assertIsNotNone(tokens)

    def test_word2vec_embedding(self):
        corpus = ["Sample text for embedding."]
        model = word2vec_embedding(corpus)
        self.assertIsNotNone(model)

    def test_bert_embedding(self):
        text = "This is a sample text for embedding."
        embedding = bert_embedding(text)
        self.assertIsNotNone(embedding)

    def test_train_intent_recognition_model(self):
        corpus = ["Sample text for intent recognition."]
        labels = [0]
        model, vectorizer = train_intent_recognition_model(corpus, labels)
        self.assertIsNotNone(model)

    def test_extract_entities(self):
        text = "This is a sample text for entity extraction."
        entities = extract_entities(text)
        self.assertIsNotNone(entities)

    def test_analyze_sentiment(self):
        text = "This is a sample text for sentiment analysis."
        sentiment = analyze_sentiment(text)
        self.assertIsNotNone(sentiment)

if __name__ == '__main__':
    unittest.main()
