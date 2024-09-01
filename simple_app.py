
# import streamlit as st
# import numpy as np
# import joblib
# import pickle
# # Import joblib for loading the model
# # try:
# #     with open('model.pkl', 'rb') as file:
# #         loaded_model = joblib.load(file)
# # except FileNotFoundError:
# #     st.error("Model file not found. Please make sure 'detection.pkl' exists.")
# # except Exception as e:
# #     st.error(f"An error occurred while loading the model: {e}")


# # Load the model
# model = joblib.load('model.pkl')

# # Streamlit UI
# st.title("Network Attack Detection System")

# A = st.number_input("Fwd Packet Length Max", format="%.2f")
# B = st.number_input("Flow IAT Mean", format="%.2f")
# C = st.number_input("Fwd IAT Std", format="%.2f")
# D = st.number_input("Packet Length Variance", format="%.2f")
# E = st.number_input("Init Fwd Win Bytes", format="%.2f")

# label_mapping = {
#     0: 'Benign', 1: 'Bot', 2: 'DDoS', 3: 'DoS GoldenEye',
#     4: 'DoS Hulk', 5: 'DoS Slowhttptest', 6: 'DoS slowloris',
#     7: 'FTP-Patator', 8: 'Heartbleed', 9: 'Infiltration', 10: 'PortScan',
#     11: 'SSH-Patator', 12: 'Web Attack - Brute Force', 13: 'Web Attack - Sql Injection',
#     14: 'Web Attack - XSS'
# }

# col1, col2, col3, col4, col5 = st.columns(5)
# with col3:
#     btn = st.button("Predict")

# # Predict and display the result
# if btn:
#     input_data = np.array([A, B, C, D, E]).reshape(1, -1)
#     pred = model.predict(input_data)
#     label = label_mapping.get(pred[0], "Unknown")
#     st.write(f"Prediction: {label}")
    

import streamlit as st
import numpy as np
import joblib
import pickle

# Load the model with error handling
try:
    with open('C:/Users/pvste/Desktop/ML CDAC Project/project/model.pkl', 'rb') as file:
        model = joblib.load(file)
except FileNotFoundError:
    st.error("Model file not found. Please make sure 'model.pkl' exists.")
    st.stop()  # Stop further execution
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    st.stop()

# Streamlit UI
st.title("Network Attack Detection System")

# Number inputs for features
A = st.number_input("Fwd Packet Length Max", format="%.2f")
B = st.number_input("Flow IAT Mean", format="%.2f")
C = st.number_input("Fwd IAT Std", format="%.2f")
D = st.number_input("Packet Length Variance", format="%.2f")
E = st.number_input("Init Fwd Win Bytes", format="%.2f")

# Mapping of model's prediction to human-readable labels
label_mapping = {
    0: 'Benign', 1: 'Bot', 2: 'DDoS', 3: 'DoS GoldenEye',
    4: 'DoS Hulk', 5: 'DoS Slowhttptest', 6: 'DoS slowloris',
    7: 'FTP-Patator', 8: 'Heartbleed', 9: 'Infiltration', 10: 'PortScan',
    11: 'SSH-Patator', 12: 'Web Attack - Brute Force', 13: 'Web Attack - Sql Injection',
    14: 'Web Attack - XSS'
}

# Layout columns for better UI placement
col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    btn = st.button("Predict")

# Predict and display the result
if btn:
    input_data = np.array([A, B, C, D, E]).reshape(1, -1)
    try:
        pred = model.predict(input_data)
        label = label_mapping.get(pred[0], "Unknown")
        st.write(f"Prediction: {label}")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")







