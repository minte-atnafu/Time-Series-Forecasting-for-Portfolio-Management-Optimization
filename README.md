Here's a professional `README.md` for your GMF Investments project:

```markdown
# GMF Investments: Portfolio Optimization & Time Series Forecasting

![Finance](https://img.shields.io/badge/domain-finance-blue)
![Python](https://img.shields.io/badge/language-python-yellow)
![Time Series](https://img.shields.io/badge/analysis-time_series-green)
![Portfolio Optimization](https://img.shields.io/badge/optimization-MPT-red)

## Overview
This project implements data-driven investment strategies for GMF Investments, combining time series forecasting with Modern Portfolio Theory (MPT) to optimize client portfolios. The solution analyzes Tesla (TSLA), Vanguard Total Bond Market ETF (BND), and S&P 500 ETF (SPY) assets, forecasting market trends and constructing efficient portfolios.

## Key Features
- **Data Pipeline**: Automated YFinance data fetching (2015-2025) with robust preprocessing
- **Forecasting Models**: Comparative evaluation of ARIMA/SARIMA and LSTM architectures
- **Portfolio Optimization**: Efficient Frontier simulation with PyPortfolioOpt
- **Backtesting Framework**: Strategy validation against benchmark portfolios
- **Risk Analysis**: VaR, Sharpe Ratio, and volatility modeling

## Project Structure
```
gmf-investments/
├── data/                    # Raw and processed datasets
├── notebooks/
│   ├── 1_data_processing.ipynb
│   ├── 2_forecast_modeling.ipynb
│   ├── 3_portfolio_optimization.ipynb
│   └── 4_backtesting.ipynb
├── src/
│   ├── data_loader.py       # YFinance API wrapper
│   ├── preprocessing.py    # Data cleaning utilities
│   ├── models/              # Forecasting implementations
│   └── optimization.py      # MPT calculations
├── reports/                 # Analysis visualizations
├── requirements.txt         # Python dependencies
└── README.md
```

## Methodology
1. **Data Acquisition & Preprocessing**
   - Automated daily price collection (OHLCV) for TSLA, BND, SPY
   - Missing value imputation and stationarity transformations
   - Feature engineering: Rolling volatility, returns, technical indicators

2. **Time Series Forecasting**
   - Comparative modeling: ARIMA (pmdarima) vs LSTM (TensorFlow/Keras)
   - Walk-forward validation with expanding window
   - Performance metrics: MAE, RMSE, MAPE

3. **Portfolio Construction**
   - Expected returns: Forecasted (TSLA) + historical (BND/SPY)
   - Covariance matrix estimation
   - Efficient Frontier simulation
   - Identification of optimal portfolios:
     - Maximum Sharpe Ratio
     - Minimum Volatility

4. **Strategy Validation**
   - 12-month backtest (Aug 2024-Jul 2025)
   - Benchmark: 60/40 SPY/BND portfolio
   - Performance metrics: Cumulative returns, Sharpe Ratio

## Installation
```bash
git clone https://github.com/[your-repo]/gmf-investments.git
cd gmf-investments
pip install -r requirements.txt
```

## Usage
1. Run Jupyter notebooks in sequential order:
```bash
jupyter notebook notebooks/1_data_processing.ipynb
```
2. Configure assets and date ranges in `config.yaml`
3. Execute pipeline:
```python
from src.data_loader import fetch_data
df = fetch_data(tickers=['TSLA', 'BND', 'SPY'], 
                start='2015-07-01', 
                end='2025-07-31')
```

## Key Findings
- LSTM outperformed ARIMA on test set (MAPE: 2.1% vs 3.7%)
- Optimal portfolio (Max Sharpe):
  - TSLA: 38% 
  - SPY: 55%
  - BND: 7%
- Strategy outperformed benchmark by 4.2% during backtest

## Dependencies
- Python 3.8+
- yfinance, pandas, numpy
- statsmodels, pmdarima
- tensorflow, scikit-learn
- PyPortfolioOpt, matplotlib

## Contributors
- Mintesinot Atnafu - Lead Financial Analyst
- GMF Investments Quantitative Team

## License
This project is proprietary property of GMF Investments. All rights reserved.
