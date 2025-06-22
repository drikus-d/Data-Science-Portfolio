
# 📈 Equity Price Forecasting - Apple Inc (AAPL)

## Objective
Forecast Apple's short-term stock prices using multiple time series and machine learning models:
- **ARIMA**
- **Prophet**
- **LSTM Neural Networks**
- **XGBoost / Random Forest**

## Data
- Source: Yahoo Finance (`yfinance`)
- Ticker: `AAPL`
- Timeframe: Last 2 years (daily OHLCV data)

## Features
- OHLCV (Open, High, Low, Close, Volume)
- Technical indicators: SMA, EMA, RSI, MACD
- Lag features, returns, rolling averages

## Methodology
1. **Data Collection**: Via `yfinance`
2. **Feature Engineering**: In `features.py`
3. **Model Training**: All models handled modularly in `model.py`
4. **Evaluation**: RMSE, MAE, directional accuracy, plots
5. **Backtesting**: Optional walk-forward validation

## Repo Structure
```
1-equity-price-forecasting/
├── data/              # Raw OHLCV data from Yahoo Finance
├── notebooks/         # Notebooks for exploration and modeling
│   └── forecasting_models.ipynb
├── src/               # Python modules
│   ├── features.py
│   ├── model.py
│   └── utils.py
├── README.md          # Project overview
├── requirements.txt   # Python dependencies
└── .gitignore         # Files/folders to ignore in git
```

## Tools & Libraries
- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `yfinance`, `ta`, `statsmodels`, `prophet`, `tensorflow`, `scikit-learn`, `xgboost`

## Next Steps
- [ ] Implement feature extraction logic in `features.py`
- [ ] Populate `model.py` with model training/prediction functions
- [ ] Build comparative modeling workflow in the notebook
- [ ] Evaluate and visualize model performance

---

Ready for you to start coding — let me know when you'd like me to scaffold `features.py`, `model.py`, and the starter notebook.
