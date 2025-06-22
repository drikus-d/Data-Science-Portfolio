import yfinance as yf
import pandas as pd
import ta  # pip install ta

def load_data(ticker="AAPL", period="2y", interval="1d"):
    df = yf.download(ticker, period=period, interval=interval)
    df = df.dropna()
    return df

def add_technical_indicators(df):
    close_series = df['Close'].squeeze()
    
    df['SMA_20'] = ta.trend.SMAIndicator(close=close_series, window=20).sma_indicator()
    df['EMA_20'] = ta.trend.EMAIndicator(close=close_series, window=20).ema_indicator()
    df['RSI']    = ta.momentum.RSIIndicator(close=close_series, window=14).rsi()
    df['MACD']   = ta.trend.MACD(close=close_series).macd_diff()
    
    return df

def add_lag_features(df, lags=[1, 2, 3]):
    for lag in lags:
        df[f'lag_{lag}'] = df['Close'].shift(lag)
    return df.dropna()