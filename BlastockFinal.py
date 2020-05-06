import importlib
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
# matplotlib does not use datetime dates so we need this next import
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

tickerSym = input("Enter ticker symbol desired: ")

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2020,1,1)

df = web.DataReader(tickerSym, 'yahoo', start, end)

# ma = moving average / This will take todays price and the last 49 days and come up with an average. This makes it easier for us to see up-trends etc
df['50ma'] = df['Adj Close'].rolling(window=100, min_periods = 0).mean()
df.dropna(inplace=True)

# ohlc = open high low close    
# Resample data for 5 days
df_ohlc = df['Adj Close'].resample('5D').ohlc()
# This way we get the true volume instead of the average volume
df_volume = df['Volume'].resample('5D').sum()

df_ohlc.reset_index(inplace = True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
print(df_ohlc.head())

df.dropna(inplace=True)
print(df.head())

ax1 = plt.subplot2grid((10,1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((10,1), (5,0), rowspan = 1, colspan = 1, sharex = ax1)
# Will take MDates and make them 'nice' looking showing actual text
ax1.xaxis_date()

# Define size of candlesticks and color, I have blue set to up and red set to down
candlestick_ohlc(ax1, df_ohlc.values, width = 3, colorup = 'b')
# Have to map for the x and then the volume will be the y (the zero will fill x and y)
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

ax1.plot(df.index, df['Adj Close']) 
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

print(df[['Open', 'High']].head())

df.plot()
# Generates second grid where you can see legend and more data
plt.legend(loc='best')
plt.show()
