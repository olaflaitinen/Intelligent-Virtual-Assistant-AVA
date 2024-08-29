import re
from nltk.tokenize import word_tokenize

def tokenize(text):
    # Tokenization algorithm
    tokens = word_tokenize(text)
    return tokens

if __name__ == "__main__":
    text = "This is a sample text for tokenization."
    tokens = tokenize(text)
    print(tokens)
