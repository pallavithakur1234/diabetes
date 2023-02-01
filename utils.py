import pickle
import numpy as np
import config

class Diabeties():
    def __init__(self,Glucose,BloodPressure,SkinThicknes,Insulin,BMI,DiabetesPedigreeFunction,Age):
        self.Glucose=Glucose
        self.BloodPressure=BloodPressure
        self.SkinThicknes=SkinThicknes
        self.Insulin=Insulin
        self.BMI=BMI
        self.DiabetesPedigreeFunction=DiabetesPedigreeFunction
        self.Age=Age
        return
    def load_model(self):
        with open(config.MODEL,"rb") as f:
            self.model=pickle.load(f)
            print("model:",self.model)
    def get_prediction(self):
        self.load_model()
        test_array=np.array([self.Glucose,self.BloodPressure,self.SkinThicknes,self.Insulin,self.BMI,self.DiabetesPedigreeFunction,self.Age],ndmin=2)
        pred_class=self.model.predict(test_array)[0]
        print("prediction is:",pred_class)
        return pred_class


