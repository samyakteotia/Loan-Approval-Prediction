from flask import Flask, request, render_template
import pickle
import numpy as np
import os

app = Flask(__name__, static_folder='../static', template_folder='../templates')

# Load model
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get form data
            gender = request.form.get('gender')
            married = request.form.get('married')
            dependents = request.form.get('dependents')
            education = request.form.get('education')
            employed = request.form.get('employed')
            credit = float(request.form.get('credit', 0))
            area = request.form.get('area')
            ApplicantIncome = float(request.form.get('ApplicantIncome', 0))
            CoapplicantIncome = float(request.form.get('CoapplicantIncome', 0))
            LoanAmount = float(request.form.get('LoanAmount', 0))
            Loan_Amount_Term = float(request.form.get('Loan_Amount_Term', 0))

            # Feature engineering
            male = 1 if gender == "Male" else 0
            married_yes = 1 if married == "Yes" else 0
            dependents_1 = 1 if dependents == '1' else 0
            dependents_2 = 1 if dependents == '2' else 0
            dependents_3 = 1 if dependents == '3+' else 0
            not_graduate = 1 if education == "Not Graduate" else 0
            employed_yes = 1 if employed == "Yes" else 0
            semiurban = 1 if area == "Semiurban" else 0
            urban = 1 if area == "Urban" else 0

            # Log transformations
            ApplicantIncomelog = np.log(ApplicantIncome) if ApplicantIncome > 0 else 0
            totalincomelog = np.log(ApplicantIncome + CoapplicantIncome) if (ApplicantIncome + CoapplicantIncome) > 0 else 0
            LoanAmountlog = np.log(LoanAmount) if LoanAmount > 0 else 0
            Loan_Amount_Termlog = np.log(Loan_Amount_Term) if Loan_Amount_Term > 0 else 0

            # Make prediction
            prediction = model.predict([[
                credit, ApplicantIncomelog, LoanAmountlog, Loan_Amount_Termlog,
                totalincomelog, male, married_yes, dependents_1, dependents_2,
                dependents_3, not_graduate, employed_yes, semiurban, urban
            ]])

            status = "Approved" if prediction[0] == "Y" else "Rejected"
            return render_template('prediction.html', prediction_text=f"Loan Status: {status}")

        except Exception as e:
            return render_template('prediction.html', prediction_text=f"Error: {str(e)}")

    return render_template('prediction.html')

# Vercel requires an app variable in api.py
app = app