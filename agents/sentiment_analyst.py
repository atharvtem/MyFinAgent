import google.generativeai as genai
from api_info import api_key, model_name

genai.configure(api_key)

def analyze_sentiment(inputs):
    ticker = inputs["ticker"]
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(f"Analyze the sentiment of the latest news for {ticker}")
    return {"sentiment_analysis": response.text}