# Research methodology

## Technical metrics

- Returns: `latest_close / close_n_periods_ago - 1`
- Moving average: arithmetic rolling mean with a full observation window
- Annualized volatility: sample standard deviation of daily returns multiplied by square root of 252
- Drawdown: `close / running_peak - 1`
- Maximum drawdown: minimum value of the drawdown series
- Volume ratio: latest volume divided by the mean of the preceding configured window

## Score

Initial configurable weights: trend 25%, relative performance 20%, volatility 15%, maximum drawdown 15%, volume consistency 15%, 52-week structure 10%.

Normalize each component to a documented 0–100 scale before combining. Missing components are excluded from the denominator and reduce displayed data coverage. Do not implement scoring until normalization and directionality are documented and tested.

## Limitations

These are market-behaviour indicators. They do not establish revenue growth, profitability, balance-sheet strength, management quality or valuation.
