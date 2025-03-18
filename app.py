import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn

print(f"App using scikit-learn version: {sklearn.__version__}")

# Set page configuration
st.set_page_config(page_title="E-commerce Prediction App", layout="wide")
st.title("E-commerce Sales Prediction")

@st.cache_resource
def load_model():
    try:
        with open('model.pkl', 'rb') as file:
            model = pickle.load(file)
            # Get feature names from model if available
            feature_names = model.feature_names_in_ if hasattr(model, 'feature_names_in_') else None
        if not hasattr(model, 'predict'):
            raise AttributeError("Loaded object is not a valid model")
        return model, feature_names
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None, None

def user_input_features(feature_names):
    # Create input fields for each feature in the correct order
    inputs = {}
    
    for feature in feature_names:
        if feature == 'CustomerID':
            inputs[feature] = st.sidebar.number_input('Customer ID', min_value=0, max_value=10000, value=1000)
        elif feature == 'DayOfWeek':
            inputs[feature] = st.sidebar.selectbox('Day of Week', options=list(range(1, 8)))
        elif feature == 'Hour':
            inputs[feature] = st.sidebar.slider('Hour', min_value=0, max_value=23, value=12)
        elif feature == 'Month':
            inputs[feature] = st.sidebar.selectbox('Month', options=list(range(1, 13)))
        elif feature == 'UnitPrice':
            inputs[feature] = st.sidebar.number_input('Unit Price', min_value=0.0, max_value=1000.0, value=10.0)
    
    # Create DataFrame with features in the correct order
    return pd.DataFrame([inputs])

# Create sidebar for user inputs
st.sidebar.header("Input Parameters")

# Load model and feature names
model, feature_names = load_model()

if model is not None and feature_names is not None:
    st.sidebar.write("Required features (in order):", feature_names)
    df = user_input_features(feature_names)
    
    st.subheader('User Input Parameters')
    st.write(df)
    
    if st.button('Predict'):
        try:
            prediction = model.predict(df)
            st.subheader('Prediction')
            st.write(f'Predicted Value: {prediction[0]:.2f}')
        except Exception as e:
            st.error(f"Prediction error: {str(e)}")
else:
    st.error("Could not load model or determine feature names")