from gensim.models import Word2Vec
from transformers import BertTokenizer, BertModel
import torch

def word2vec_embedding(corpus):
    model = Word2Vec(corpus, vector_size=100, window=5, min_count=1, workers=4)
    return model

def bert_embedding(text):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    inputs = tokenizer(text, return_tensors='pt')
    outputs = model(**inputs)
    return outputs.last_hidden_state

if __name__ == "__main__":
    text = "This is a sample text for embedding."
    embedding = bert_embedding(text)
    print(embedding)
