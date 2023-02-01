import config
from flask import Flask, request, jsonify, render_template
from utils import Diabeties
import traceback

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    # return "diabeties Prediction"


@app.route('/predict_disease', methods = ['GET','POST'])
def predict_disease():
    try:
        if request.method == 'POST':
            data = request.form.get

            print("Data :: ", data)
            Glucose  = eval(data('Glucose'))
            BloodPressure = eval(data('BloodPressure'))
            SkinThicknes = eval(data('SkinThicknes'))
            Insulin = eval(data('Insulin'))
            BMI    = eval(data('BMI'))
            DiabetesPedigreeFunction  = eval(data('DiabetesPedigreeFunction'))
            Age = eval(data('Age'))
            
            diabetes= Diabeties(Glucose,BloodPressure,SkinThicknes,Insulin,BMI,DiabetesPedigreeFunction,Age)
            predict_disease = diabetes.get_prediction()

            # return  jsonify({"Result" : f"Disease Prediction class is  : {predict_disease}"})
            if predict_disease == 0:
                return render_template('index.html', prediction = "NO")
            else:
                return render_template('index.html', prediction = "YES")

        else:
            data = request.args.get

            print("Data :: ", data)
            Glucose  = eval(data('Glucose'))
            BloodPressure = eval(data('BloodPressure'))
            SkinThicknes = eval(data('SkinThicknes'))
            Insulin = eval(data('Insulin'))
            BMI    = eval(data('BMI'))
            DiabetesPedigreeFunction = eval(data('DiabetesPedigreeFunction'))
            Age = eval(data('Age'))

            diabetes= Diabeties(Glucose,BloodPressure,SkinThicknes,Insulin,BMI,DiabetesPedigreeFunction,Age)
            predict_disease = diabetes.get_prediction()
            

           

            # return  jsonify({"Result" : f"Disease Prediction class is  : {predict_disease}"})
            if predict_disease == 0:
                return render_template('index.html', prediction = "NO")
            else:
                return render_template('index.html', prediction = "YES")

    except:
        print(traceback.print_exc())
        return  jsonify({"Message" : "Unsuccessful"})



if __name__ =='__main__':
    app.run(host = '0.0.0.0', debug =False, port= config.PORT)