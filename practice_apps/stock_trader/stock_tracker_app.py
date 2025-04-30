import yfinance as yf
import pandas as pd

"""
Okay, let's craft a minimum viable product (MVP) codebase as a proof of concept. This will focus on:

Fetching real-time stock prices for a small selection of tickers from the NASDAQ, Dow Jones, and S&amp;P 500 using the yfinance library (as it's relatively straightforward for basic price data).
Calculating a very basic "undervaluation" metric: Price-to-Book (P/B) ratio. We'll need to fetch book value data for this, which might be less consistently available for free via yfinance. We'll aim to include it if feasible, but the core will be price monitoring.
Providing a simple output of the current prices and the calculated P/B ratio (if available).
We will not implement growth potential analysis or a user interface in this MVP to keep it focused.
Important Considerations for this Proof of Concept:

yfinance Limitations: While convenient, yfinance's data quality and consistency for fundamental data (like book value) can vary. For a more robust application, using a dedicated financial data API as discussed earlier is recommended.
Basic Undervaluation: The P/B ratio alone is a very simplistic measure and shouldn't be the sole basis for investment decisions.   
No Growth Analysis: This MVP will not include any analysis of future growth potential as that requires more complex data and logic.
No Scheduling: This will be a one-time execution script, not a continuously running monitor.
Error Handling: Basic error handling will be included, but comprehensive error management for API issues is beyond the scope of this MVP.

Expected Output:

The output will first show the current closing prices for the selected tickers.
Then, it will attempt to calculate and display the Price-to-Book ratio for each ticker.
Note that the availability and accuracy of the book value data will depend on what yfinance can retrieve.
Some tickers might show "Book Value or Market Price not available" or an error message if the data isn't readily accessible.

Next Steps (Beyond this MVP):

To build a more comprehensive application as initially described, you would need to:

Integrate with more robust financial data APIs: Explore Alpha Vantage, Financial Modeling Prep, or others for reliable fundamental data and potentially analyst ratings.
Implement more sophisticated undervaluation metrics: Consider comparing P/B to historical averages, industry peers, and incorporating other valuation ratios.
Develop growth potential analysis: This would involve fetching and analyzing analyst ratings, earnings forecasts, revenue growth, and potentially incorporating qualitative factors.
Build a user interface: Create a GUI or web-based interface to visualize the data and highlighted stocks.
Implement scheduling: Use a scheduling library to run the data fetching and analysis periodically.
Add error handling and logging: Implement robust error management and logging to make the application more reliable.
Consider data persistence: Store historical data and analysis results in a database or files.
This MVP provides a basic foundation for fetching stock prices and attempting a simple valuation metric. Building upon this with more comprehensive data sources and analysis techniques will be key to achieving your initial vision.

"""

def get_stock_data(tickers):
    """Fetches current stock price and basic info for a list of tickers."""
    data = yf.download(tickers, period="1d")
    return data['Close']

def get_fundamental_data(ticker):
    """Attempts to fetch fundamental data (specifically book value) for a ticker."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        if 'bookValue' in info and 'marketCap' in info:
            book_value_per_share = info['bookValue']
            market_price = get_stock_data([ticker]).iloc[0]
            if book_value_per_share is not None and market_price is not None and book_value_per_share > 0:
                pb_ratio = market_price / book_value_per_share
                return pb_ratio
            else:
                return "Book Value or Market Price not available"
        else:
            return "Book Value or Market Cap not found in data"
    except Exception as e:
        return f"Error fetching fundamental data: {e}"

if __name__ == "__main__":
    # Select a small sample of tickers from each index
    nasdaq_tickers = ["AAPL", "MSFT", "GOOGL"]
    dow_jones_tickers = ["AXP", "JPM", "WMT"]
    sp500_tickers = ["SPY", "AMZN", "TSLA"] # Including SPY to represent the index itself

    all_tickers = list(set(nasdaq_tickers + dow_jones_tickers + sp500_tickers))

    print("--- Current Stock Prices ---")
    prices = get_stock_data(all_tickers)
    print(prices)
    print("\n")

    print("--- Price-to-Book (P/B) Ratio (Basic Attempt) ---")
    pb_ratios = {}
    for ticker in all_tickers:
        pb = get_fundamental_data(ticker)
        pb_ratios[ticker] = pb
        print(f"{ticker}: {pb}")