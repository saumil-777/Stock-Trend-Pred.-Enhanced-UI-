# 📈 Stock Trend Predictor

A Streamlit web app for predicting stock trends using historical data and an LSTM model. This enhanced version features a modern UI, sidebar configuration, better data visuals, and improved interactivity.

---

## 🚀 Features

- 📊 Displays historical stock data from **Yahoo Finance**
- 🧮 Calculates & visualizes **100-day** and **200-day moving averages**
- 🤖 Uses a pre-trained **LSTM model** (Keras) to predict future stock prices
- 📈 Compares predicted vs actual closing prices
- 🗓️ Allows users to select custom start and end dates for analysis
- 🔮 Predicts the **next trading day’s closing price** based on selected data range
- 🖼️ Enhanced UI with **sidebar controls**, **responsive plots**, and **tooltips**

---

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/)
- [yFinance](https://pypi.org/project/yfinance/)
- [Keras](https://keras.io/)
- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [scikit-learn](https://scikit-learn.org/)

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/stock-trend-predictor.git
   cd stock-trend-predictor
1. **Clone this repository:**

   ```bash
   git clone https://github.com/saumil-777/stock-trend-predictor-basic.git
   cd stock-trend-predictor-basic
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   *(If you don’t have a `requirements.txt`, manually install: `streamlit`, `keras`, `pandas`, `numpy`, `matplotlib`, `yfinance`)*

3. **Run the app:**

   ```bash
   streamlit run app.py
   ```

4. **Model file:**

   Make sure `keras_model.h5` is present in the same folder as `app.py`.

----
📝 Usage
Enter the desired stock ticker symbol (e.g., AAPL, TSLA) in the sidebar.

Select the start date and end date for the historical data you want to analyze.

The app will fetch stock data within this range, display statistics, plot closing prices, and moving averages.

The LSTM model will use the latest 100 days of data within your chosen range to predict the closing price for the next trading day (the day after your selected end date).

This dynamic date selection allows you to predict future stock trends up to the latest available data.
   
----
### 📝 Example Tickers
Try entering:

AAPL – Apple Inc.

GOOGL – Alphabet Inc.

TSLA – Tesla Inc.

MSFT – Microsoft



### 🧠 Model Info
The backend model is an LSTM (Long Short-Term Memory) neural network trained on normalized closing prices. It takes in sequences of the past 100 days to predict future stock trends.

----
## 🖼️ Screenshots

### 🔹 Main UI
![UI](https://github.com/saumil-777/Stock-Trend-Pred.-Enhanced-UI-/blob/83c01821c9db4ae42111673bcd7be00109d56158/Screenshot%202025-06-02%20113152.png)

### 🔹Data Summary and Closing Price Over Time
![Closing Price](https://github.com/saumil-777/Stock-Trend-Pred.-Enhanced-UI-/blob/8ebe52afae87088f2854a6c361d9f131865d533c/Screenshot%202025-06-02%20120914.png)

### 🔹 Moving Averages
![Moving Averages](https://github.com/saumil-777/Stock-Trend-Pred.-Enhanced-UI-/blob/9777ef8934cbc92b3a8014d2b52a8d750c8454c7/Screenshot%202025-06-02%20113219.png)

----

## Live Demo - https://ibkasmuyp5kvevrfazpdqh.streamlit.app/

----
🙌 Credits
Built by Saumil Singhal

Powered by Streamlit

