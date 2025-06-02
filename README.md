# 📈 Stock Trend Predictor

A Streamlit web app for predicting stock trends using historical data and an LSTM model. This enhanced version features a modern UI, sidebar configuration, better data visuals, and improved interactivity.

---

## 🚀 Features

- 📊 Displays historical stock data from **Yahoo Finance**
- 🧮 Calculates & visualizes **100-day** and **200-day moving averages**
- 🤖 Uses a pre-trained **LSTM model** (Keras) to predict future stock prices
- 📈 Compares predicted vs actual closing prices
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

###Click Deploy(Link- ).

###📝 Example Tickers
Try entering:

AAPL – Apple Inc.

GOOGL – Alphabet Inc.

TSLA – Tesla Inc.

MSFT – Microsoft

###🧠 Model Info
The backend model is an LSTM (Long Short-Term Memory) neural network trained on normalized closing prices. It takes in sequences of the past 100 days to predict future stock trends.

## 🖼️ Screenshots

### 🔹 Main UI
![UI]([screenshots/ui.png](https://github.com/saumil-777/Stock-Trend-Pred.-Enhanced-UI-/blob/83c01821c9db4ae42111673bcd7be00109d56158/Screenshot%202025-06-02%20113152.png)

### 🔹 Closing Price Over Time
![Closing Price](screenshots/closing_price.png)

### 🔹 Moving Averages
![Moving Averages](screenshots/moving_averages.png)


🙌 Credits
Built by Saumil Singhal

Powered by Streamlit

