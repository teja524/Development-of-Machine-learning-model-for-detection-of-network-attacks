
# 🛡️ Network Attack Detection Using Machine Learning

This project focuses on developing a machine learning model to detect and classify network attacks in real-time. By leveraging the power of Random Forest algorithms, the project aims to enhance the accuracy and speed of intrusion detection systems (IDS) to secure networks from evolving cyber threats.

## 📂 Project Overview

### Objective
To create an efficient and accurate machine learning model that can detect various network attacks, including novel threats, using the CICIDS2017 dataset.

### Key Features
- **Random Forest Model:** Utilizes Random Forest for feature selection and classification.
- **Real-time Detection:** Capable of detecting and classifying network attacks in real-time.
- **Data Preprocessing:** Includes data cleaning, feature extraction, and normalization.
- **Streamlit UI:** A user-friendly interface for interacting with the model and visualizing results.

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Jupyter Notebook
- Streamlit

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/network-attack-detection.git
   cd network-attack-detection
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project
1. **Data Preprocessing:**
   - Run the preprocessing script to clean and prepare the data.
   ```bash
   python preprocess_data.py
   ```
2. **Model Training:**
   - Train the model using the prepared dataset.
   ```bash
   python train_model.py
   ```
3. **Real-time Detection:**
   - Launch the Streamlit app for real-time network attack detection.
   ```bash
   streamlit run app.py
   ```

## 📊 Model Evaluation

The Random Forest model was evaluated against K-Nearest Neighbors (KNN) and Decision Tree classifiers, showing superior performance in terms of accuracy, precision, and F1-score.

- **Random Forest Accuracy:** 98.35%
- **Decision Tree Accuracy:** 98.17%
- **KNN Accuracy:** 93.30%

## 🛠️ Features

- **Intrusion Detection:** Detects and classifies network traffic as benign or malicious.
- **Real-time Monitoring:** Continuously monitors network traffic to identify potential threats.
- **User Interface:** Built using Streamlit for ease of use and accessibility.

## 📚 Dataset

This project uses the CICIDS2017 dataset, which contains a comprehensive set of network traffic data, including normal traffic and various types of attacks.

Thank You.
