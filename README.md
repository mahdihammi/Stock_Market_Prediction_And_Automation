# Stock Price Forecasting Application

## Introduction
This application is designed to forecast stock prices using the fbProphet model, a robust time series forecasting tool developed by Facebook. The data is collected from Yahoo Finance, and the entire process is automated through a user-friendly Streamlit interface. Users can upload their stock data, and the application will instantly generate comprehensive analysis and forecasting results.

## Dataset
The application utilizes historical stock price data from Yahoo Finance. Users need to upload a CSV file containing the following columns:

Date: The date of the stock price. <br>
Open: The opening price. <br>
High: The highest price during the day. <br>
Low: The lowest price during the day. <br>
Close: The closing price. <br>
Volume: The trading volume. <br>

## fbProphet Model
The fbProphet model is used for forecasting. It is particularly effective for time series data that have strong seasonal effects and several seasons of historical data. The model handles missing data, outliers, and shifts in the trend. you can learn more about the model in this link : https://facebook.github.io/prophet/docs/quick_start.html <br>

## Streamlit App

