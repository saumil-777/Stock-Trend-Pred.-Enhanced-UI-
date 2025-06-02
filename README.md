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
Install dependencies
(You can use requirements.txt from the repo or create a virtual environment)

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
streamlit run app.py
🔧 Folder Structure
bash
Copy
Edit
stock-trend-predictor/
├── app.py                # Main Streamlit application
├── keras_model.h5        # Pretrained LSTM model
├── requirements.txt
└── README.md
🌐 Deployment (Streamlit Cloud)
Push your project to GitHub.

Go to Streamlit Cloud and connect your GitHub repo.

Select app.py as the main file.

Add a keras_model.h5 file to the root directory of your repo.

Add your requirements.txt file (include tensorflow, yfinance, streamlit, etc.)

Click Deploy(Link- ).

📝 Example Tickers
Try entering:

AAPL – Apple Inc.

GOOGL – Alphabet Inc.

TSLA – Tesla Inc.

MSFT – Microsoft

🧠 Model Info
The backend model is an LSTM (Long Short-Term Memory) neural network trained on normalized closing prices. It takes in sequences of the past 100 days to predict future stock trends.

📷 Screenshots (optional)
Dashboard	Prediction Plot

Add a /screenshots/ folder with sample images if you'd like visuals.

🙌 Credits
Built by Your Name

Powered by Streamlit

