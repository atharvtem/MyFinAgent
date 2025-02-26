import streamlit as st
from fetch_stock import fetch_stock_data, fetch_stock_news
from analysis.technical_analysis import add_technical_indicators, generate_technical_summary
from analysis.sentiment_analysis import analyze_sentiment
from visualizations.visualize_stock import plot_stock_plotly

# Streamlit App Title
st.title("AI Stock Analyst")

# Inputs
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL):", "AAPL")
period = st.selectbox("Select Period:", ["1mo", "3mo", "6mo", "1y"])

# Analyze Button
if st.button("Analyze"):
    # Fetch stock data
    st.write(f"Fetching data for {ticker}...")
    data = fetch_stock_data(ticker, period=period)
    
    # Add technical indicators
    data = add_technical_indicators(data)

    # Display stock price and technical analysis
    st.subheader(f"{ticker} Stock Price Trend & Technical Analysis")
    st.plotly_chart(plot_stock_plotly(data, ticker))

    # Display technical summary
    st.subheader("Technical Analysis Summary")
    summary = generate_technical_summary(data)

    # RSI Interpretation
    rsi_value = summary['RSI']
    if rsi_value > 70:
        rsi_interpretation = "Overbought (Potential Sell)"
    elif rsi_value < 30:
        rsi_interpretation = "Oversold (Potential Buy)"
    else:
        rsi_interpretation = "Neutral"
    st.write(f"**RSI (14):** {rsi_value:.2f} ({rsi_interpretation})")

    # MACD Interpretation
    macd_value = summary['MACD']
    signal_value = summary['Signal']
    if macd_value > signal_value:
        macd_interpretation = "Potential Buy (MACD > Signal)"
    else:
        macd_interpretation = "Potential Sell (MACD < Signal)"
    st.write(f"**MACD:** {macd_value:.2f}")
    st.write(f"**Signal Line:** {signal_value:.2f}")
    st.write(f"**MACD Interpretation:** {macd_interpretation}")

    # Fetch and analyze news sentiment
    # Fetch and analyze news sentiment
# Fetch and analyze news sentiment

    st.subheader("Sentiment Analysis")

ticker = st.text_input("Enter Stock Ticker:", "AAPL")

# Fetch news for the given stock ticker
news = fetch_stock_news(ticker)

if news:
    st.write(f"Top 5 news headlines for {ticker}:")
    sentiment_scores = []
    sentiment_labels = []

    for item in news[:5]:  # Show top 5 news items
        title = item.get("title", "No title available")
        source = item.get("source", {}).get("name", "No source available")

        st.write(f"**{title}**")
        st.write(f"Source: {source}")

        # Analyze sentiment
        dominant_sentiment, dominant_value = analyze_sentiment(title)
        sentiment_scores.append(dominant_value)
        sentiment_labels.append(dominant_sentiment)

        st.write(f"Sentiment: {dominant_sentiment} ({dominant_value:.2f})")
        st.write("---")

    # **Fixed Sentiment Summary Calculation**
    positive_count = sentiment_labels.count("Positive")
    negative_count = sentiment_labels.count("Negative")
    neutral_count = sentiment_labels.count("Neutral")

    # Determine overall sentiment based on majority voting
    if positive_count > negative_count and positive_count > neutral_count:
        overall_sentiment = "Positive"
    elif negative_count > positive_count and negative_count > neutral_count:
        overall_sentiment = "Negative"
    else:
        overall_sentiment = "Neutral"

    avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0

    st.subheader("Sentiment Summary")
    st.write(f"Average Sentiment Score: {avg_sentiment:.2f}")
    st.write(f"Overall Sentiment: {overall_sentiment}")

else:
    st.write("No news available for this stock.")



# st.subheader("Sentiment Analysis")
# news = fetch_stock_news(ticker)
# if news:
#     st.write(f"Top 5 news headlines for {ticker}:")
#     sentiment_scores = []
#     for item in news[:5]:  # Show top 5 news items
#         title = item.get("title", "No title available")
#         source = item.get("source", {}).get("name", "No source available")
#         st.write(f"**{title}**")
#         st.write(f"Source: {source}")
        
#         # Analyze sentiment
#         sentiment_dict = analyze_sentiment(title)
#         dominant_sentiment = max(sentiment_dict, key=sentiment_dict.get)  # Get the highest sentiment
#         dominant_value = sentiment_dict[dominant_sentiment]

#         st.write(f"Sentiment: {dominant_sentiment} ({dominant_value:.2f})")

#         sentiment_scores.append(dominant_value)
#         st.write("---")
    
#     # Sentiment Summary
#     avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0
#     st.subheader("Sentiment Summary")
#     st.write(f"Average Sentiment: {avg_sentiment:.2f}")
#     if avg_sentiment > 0:
#         st.write("Overall Sentiment: Positive")
#     elif avg_sentiment < 0:
#         st.write("Overall Sentiment: Negative")
#     else:
#         st.write("Overall Sentiment: Neutral")
# else:
#     st.write("No news available for this stock.")