# Used-Car-Price-Prediction


A machine learning-powered web app that predicts the selling price of a used car based on its specifications. Built using **XGBoost**, **Streamlit**, and **Pandas**, it's ideal for learning ML deployment and showcasing projects.

---

##📊 Overview

This app predicts the price of a used car based on:
- Brand
- Year of purchase
- Kilometers driven
- Fuel type
- Transmission type
- Seller type
- Ownership status

The backend is powered by a trained **XGBoost Regressor** model stored in `model.pkl`.

---

## 🛠 Tech Stack

- 🐍 Python 3
- 📈 XGBoost
- 📊 Pandas
- 🌐 Streamlit
- 💾 Pickle

---

## 📁 Project Structure

📦 used-car-price-predictor/
├── app.py # Streamlit web app
├── model.pkl # Trained XGBoost model
├── CAR DETAILS FROM CAR DEKHO.csv # Original training dataset
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## 🚀 How to Run Locally


# 1. Clone the repository
```bash
git clone 
cd used-car-price-predictor
```
# 2. (Optional) Create and activate a virtual environment
```bash
python -m venv env
```
**On Windows:**
```bash
env\Scripts\activate
```
**On macOS/Linux:**
```bash
source env/bin/activate
```
# 3. Install all dependencies
```bash
pip install -r requirements.txt
```
# 4. Run the Streamlit app
```bash
streamlit run app.py
```
