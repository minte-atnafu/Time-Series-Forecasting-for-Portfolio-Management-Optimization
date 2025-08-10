# Task 2: Develop Time Series Forecasting Models (TSLA) - ARIMA only for interim
if 'TSLA' in available_tickers:
    tsla_close = data['TSLA'][('Close', 'TSLA') if isinstance(data['TSLA'].columns, pd.MultiIndex) else 'Close']
    train_size = int(len(tsla_close) * 0.8)
    train, test = tsla_close[:train_size], tsla_close[train_size:]

    # ARIMA
    model_arima = ARIMA(train, order=(1, 1, 1))
    arima_fit = model_arima.fit()
    arima_forecast = arima_fit.forecast(steps=len(test))
    mae_arima = mean_absolute_error(test, arima_forecast)
    rmse_arima = sqrt(mean_squared_error(test, arima_forecast))
    mape_arima = np.mean(np.abs((test - arima_forecast) / test)) * 100
    print(f"ARIMA MAE: {mae_arima:.2f}, RMSE: {rmse_arima:.2f}, MAPE: {mape_arima:.2f}%")

    plt.figure(figsize=(10, 5))
    plt.plot(test.index, test, label='Actual')
    plt.plot(test.index, arima_forecast, label='ARIMA Forecast')
    plt.title('TSLA Forecast vs Actual')
    plt.legend()
    plt.savefig('tsla_forecast.png')
    plt.show()