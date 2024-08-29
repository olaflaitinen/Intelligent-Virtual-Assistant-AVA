from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment

if __name__ == "__main__":
    text = "This is a sample text for sentiment analysis."
    sentiment = analyze_sentiment(text)
    print(sentiment)
