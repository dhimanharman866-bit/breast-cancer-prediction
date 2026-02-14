# Breast Cancer Risk Prediction Web App

This project is a Flask-based machine learning web application that predicts the risk of breast cancer (malignant or benign) based on diagnostic measurements. The backend uses a trained scikit-learn classification model, and the frontend provides a simple, professional user interface.

---

## Overview

The model is trained on the Breast Cancer Wisconsin dataset and originally uses 30 diagnostic features.  
For better usability, the web interface collects only the most important 5 features.  
The remaining features are automatically filled using training-set mean values to preserve model accuracy and stability.

---

## Features

- Machine learning–based cancer risk prediction  
- Probability output (confidence score)  
- Flask web interface  
- Professional dark-blue user interface  
- Mean-value padding to avoid accuracy loss  
- Ready for deployment on cloud platforms  

---

## Input Parameters

The web application accepts the following inputs:

- Mean Radius  
- Mean Texture  
- Mean Perimeter  
- Mean Area  
- Mean Smoothness  

All inputs must be numeric.

---

## Prediction Output

- Benign: No cancer detected  
- Malignant: Cancer detected  
- Probability score shown as a percentage  

---

## Project Structure

Cancer Detection/
│── app.py
│── cancer_model.pkl
│── feature_means.pkl
│── requirements.txt
│── templates/
│ └── index.html
│── static/
│ └── style.css

---

## Technologies Used

- Python  
- Flask  
- NumPy  
- scikit-learn  
- Joblib  
- HTML and CSS  

---

## How It Works

1. User enters diagnostic values in the web form  
2. Input values are combined with training feature means  
3. Data is passed to the trained machine learning model  
4. The model outputs a malignancy probability  
5. The result is displayed on the web page  

---

## Installation (Local Setup)

1. Clone the repository:
git clone <repository-url>


2. Create and activate a virtual environment:


py -3.10 -m venv venv
venv\Scripts\activate


3. Install dependencies:


pip install -r requirements.txt



4. Run the application:


python app.py


5. Open your browser and visit:


http://127.0.0.1:10000


---

## Deployment

The application can be deployed on platforms such as Render using:

- Build command:


pip install -r requirements.txt


- Start command:


python app.py


---

## Accuracy Considerations

- Original model accuracy (30 features): approximately 96–98 percent  
- Accuracy with mean-value padding: approximately 90–94 percent  
- Zero-padding is avoided to prevent significant accuracy degradation  

---

## Disclaimer

This application is intended for educational and demonstration purposes only.  
It is not designed for medical diagnosis or clinical decision-making.

---

## Author
Developed as a machine learning and Flask integration project for learning and demonstration purposes.
