## 📈 S&P 500 Price Prediction using Machine Learning

### 🔍 Objective
The goal of this project is to build a reliable machine learning model that can predict the closing prices of the S&P 500 index using historical market data. This project demonstrates how financial time series data can be leveraged for forecasting and investment insight.

### 🛠️ Methods
- **Data Preprocessing**: Loaded 5 years of historical S&P 500 data. Cleaned missing values, handled time formats, and generated lag-based features.
- **Feature Engineering**: Created indicators like moving averages, price momentum, and volume-based metrics to enrich predictive signals.
- **Model Selection**: Trained and compared several regression algorithms:
  - Linear Regression
  - Random Forest Regressor
  - Support Vector Regressor (SVR)
  - K-Nearest Neighbors (KNN)
- **Feature Selection**: Used `SelectKBest` with `f_regression` to identify the top 5 influential features.
- **Evaluation**: Evaluated models using R² score and 5-fold cross-validation to ensure generalization.

### 📊 Results
- The best-performing model achieved an **R² score close to 0.99**, indicating it explains 99% of the variance in S&P 500 prices.
- The model successfully learned patterns influenced by key indicators like volume changes, moving averages, and short-term price shifts.
- Visual comparison of predicted vs actual prices showed strong alignment and consistency.

### 💡 Insights & Business Value
- High prediction accuracy is valuable for:
  - **Algorithmic trading strategies**
  - **Portfolio rebalancing**
  - **Market timing and entry/exit planning**
- This type of model, retrained frequently with new data, could support **real-time financial analysis**.

### 🧠 Conclusion & Next Steps
This project demonstrates the capability of classic machine learning techniques to forecast financial time series data with high accuracy. Future improvements could include:
- Incorporating macroeconomic data (inflation, interest rates, GDP growth)
- Implementing deep learning models like LSTMs for sequential prediction
- Creating a live dashboard or automated trading simulation to showcase applied usage

---

### ✅ Built for Portfolio Submission – Wealthsimple Application
This project was created to showcase practical machine learning skills, data storytelling, and financial insight for a role in fintech, specifically targeting Wealthsimple.

 
