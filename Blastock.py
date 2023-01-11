import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from keras.models import Sequential
from keras.layers import LSTM, Dense

def get_data(ticker):
    # Get stock data from yahoo finance
    data = yf.download(ticker)
    return data

def plot_data(data):
    # Plot the closing price over time
    data['Close'].plot(figsize=(10,5))
    plt.ylabel("Closing Price")
    plt.xlabel("Date")
    plt.show()

def make_prediction(data, model_type='linear'):
    if model_type == 'linear':
        # Use linear regression to make a prediction
        X = range(0,len(data.index))
        X = pd.DataFrame(X)
        y = data['Close']
        model = LinearRegression().fit(X,y)
        prediction = model.predict([[len(data.index)]])
    elif model_type == 'gbm':
        # Use GBM to make a prediction
        X = range(0,len(data.index))
        X = pd.DataFrame(X)
        y = data['Close']
        model = GradientBoostingRegressor().fit(X, y)
        prediction = model.predict([[len(data.index)]])
    elif model_type == 'lstm':
        # Use LSTM to make a prediction
        X = data['Close'].values
        X = X.reshape(len(X), 1)
        model = Sequential()
        model.add(LSTM(50, return_sequences=True, input_shape=(1, 1)))
        model.add(LSTM(50))
        model.add(Dense(1))
        model.compile(loss='mean_squared_error', optimizer='adam')
        model.fit(X, y, epochs=100, batch_size=1, verbose=2)
        prediction = model.predict([[len(data.index)]])
    return prediction

def should_invest(prediction, current_price):
    # Make a recommendation to invest or not
    if prediction > current_price:
        print("Based on previous trends, it may be a good idea to invest in this stock.")
    else:
        print("Based on previous trends, it may not be a good idea to invest in this stock.")

if __name__ == "__main__":
    ticker = input("Enter the ticker symbol of the stock you want to monitor: ")
    data = get_data(ticker)
    plot_data(data)
    model_type = input("Enter the type of model you want to use (linear, gbm, lstm): ")
prediction = make_prediction(data, model_type)
current_price = data['Close'][-1]
should_invest(prediction, current_price)
