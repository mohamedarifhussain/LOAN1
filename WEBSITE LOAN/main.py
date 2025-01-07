import joblib
import pandas as pd
import numpy as np

model = joblib.load("TEST\loan_predictor.pkl")


gender = input("Enter your Gender (M/F):")
marital_status = input("Are you Married (M NM):")
dependents = input("Enter number of dependents (0/1/2/3+):")
education = input("Are you Graduated (Y/N):")
employment = input("Are you self-employeed (Y/N):")
applicant_income = int(input("Enter Applicant's Income:"))
co_applicant_income = int(input("Enter co-applicant's income:"))
loan_amount = int(input(("Enter the loan amount:")))
loan_amount_term = int(input(("Enter Loan Amount Term: ")))
credit_history = int(input("Credit History (Good: 1 / Bad: 0)"))
area = int(input("Enter where you live (Rural:0 / semi-urban: 1 / Urban: 2)"))

if gender == "M":
          gender = 1
else:
        gender = 0

if marital_status == "M":
        marital_status = 1
else:
        marital_status=0

if dependents=="0":
        dependents=0
elif dependents=="1":
        dependents=1
elif dependents=="2":
        dependents=2
else:
        dependents=3

if education=="Y":
        education=1
else:
        education=0

if employment=="Y":
        employment=1
else:
        employment=0


input_features = pd.DataFrame({ 'Gender':[gender], 
                                       'Married':[marital_status], 
                                       'Dependents':[dependents], 
                                       'Education':[education],
                                       'Self_Employed':[employment], 
                                       'ApplicantIncome':[applicant_income], 
                                       'CoapplicantIncome':[co_applicant_income], 
                                       'LoanAmount':[loan_amount], 
                                       'Loan_Amount_Term':[loan_amount_term], 
                                       'Credit_History':[credit_history], 
                                       'Property_Area':[area]})

prediction = model.predict(input_features)
prediction = int(np.array(prediction)[0])
result = "You are eligible for Loan \n Thank you" if prediction == 1 else "Sorry you are not eligible for Loan\n Thank you"
print(result)







