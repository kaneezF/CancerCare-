import os
import cv2
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import random
import shutil

def load_images_and_preprocess(path, classes, reduction_factor=None):
    X = []
    Y = []
    for cls in classes:
        pth = os.path.join(path, cls)
        files = os.listdir(pth)
        if reduction_factor is not None:
            num_samples_to_keep = int(len(files) * reduction_factor)
            files = random.sample(files, num_samples_to_keep)
        for j in files:
            img = cv2.imread(os.path.join(pth, j), 0)
            img = cv2.resize(img, (200, 200))
            X.append(img)
            Y.append(classes[cls])
    X = np.array(X)
    Y = np.array(Y)
    X_updated = X.reshape(len(X), -1)
    return X_updated, Y

def app():
    # Load data with optional reduction
    path = "/Users/kashifkhan/Desktop/streamlit/Training"
    classes = {'notumor': 0, 'pituitary': 1, 'glioma': 2, 'meningioma': 3}
    reduction_factor = 0.5  # Adjust this as needed
    X, Y = load_images_and_preprocess(path, classes, reduction_factor)

    # Split data into train and test sets
    xtrain, xtest, ytrain, ytest = train_test_split(X, Y, random_state=10, test_size=.20)

    # Reshape images to 40,000 features
    xtrain_flat = xtrain.reshape(xtrain.shape[0], -1)
    xtest_flat = xtest.reshape(xtest.shape[0], -1)

    # Train models
    lg = LogisticRegression(C=0.1)
    lg.fit(xtrain_flat, ytrain)
    sv = SVC()
    sv.fit(xtrain_flat, ytrain)

    # Define class labels
    dec = {0: 'No Tumor', 1: 'Pitutary Tumor', 2: 'Giloma Tumor', 3: 'Meningioma Tumor'}

    # Streamlit UI
    st.title('Tumor Classification')

    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read uploaded image
        img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 0)
        img_resized = cv2.resize(img, (200, 200))
        img_flat = img_resized.reshape(1, -1)

        # Predict image class
        prediction = sv.predict(img_flat)

        # Display image and prediction
        st.image(img_resized, caption=f"Predicted class: {dec[prediction[0]]}", use_column_width=True)


