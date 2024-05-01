import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load the dataset
def app():
    def load_data():
        df = pd.read_csv('//Users//kashifkhan//Desktop//streamlit//lungcancer.csv')
        # Dropping 'index' and 'Patient Id' columns
        df.drop(['index', 'Patient Id', 'Clubbing of Finger Nails','Gender','OccuPational Hazards'], axis=1, inplace=True)
        return df

    df = load_data()

    # Encode categorical variables
    encoder = LabelEncoder()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    encoders = {}
    for col in categorical_cols:
        df[col] = encoder.fit_transform(df[col])
        encoders[col] = encoder

    # Split data into features and target variable
    X = df.drop('Level', axis=1)
    y = df['Level']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model training
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # Sidebar for user inputs
    st.title("Lung Cancer Prediction")
    st.title("Please select your inputs:")

    # User inputs
    user_inputs = {}
    for col in X.columns:
        if col == 'Age':
            user_inputs[col] = st.slider(f"{col}", min_value=0, max_value=100, value=50)
    
        
        else:
            user_inputs[col] = st.slider(f"{col}", min_value=0, max_value=7)

    # Convert user inputs into DataFrame
    input_df = pd.DataFrame([user_inputs])

    # Define function to predict lung cancer
    def predict_lung_cancer(input_data):
        input_df = pd.DataFrame(input_data, index=[0])
        input_df.columns = X.columns
        input_df = input_df.apply(lambda x: encoders[x.name].transform([x])[0] if x.name in encoders else x)
        prediction = rf_model.predict(input_df)
        return prediction

    # Display model performance
    st.sidebar.title("Model Performance")
    y_pred = rf_model.predict(X)
    accuracy = accuracy_score(y, y_pred)
    st.sidebar.write("Accuracy:", accuracy)
    # st.write("Classification Report:")
    # st.write(classification_report(y, y_pred))

    if st.button('Predict'):
        # Predict lung cancer
        prediction = predict_lung_cancer(user_inputs)
    
        # Display prediction
        st.title("Lung Cancer Prediction Result")
        st.write("Predicted Lung Cancer:", "No" if prediction[0] == 1 else "Yes")

