import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def generate_sample_prices(filename='prices.csv', days=365):
    dates = [datetime.now() - timedelta(days=x) for x in range(days)][::-1]
    prices = np.cumprod(1 + np.random.normal(0.0005, 0.02, size=days)) * 100
    df = pd.DataFrame({'date': dates, 'close': prices})
    df.to_csv(filename, index=False)
    print('Wrote', filename)
    return filename

def sma_strategy(filename='prices.csv', short=10, long=50, initial_cash=10000):
    df = pd.read_csv(filename, parse_dates=['date'])
    df['sma_short'] = df['close'].rolling(window=short).mean()
    df['sma_long'] = df['close'].rolling(window=long).mean()
    position = 0
    cash = initial_cash
    holdings = 0.0
    trades = []
    for i,row in df.iterrows():
        if i < long: continue
        price = row['close']
        if row['sma_short'] > row['sma_long'] and position == 0:
            # buy all-in
            holdings = cash / price
            cash = 0.0
            position = 1
            trades.append((str(row['date']), 'BUY', float(price), float(holdings)))
        elif row['sma_short'] < row['sma_long'] and position == 1:
            # sell all
            cash = holdings * price
            holdings = 0.0
            position = 0
            trades.append((str(row['date']), 'SELL', float(price), float(cash)))
    final_value = cash + holdings * df.iloc[-1]['close']
    return {'final_value': float(final_value), 'trades': trades, 'return_pct': float((final_value/initial_cash-1)*100)}

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    fname = generate_sample_prices('prices.csv', days=365)
    results = sma_strategy(fname)
    import json
    with open('results.json','w') as f:
        json.dump(results, f, indent=2)
    print('Backtest complete. Results saved to results.json')
