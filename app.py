import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
import streamlit as st
import yfinance as yf
import os
from datetime import datetime, timedelta

# -----------------------------
# Page Setup
# -----------------------------
st.set_page_config(page_title="Stock Trend Predictor", layout="wide")
st.title('📈 Stock Trend Prediction')

# -----------------------------
# Sidebar Input
# -----------------------------
with st.sidebar:
    st.header("🛠️ Settings")
    user_input = st.text_input('Enter Stock Ticker (e.g. AAPL, TSLA)', 'AAPL')
    start_date = st.date_input("Start Date", pd.to_datetime('2010-01-01'))
    end_date = st.date_input("End Date (latest available date)", datetime.today())

# -----------------------------
# Load Data
# -----------------------------
df = yf.download(user_input, start=start_date, end=end_date)

# -----------------------------
# Show Data Summary
# -----------------------------
st.subheader('📊 Data Statistics ({} - {})'.format(start_date, end_date))
with st.expander("🔍 Show Data Summary"):
    st.write(df.describe())

# -----------------------------
# Plot: Closing Price
# -----------------------------
st.subheader('🔹 Closing Price Over Time')
st.line_chart(df['Close'], use_container_width=True)

# -----------------------------
# Moving Averages
# -----------------------------
ma100 = df['Close'].rolling(100).mean()
ma200 = df['Close'].rolling(200).mean()

col1, col2 = st.columns(2)

with col1:
    st.subheader('📉 Closing Price with 100 MA')
    fig, ax = plt.subplots()
    ax.plot(df['Close'], label='Close')
    ax.plot(ma100, label='100 MA', color='orange')
    ax.legend()
    st.pyplot(fig, use_container_width=True)

with col2:
    st.subheader('📉 100 & 200 MA')
    fig2, ax2 = plt.subplots()
    ax2.plot(df['Close'], label='Close')
    ax2.plot(ma100, label='100 MA', color='orange')
    ax2.plot(ma200, label='200 MA', color='green')
    ax2.legend()
    st.pyplot(fig2, use_container_width=True)

# -----------------------------
# Data Splitting
# -----------------------------
data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70):])
scaler = MinMaxScaler(feature_range=(0,1))
data_training_array = scaler.fit_transform(data_training)

# -----------------------------
# Load Model
# -----------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'keras_model.h5')
model = load_model(model_path)

# -----------------------------
# Prepare Test Data
# -----------------------------
past_100_days = data_training.tail(100)
final_df = pd.concat([past_100_days, data_testing], ignore_index=True)
input_data = scaler.fit_transform(final_df)

x_test = []
y_test = []

for i in range(100, input_data.shape[0]):
    x_test.append(input_data[i-100:i])
    y_test.append(input_data[i, 0])

x_test, y_test = np.array(x_test), np.array(y_test)
y_predicted = model.predict(x_test)

# Rescaling
scaling_factor = 1 / scaler.scale_[0]
y_predicted *= scaling_factor
y_test *= scaling_factor

# -----------------------------
# Prediction Plot
# -----------------------------
st.subheader('📈 Predicted vs Original Price')
fig3, ax3 = plt.subplots(figsize=(8, 4))
ax3.plot(y_test, 'b', label='Original Price')
ax3.plot(y_predicted, 'r', label='Predicted Price')
ax3.set_xlabel('Time')
ax3.set_ylabel('Stock Price')
ax3.legend()
st.pyplot(fig3, use_container_width=True)

# -----------------------------
# Predict Tomorrow's Price
# -----------------------------
st.subheader("🔮 Predict Tomorrow's Closing Price")

if st.button("Predict"):
    last_100_days = df['Close'].tail(100).values.reshape(-1, 1)
    scaled_input = scaler.transform(last_100_days)
    x_future = []
    x_future.append(scaled_input)
    x_future = np.array(x_future)
    
    pred = model.predict(x_future)
    predicted_price = pred[0][0] * scaling_factor

    next_day = df.index[-1] + timedelta(days=1)
    st.success(f"📅 Predicted closing price for **{next_day.date()}**: **${predicted_price:.2f}**")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("🚀 Built with Streamlit, yFinance, Keras & Matplotlib")
