# Task 4: Optimize Portfolio

# Maximum Sharpe Ratio Portfolio
ef_max_sharpe = EfficientFrontier(expected_returns_vec, cov_matrix)
weights_max_sharpe = ef_max_sharpe.max_sharpe()
max_sharpe_perf = ef_max_sharpe.portfolio_performance(verbose=True)

# Minimum Volatility Portfolio
ef_min_vol = EfficientFrontier(expected_returns_vec, cov_matrix)
weights_min_vol = ef_min_vol.min_volatility()
min_vol_perf = ef_min_vol.portfolio_performance(verbose=True)

# Plot Efficient Frontier with a fresh EfficientFrontier instance
ef_plot = EfficientFrontier(expected_returns_vec, cov_matrix)  # Fresh instance for plotting
fig, ax = plt.subplots(figsize=(10, 5))
plotting.plot_efficient_frontier(ef_plot, ax=ax, show_assets=True)
ax.scatter(max_sharpe_perf[1], max_sharpe_perf[0], marker='*', color='r', s=200, label='Max Sharpe')
ax.scatter(min_vol_perf[1], min_vol_perf[0], marker='*', color='g', s=200, label='Min Volatility')
plt.title('Efficient Frontier')
plt.xlabel('Volatility (Risk)')
plt.ylabel('Expected Return')
plt.legend()
plt.savefig('efficient_frontier.png')
plt.show()

# Recommended Portfolio
print("\nRecommended Portfolio: Max Sharpe Ratio")
print("Weights:", weights_max_sharpe)
print(f"Expected Return: {max_sharpe_perf[0]:.2%}, Volatility: {max_sharpe_perf[1]:.2%}, Sharpe: {max_sharpe_perf[2]:.2f}")