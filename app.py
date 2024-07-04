import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.express as px


uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

page = st.sidebar.selectbox("Choose a page", ["Forecast", "Analysis"])


def preprocess_data(data):
            columns = ['Date', 'Close']
            ndf = data[columns]
            ndf.rename(columns={'Date' : 'ds', 'Close' : 'y'} , inplace=True)
            return ndf
        

def time_extraction(data):
            data['Date'] = pd.to_datetime(data['Date'])
            data['year'] = data['Date'].dt.year
            data['month'] = data['Date'].dt.month
            data['day'] = data['Date'].dt.day
            
            
            return data




if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    file_name = uploaded_file.name.split(".")
    file_name = file_name[0]
    if page == "Forecast":
        
        st.title(f'{file_name} Stock Forecasting with Prophet')        
        
        ndf = preprocess_data(data)
        # Display the first few rows of the data
        st.write("Data Preview:")
        st.write(data.head())

        # Check if data has the required columns
        if 'ds' in ndf.columns and 'y' in ndf.columns:
            # Initialize the Prophet model
            model = Prophet()

            # Fit the model to your data
            model.fit(ndf)

            # Create a dataframe for future predictions (e.g., predicting for the next 365 days)
            future = model.make_future_dataframe(periods=365)

            # Make the predictions
            forecast = model.predict(future)

            # Display the predictions
            st.write("Forecast Preview:")
            st.write(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

            # Plot the forecast
            fig1 = model.plot(forecast)
            st.pyplot(fig1)

            # Plot the forecast components
            fig2 = model.plot_components(forecast)
            st.pyplot(fig2)
        else:
            st.error("The uploaded file does not have the required columns 'ds' and 'y'.")
    
    elif page == "Analysis":
        st.title(f'{file_name} Stock Analysis')
        st.header("Basic Statistics")
        st.write(data.describe())
        
        
        
        data = time_extraction(data)
        fig1 = px.area(data, x='Date', y='Close', title="Close Prices Trend")
        st.plotly_chart(fig1)
        
        fig2 = px.histogram(data, x='Close', nbins=50, title='Distribution of Close Prices')
        st.plotly_chart(fig2)
        
        fig3 = px.bar(data, x='year', y='Close', title='Close Prices By year')
        st.plotly_chart(fig3)
        
        fig4 = px.bar(data, x='day', y='Close', title='Close Prices By day')
        st.plotly_chart(fig4)

        
    else:
        st.title("page not found")
        
        
            
            
        
else:
    st.title("Stock prices Forecast and Analysis")
    st.write("Please upload a CSV file to proceed.")
