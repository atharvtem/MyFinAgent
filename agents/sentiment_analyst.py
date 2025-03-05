import google.generativeai as genai
genai.configure(api_key="AIzaSyDXm5G-lYME1ccDIgoAR-7KTJpihspqVxA")

def analyze_sentiment(inputs):
    ticker = inputs["ticker"]
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(f"Analyze the sentiment of the latest news for {ticker}")
    return {"sentiment_analysis": response.text}