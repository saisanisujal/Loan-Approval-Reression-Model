print("---SCRIPT IS STARTING---")
from flask import Flask,render_template,request
import pickle

with open("project loan.pkl","rb")as file:
    model=pickle.load(file)

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    person_age=int(request.form["person_age"])
    person_gender=int(request.form["person_gender"])
    person_education=int(request.form["person_education"])
    person_income=int(request.form["person_income"])
    person_emp_exp=int(request.form["person_emp_exp"])
    person_home_ownership=int(request.form["person_home_ownership"])
    loan_amnt=int(request.form["loan_amnt"])
    loan_intent=int(request.form["loan_intent"])
    loan_int_rate=int(request.form["loan_int_rate"])
    loan_percent_income=int(request.form["loan_percent_income"])
    cb_person_cred_hist_length=int(request.form["cb_person_cred_hist_length"])
    credit_score=int(request.form["credit_score"])
    previous_loan_defaults_on_file=int(request.form["previous_loan_defaults_on_file"])

    prediction=model.predict([[person_age,person_gender,person_education,person_income,person_emp_exp,person_home_ownership,loan_amnt,loan_intent,loan_int_rate,loan_percent_income,cb_person_cred_hist_length,credit_score,previous_loan_defaults_on_file]])


    if prediction[0]==1:
        xyz="Loan Approved"
    else: 
        xyz="Loan Not Approved"
    
    return render_template("answer.html",prediction=xyz)


if __name__==("__main__"):
    app.run(debug=True)