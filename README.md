# Loan Status Prediction using Machine Learning

## Overview

This project involves predicting the loan approval status using machine learning techniques. The dataset used for this project is split into training and testing datasets. The models applied in this project include Random Forest Classifier, Decision Tree Classifier, and Logistic Regression.

## Project Structure

- `train.csv` - Training dataset
- `test.csv` - Testing dataset
- `model.pkl` - Serialized model file

## Dependencies

To run this project, you need to install the following Python libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```
# Data Preprocessing
## Load Data:

Training and testing datasets are loaded using pandas.
## Handle Missing Values:

Numerical missing data is filled with the mean value.
Categorical missing data is filled with the mode value.
## Feature Engineering:

Log transformations are applied to skewed features to normalize their distribution.
Categorical features are converted into dummy variables.
## Feature Selection:

Irrelevant columns are dropped from the dataset.
Model Training
# Random Forest Classifier:

Trained on the preprocessed data.
Accuracy is computed and displayed.

<img width="322" alt="Screenshot 2024-09-15 132340" src="https://github.com/user-attachments/assets/f2dbccc7-480d-4e51-bee2-061ea160e8f6">

# Decision Tree Classifier:

Trained on the preprocessed data.
Accuracy is computed and displayed.

<img width="333" alt="Screenshot 2024-09-15 132346" src="https://github.com/user-attachments/assets/6d344879-de69-4196-8e0a-59720c0c44a4">

# Logistic Regression:

Trained on the preprocessed data.
Accuracy is computed and displayed.

<img width="321" alt="Screenshot 2024-09-15 132352" src="https://github.com/user-attachments/assets/4a47c399-dd77-4a1c-8f88-be2923a4b142">

# Confusion Matrix:

A confusion matrix is generated for the Random Forest Classifier.

<img width="282" alt="Screenshot 2024-09-15 132737" src="https://github.com/user-attachments/assets/2078fec1-7005-4a0b-8b03-7fcb211725df">

# Model Serialization:

The trained Random Forest model is saved as model.pkl using pickle.

# User Interface and Form for Loan Status Analysis
The Flask app includes a simple, user-friendly web-based interface where users can input various details related to a loan application. These details include personal and financial information, such as gender, marital status, dependents, education, employment status, credit history, income, and loan amount.

# Features of the Form:
## Gender:
The user selects whether the applicant is male or female.
## Marital Status:
The user can choose between "Yes" or "No" to indicate if the applicant is married.
## Dependents:
The form allows the user to select the number of dependents from options such as 0, 1, 2, or "3+".
## Education:
The user specifies whether the applicant is a graduate or not.
## Employment Status: 
The form captures whether the applicant is self-employed.
## Credit History: 
The user enters a numerical value indicating the applicant's credit score.
## Property Area: 
The form allows the user to select between urban, semi-urban, and rural areas for the property location.
## Applicant Income and Coapplicant Income: 
Users input their income details, which are used in the backend for calculating total income and log transformations.
## Loan Amount and Loan Term: 
These fields capture the amount of the loan and the loan term, respectively.

<img width="801" alt="Screenshot 2024-09-15 133012" src="https://github.com/user-attachments/assets/579b117e-8f12-4cdb-85bc-237560b2d09c">

# Backend Processing:
Once the user submits the form, the inputs are processed in the backend to create the necessary features for the machine learning model. Categorical values like gender, marital status, and education are encoded into numerical formats. The applicant's income, loan amount, and loan term undergo log transformations to improve the prediction model's accuracy.

The prediction result (loan approval status) is then displayed on a new page, informing the user whether their loan is likely to be approved or not.

This streamlined form makes it easy for users to interact with the loan prediction model and quickly receive feedback based on their inputs.
