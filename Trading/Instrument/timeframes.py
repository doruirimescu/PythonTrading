__all__=['TIMEFRAMES', 'TIMEFRAME_TO_MINUTES']
TIMEFRAMES = ['1m', '5m', '15m', '30m', '1h', '5h', '1D', '1W', '1M']
TIMEFRAME_TO_MINUTES=dict(zip(TIMEFRAMES, [1, 5, 15, 30, 60, 300, 1440, 10080, 43200]))

TIMEFRAME_TO_YFINANCE={'1m': '1m', '5m': '5m', '15m': '15m', '30m': '30m', '1h': '1h', '1D': '1d', '1W': '1w', '1M':'1mo'}
