# Task 3: Forecast Future Market Trends (Simplified)
if 'TSLA' in available_tickers:
    future_periods = 252
    future_forecast = arima_fit.forecast(steps=future_periods)
    conf_int = arima_fit.get_forecast(steps=future_periods).conf_int()
    last_date = tsla_close.index[-1]
    future_dates = pd.date_range(last_date + pd.Timedelta(days=1), periods=future_periods, freq='B')

    plt.figure(figsize=(10, 5))
    plt.plot(tsla_close.index, tsla_close, label='Historical')
    plt.plot(future_dates, future_forecast, label='Forecast')
    plt.fill_between(future_dates, conf_int.iloc[:, 0], conf_int.iloc[:, 1], color='gray', alpha=0.3, label='95% CI')
    plt.title('TSLA 12-Month Forecast')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.savefig('tsla_future_forecast.png')
    plt.show()

    print("\nForecast Insights:")
    print("- Trend: Check plot for trend direction.")
    print("- Volatility: Wider CIs indicate higher uncertainty.")