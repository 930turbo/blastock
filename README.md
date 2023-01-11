# Blastock 📈🚀

Welcome to Blastock, the easiest way to view stock data in just a few simple steps.

## Getting Started

This code prompts the user to enter a stock ticker symbol, retrieve the historical data for that stock using the yfinance library, and plot the closing price over time using matplotlib. After that, it prompts the user to select the type of model they want to use for prediction (linear, gbm, lstm).

For the linear model, the code uses the linear regression algorithm to make the prediction. For GBM it uses the GradientBoostingRegressor algorithm from sklearn package. And for LSTM it uses a sequential model from Keras library,  where it reshapes the input data and using 2 LSTM layers and a dense layer to make the prediction. The code also compares the predicted value with the last closing price, and makes a recommendation to the user if they should invest or not based on previous trends.

It's important to mention that this is a very basic example of how these models can be used for stock prediction, and it's not expected to get accurate results on real-world scenarios. It's also important to note that these models are only one aspect to consider when making predictions and investment decisions, and should be used in conjunction with other analysis such as fundamental analysis, and monitoring of the overall economy, industry performance, and any relevant news or events. Also, it's essential to understand the concept behind these models and the math and statistics behind them to correctly use them.

Additionally, in a real-world scenario, other considerations should be taken into account such as data preprocessing, feature engineering, and model tuning.
Data preprocessing is crucial for the training process, it can include cleaning the data, handling missing values, normalizing or standardizing the data, etc. Feature engineering is the process of creating new features from the data that can improve the model performance. And model tuning is the process of adjusting the parameters of the model to improve its performance.

Another important point is to evaluate the performance of the model and to use different performance metrics such as accuracy, precision, recall or ROC-AUC to compare the performance of different models.

It's also essential to have a large set of data to train the model, otherwise the model will be overfitting. It's also important to use a separate set of data for testing and evaluating the performance of the model.

In summary, this example is a simple demonstration of how stock market monitor can be implemented in Python using multiple models, LSTMs, and GBM for predictions. It's important to keep in mind that stock prediction is a complex task that requires a significant amount of knowledge in data science and finance, and it's not as simple as running a script. It is important to understand the concepts behind the models, the data, and to use various techniques to improve model performance.
