# from nltk.sentiment import SentimentIntensityAnalyzer
# import nltk

# nltk.download("vader_lexicon")

# def analyze_sentiment(text):
#     """Analyze sentiment using VADER."""
#     sia = SentimentIntensityAnalyzer()
#     sentiment = sia.polarity_scores(text)
#     return sentiment

from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download("vader_lexicon")

def analyze_sentiment(text):
    """
    Analyze sentiment using VADER with improved classification.
    Returns: (Sentiment Label, Sentiment Score)
    """
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)

    # Adjusted thresholds for better classification
    if sentiment["compound"] >= 0.02:
        return "Positive", sentiment["compound"]
    elif sentiment["compound"] <= -0.02:
        return "Negative", sentiment["compound"]
    else:
        return "Neutral", sentiment["compound"]
