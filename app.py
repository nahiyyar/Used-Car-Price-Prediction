import streamlit as st
import pandas as pd
import xgboost
from xgboost import XGBRegressor
import pickle as pk

st.title("Used Car Price Predictor")

model=pk.load(open('model.pkl','rb'))
df=pd.read_csv('CAR DETAILS FROM CAR DEKHO.csv')

# Input fields
year = st.number_input("Car Year", 1990, 2025, 2015)
km_driven = st.number_input("Kilometers Driven", 0, 500000, 30000)
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
brand = st.selectbox("Brand",['Maruti', 'Hyundai', 'Datsun', 'Honda', 'Tata', 'Chevrolet',
       'Toyota', 'Jaguar', 'Mercedes-Benz', 'Audi', 'Skoda', 'Jeep',
       'BMW', 'Mahindra', 'Ford', 'Nissan', 'Renault', 'Fiat',
       'Volkswagen', 'Volvo', 'Mitsubishi', 'Land', 'Daewoo', 'MG',
       'Force', 'Isuzu', 'OpelCorsa', 'Ambassador', 'Kia'])
fuel_type=st.selectbox("Fuel Type",['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
seller_type=st.selectbox("Seller Type",['Individual', 'Dealer', 'Trustmark Dealer'])
owner=st.selectbox("owner",['First Owner', 'Second Owner', 'Fourth & Above Owner',
       'Third Owner', 'Test Drive Car'])


if st.button("Predict"):
    input_data_model = pd.DataFrame(
    [[year,km_driven,fuel_type,seller_type,transmission,owner,brand]],
    columns=['year','km_driven','fuel','seller_type','transmission','owner','brand'])
    
    # 🛠 1. Define your mapping dictionaries
    brand_map = {
        'Maruti': 0, 'Hyundai': 1, 'Datsun': 2, 'Honda': 3, 'Tata': 4, 'Chevrolet': 5,
        'Toyota': 6, 'Jaguar': 7, 'Mercedes-Benz': 8, 'Audi': 9, 'Skoda': 10, 'Jeep': 11,
        'BMW': 12, 'Mahindra': 13, 'Ford': 14, 'Nissan': 15, 'Renault': 16, 'Fiat': 17,
        'Volkswagen': 18, 'Volvo': 19, 'Mitsubishi': 20, 'Land': 21, 'Daewoo': 22, 'MG': 23,
        'Force': 24, 'Isuzu': 25, 'OpelCorsa': 26, 'Ambassador': 27, 'Kia': 28
    }

    fuel_map = {'Petrol': 0, 'Diesel': 1, 'CNG': 2, 'LPG': 3, 'Electric': 4}
    seller_map = {'Individual': 0, 'Dealer': 1, 'Trustmark Dealer': 2}
    trans_map = {'Manual': 1, 'Automatic': 2}
    owner_map = {
        'First Owner': 0, 'Second Owner': 1, 'Third Owner': 2,
        'Fourth & Above Owner': 3, 'Test Drive Car': 4
    }

    # 🛠 2. Apply all mappings with .map() — DO NOT use replace() or inplace
    input_data_model['brand'] = input_data_model['brand'].map(brand_map)
    input_data_model['fuel'] = input_data_model['fuel'].map(fuel_map)
    input_data_model['seller_type'] = input_data_model['seller_type'].map(seller_map)
    input_data_model['transmission'] = input_data_model['transmission'].map(trans_map)
    input_data_model['owner'] = input_data_model['owner'].map(owner_map)

    input_data_model = input_data_model.astype(int)

    if input_data_model.isnull().any().any():
        st.error("❌ Error: One or more input values could not be encoded. Please check input.")
        st.write(input_data_model)  # Show what's wrong
    else:
        input_data_model = input_data_model.astype(int)
        input_data_model = input_data_model[['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'brand']]
        car_price = model.predict(input_data_model)
        st.success(f"💰 Estimated Price: ₹{int(car_price[0]):,}")

    car_price = model.predict(input_data_model)

    st.markdown('Car Price is going to be '+ str(car_price[0]))