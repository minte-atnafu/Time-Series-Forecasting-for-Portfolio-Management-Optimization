# Task 1: Preprocess and Explore the Data

# Fetch data from yfinance
tickers = ['TSLA', 'BND', 'SPY']
data = {}
for ticker in tickers:
    data[ticker] = yf.download(ticker, start='2015-07-01', end='2025-08-01')

# Combine closing prices
closes = pd.DataFrame({ticker: data[ticker]['Adj Close'] for ticker in tickers})
closes.dropna(inplace=True)

# Data Cleaning
for ticker in tickers:
    df = data[ticker]
    print(f"\n{ticker} Data Info:")
    print(df.info())
    df.fillna(method='ffill', inplace=True)
    df.dropna(inplace=True)

# Basic Statistics
for ticker in tickers:
    print(f"\n{ticker} Basic Statistics:")
    print(data[ticker].describe())

# EDA: Plot closing prices, daily returns, and volatility
for ticker in tickers:
    df = data[ticker]
    plt.figure(figsize=(10, 5))
    plt.plot(df['Adj Close'], label=f'{ticker} Adj Close')
    plt.title(f'{ticker} Adjusted Closing Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

    df['Daily Return'] = df['Adj Close'].pct_change()
    plt.figure(figsize=(10, 5))
    plt.plot(df['Daily Return'], label=f'{ticker} Daily Return')
    plt.title(f'{ticker} Daily Returns')
    plt.xlabel('Date')
    plt.ylabel('Return')
    plt.legend()
    plt.show()

    df['Rolling Volatility'] = df['Daily Return'].rolling(window=30).std()
    plt.figure(figsize=(10, 5))
    plt.plot(df['Rolling Volatility'], label=f'{ticker} 30-Day Volatility')
    plt.title(f'{ticker} Rolling Volatility')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.legend()
    plt.show()

# Stationarity Test
for ticker in tickers:
    df = data[ticker]
    adf_close = adfuller(df['Adj Close'])
    adf_return = adfuller(df['Daily Return'].dropna())
    print(f"\n{ticker} ADF Test for Adj Close: p-value = {adf_close[1]}")
    print(f"{ticker} ADF Test for Daily Returns: p-value = {adf_return[1]}")

# Volatility Analysis
for ticker in tickers:
    df = data[ticker]
    var_95 = np.percentile(df['Daily Return'].dropna(), 5)
    sharpe = (df['Daily Return'].mean() * 252) / (df['Daily Return'].std() * np.sqrt(252))
    print(f"\n{ticker} 95% VaR: {var_95:.4f}, Sharpe Ratio: {sharpe:.4f}")

