import pandas as pd
from prophet import Prophet
from statsmodels.tsa.arima.model import ARIMA
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

# ARIMA
def train_arima(df):
    model = ARIMA(df['Close'], order=(5,1,0))
    result = model.fit()
    return result

# Prophet
def train_prophet(df):
    df = df.copy()
    df['ds'] = df.index
    df['y'] = df['Close']
    df_prophet = df[['ds', 'y']]
    model = Prophet()
    model.fit(df_prophet)
    return model

# Random Forest / XGBoost
def train_tree_model(df, model_type='rf'):
    df = df.dropna()
    features = [col for col in df.columns if col not in ['Close']]
    X = df[features]
    y = df['Close']

    if model_type == 'rf':
        model = RandomForestRegressor(n_estimators=100, random_state=42)
    else:
        model = XGBRegressor(n_estimators=100, random_state=42)

    model.fit(X, y)
    return model